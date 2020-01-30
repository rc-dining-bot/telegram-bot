from psycopg2 import sql


def menu_query(meal):
    return sql.SQL("SELECT * FROM {table} WHERE {pkey} = %s;").format(
        table=sql.Identifier(meal),
        pkey=sql.Identifier('date')
    )


def settings_query(setting):
    return sql.SQL("SELECT {setting} FROM {table} WHERE {pkey} = %s;").format(
        setting=sql.Identifier(setting),
        table=sql.Identifier('user_pref'),
        pkey=sql.Identifier('chat_id')
    )


def settings_insert():
    # takes in 3 values:
    # chat_id
    # hidden cuisines table
    # favorite foods table
    return sql.SQL("INSERT INTO {table} VALUES (%s, %s, %s)").format(
        table=sql.Identifier('user_pref')
    )


def settings_update(setting):
    # takes in 2 values:
    # updated hidden cuisines table;
    # chat_id
    return sql.SQL("UPDATE {table} SET {setting} = %s WHERE {pkey} = %s;").format(
        table=sql.Identifier('user_pref'),
        setting=sql.Identifier(setting),
        pkey=sql.Identifier('chat_id')
    )
