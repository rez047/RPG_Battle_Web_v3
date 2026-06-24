# ⚔️ RPG Battle Web Game (Flask)

A browser-based RPG battle game built using Python Flask.

The application allows players to:

- Create an account
- Login securely
- Create a hero
- Choose a hero class
- Fight enemies
- Gain XP
- Level up
- Increase stats
- Use healing potions
- Battle different enemies

---

# 🚀 How To Run The Project

## 1. Check Python Installation

Make sure Python is installed:

```bash
python --version
```

Example:

```
Python 3.x.x
```

Check pip:

```bash
pip --version
```

---

# 2. Open The Project Folder

Open terminal inside the project directory.

Example:

```bash
cd RPG_Battle_Web_v3
```

The folder should contain:

```
app.py
requirements.txt
templates/
static/
```

---

# 3. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

This reads the requirements file and installs all libraries needed by the project.

---

# 📦 Installed Packages Explained

## Flask

Installed using:

```
Flask
```

### Purpose

Flask is the web framework powering the RPG game.

It handles:

- Starting the web server
- Creating pages
- Managing routes
- Receiving user actions
- Returning HTML responses


Example:

```python
@app.route("/battle")
def battle():

    return render_template("battle.html")
```

When the player opens:

```
/battle
```

Flask loads the battle page.

---

# Flask-SQLAlchemy

Installed using:

```
Flask-SQLAlchemy
```

### Purpose

Flask-SQLAlchemy connects Flask to a database.

It saves game information permanently.

Used for storing:

- User accounts
- Heroes
- Hero classes
- HP
- Attack stats
- XP
- Levels


Example:

```python
class Hero(db.Model):

    name=db.Column(db.String(50))
```

This creates a Hero database table.

Without the database:

- Heroes disappear after closing the program

With SQLAlchemy:

- Progress is saved

---

# Flask-Login

Installed using:

```
Flask-Login
```

### Purpose

Handles authentication.

It manages:

- Login
- Logout
- User sessions
- Protected pages


Example:

```python
@login_required
def battle():

    return "Fight!"
```

Only logged-in players can access battles.

---

# Werkzeug

Installed using:

```
Werkzeug
```

### Purpose

Werkzeug provides security utilities used by Flask.

This project uses it to secure passwords.

Instead of saving:

```
password123
```

The database stores an encrypted hash:

```
pbkdf2:sha256:...
```

Example:

```python
generate_password_hash(password)
```

This protects player accounts.

---

# ▶ Running The Game

After installing requirements:

```bash
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

Open:

```
http://127.0.0.1:5000
```

---

# 📁 Project Structure

```
RPG_Battle_Web_v3/

│
├── app.py

├── requirements.txt


├── templates/

│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── battle.html
│   └── gameover.html


└── static/

    ├── css/

    │   └── style.css

    │

    └── images/

        ├── warrior.png
        ├── mage.png
        ├── archer.png
        └── enemies/
```

---

# 🎮 Game Flow

## 1. Create Account

The player registers.

Saved in the database:

- Username
- Encrypted password


---

## 2. Create Hero

The player chooses:

```
Warrior
Mage
Archer
```

Each class has different stats.

Example:

Warrior:

```
High HP
Medium Attack
```

Mage:

```
Low HP
High Attack
```

---

## 3. Enter Battle

The game creates a random enemy.

Examples:

```
Goblin
Orc
Dragon
```

---

## 4. Attack System

When clicking:

```
⚔ Attack
```

The game calculates damage:

```
Hero attack
+
Critical chance
```

Enemy responds with an attack.

---

## 5. Experience System

Winning gives XP:

```
+50 XP
```

At:

```
100 XP
```

The hero levels up.

Rewards:

- More HP
- More Attack
- Higher level

---

## 6. Potion System

The player can heal:

```
🧪 Potion
```

It restores HP.

---

# 🧠 Concepts Practiced

This project demonstrates:

## Flask

- Routes
- Templates
- Forms


## OOP

Classes:

```python
Hero()
Enemy()
User()
```

Objects represent game entities.


## Database

Tables:

```
User
Hero
```


## Authentication

Login system with sessions.


## Game Logic

- Random enemies
- Damage calculations
- XP
- Levels

---

# 🔮 Future Improvements

Possible upgrades:

- Inventory system
- Weapons
- Armor
- Multiple heroes
- Boss battles
- Skills and magic
- Leaderboard
- Multiplayer mode
- Admin dashboard
- API version


---

# Requirements

Current:

```
Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug
```

They provide:

| Package | Purpose |
|---|---|
| Flask | Web application |
| Flask-SQLAlchemy | Database |
| Flask-Login | Authentication |
| Werkzeug | Password security |

---

# Quick Start

```bash
pip install -r requirements.txt

python app.py
```

Open:

```
http://127.0.0.1:5000
```

Enjoy the battle ⚔️