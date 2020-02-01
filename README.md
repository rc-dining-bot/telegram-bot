# telegram-bot
Telegram bot server for RC Dining Bot to replace @rc_meal_bot which became dysfunctional after
change of data format in end of 2019.

## Requirement
* Set up PostgreSQL database locally/online
* Configure `.env` file with template `.env.example`

## Setup Instructions
1. `pipenv install`
2. `pipenv run python src/bot.py`

## Database Setup Instructions (PostgreSQL for local setup)
1. Download and install [PostgreSQL](https://www.postgresql.org/download/)
3. Create user for the bot to access the database with. `createuser --interactive --pwprompt`
4. Create database for the bot. `createdb -0 name_of_user name_of_db;`
5. Launch psql in database mode.
6. Create tables using queries in db_setup.txt.
7. Grant permissions if necessary for every table.
8. Configure `.env` file accordingly.