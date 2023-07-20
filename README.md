# Step Resume Bot
Resume writing bot specifically for IT STEP

## Python Version
Download [Python 3.11.4](https://www.python.org/downloads/release/python-3114/)

## Installing Packages
```
pip install -U aiogram
pip install python-dotenv 
pip install pysqlcipher3
pip install reportlab
pip install cryptography
```

## Database
### SQLite
You can download either [SQlite](https://www.sqlite.org/download.html) or [SQLiteStudio](https://github.com/pawelsalawa/sqlitestudio/releases)

## Bot Launch
```
step-resume-bot/  
├─ public/  
├─ src/  
├─ tests/  
├─ .gitignore  
├─ LICENSE  
├─ README.md  
├─ run.py  <-- run this file
```
### .env Settings
```
BOT_TOKEN={YOUR TOKEN}
BOT_USERNAME={YOUR NAME}
ENCRYPTION_KEY={WILL CREATE AFTER FIRST LAUNCH}
```