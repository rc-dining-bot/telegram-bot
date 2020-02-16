# telegram-bot
Telegram bot server for RC Dining Bot to replace @rcmealbot which became dysfunctional after
change of data format in end of 2019.

It now comes with a Graphic User Interface design.

## Functionality
1. Check daily meal menus: `/breakfast` and `/dinner` 
    * Note: command with payload display menu of the day specified.
    * e.g. `/breakfast tomorrow` or `/dinner yesterday`
2. Check settings: `/settings`
    * Menu of customizable settings available
3. Hide menu items: `/hidden` or `Toggle Menu Visibility` button
    * Hide certain cuisines and menu items you no long wish to see in the menu.
    * e.g. vegetarians can choose to hide non-vegetarian options
4. Turn on menu notification: `/subscribe_breakfast` and `/subscribe_dinner`
    * Alternatively, `Toggle Notification Settings` button
    * Breakfast will be broadcast at 12 AM daily
    * Dinner will be broadcast at 3 PM daily
    * TODO: customizable broadcast timings
5. Help menu: `/help`
6. (For COVID-19 period) Check RVRC dining hall occupancy: /rvcount
    * We have only acquired the access to RVRC dining hall data so far.

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

## License : [MIT](./LICENSE)
