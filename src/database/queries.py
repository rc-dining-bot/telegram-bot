from psycopg2 import sql


def menu_query(meal):
    return sql.SQL("SELECT * FROM {table} WHERE {pkey} = %s;").format(
        table=sql.Identifier(meal),
        pkey=sql.Identifier('date'))