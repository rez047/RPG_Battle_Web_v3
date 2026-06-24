from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import random


app = Flask(__name__)


app.config["SECRET_KEY"] = "secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rpg.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(app)


login_manager = LoginManager(app)

login_manager.login_view = "login"



# =========================
# DATABASE MODELS
# =========================


class User(db.Model, UserMixin):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True
    )

    password = db.Column(
        db.String(200)
    )


    hero = db.relationship(
        "Hero",
        backref="user",
        uselist=False
    )


    def set_password(self,password):

        self.password = generate_password_hash(password)



    def check_password(self,password):

        return check_password_hash(
            self.password,
            password
        )




class Hero(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    name=db.Column(db.String(50))

    role=db.Column(db.String(30))

    hp=db.Column(db.Integer)

    max_hp=db.Column(db.Integer)

    attack=db.Column(db.Integer)

    level=db.Column(
        db.Integer,
        default=1
    )

    xp=db.Column(
        db.Integer,
        default=0
    )

    user_id=db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )



@login_manager.user_loader
def load_user(id):

    return User.query.get(int(id))



# =========================
# GAME ENGINE
# =========================


class Enemy:


    def __init__(self, level=1):

        enemies=[

            ("Goblin",80,15),

            ("Orc",160,25),

            ("Dragon",300,45)

        ]


        enemy=random.choice(enemies)


        self.name=enemy[0]

        self.hp=enemy[1] + level*20

        self.attack=enemy[2] + level*5



enemy_memory={}



def attack_player(hero,enemy):


    damage=hero.attack


    critical=False


    if random.randint(1,5)==1:

        damage*=2

        critical=True



    enemy.hp -= damage


    return damage,critical




def enemy_attack(hero,enemy):

    hero.hp -= enemy.attack





def level_up(hero):


    if hero.xp >=100:

        hero.level +=1

        hero.attack +=10

        hero.max_hp +=30

        hero.hp=hero.max_hp

        hero.xp=0

        return True


    return False





# =========================
# ROUTES
# =========================


@app.route("/", methods=["GET","POST"])
def register():


    if request.method=="POST":


        user=User(
            username=request.form["username"]
        )


        user.set_password(
            request.form["password"]
        )


        db.session.add(user)

        db.session.commit()


        login_user(user)


        return redirect("/dashboard")



    return render_template("register.html")





@app.route("/login",methods=["GET","POST"])
def login():


    if request.method=="POST":


        user=User.query.filter_by(
            username=request.form["username"]
        ).first()



        if user and user.check_password(
            request.form["password"]
        ):

            login_user(user)

            return redirect("/dashboard")



    return render_template("login.html")






@app.route("/dashboard",methods=["GET","POST"])
@login_required
def dashboard():


    if request.method=="POST":


        hero=Hero(

            name=request.form["name"],

            role=request.form["role"],

            hp=150,

            max_hp=150,

            attack=30,

            user_id=current_user.id

        )


        db.session.add(hero)

        db.session.commit()



    return render_template(
        "dashboard.html",
        hero=current_user.hero
    )






@app.route("/battle",methods=["GET","POST"])
@login_required
def battle():


    hero=current_user.hero


    if current_user.id not in enemy_memory:

        enemy_memory[current_user.id]=Enemy(
            hero.level
        )


    enemy=enemy_memory[current_user.id]


    message=""


    if request.method=="POST":


        action=request.form["action"]



        if action=="attack":


            damage,critical=attack_player(
                hero,
                enemy
            )


            message=f"You dealt {damage} damage"


            if critical:

                message+=" Critical hit!"



            if enemy.hp>0:

                enemy_attack(
                    hero,
                    enemy
                )


            else:

                hero.xp +=50

                level_up(hero)

                enemy_memory[current_user.id]=Enemy(
                    hero.level
                )




        if action=="heal":


            hero.hp=min(
                hero.max_hp,
                hero.hp+40
            )


            message="Potion used"



        db.session.commit()



    if hero.hp <=0:

        return render_template(
            "gameover.html"
        )



    return render_template(
        "battle.html",
        hero=hero,
        enemy=enemy,
        message=message
    )





@app.route("/logout")
def logout():

    logout_user()

    return redirect("/")





with app.app_context():

    db.create_all()



if __name__=="__main__":

    app.run(debug=True)