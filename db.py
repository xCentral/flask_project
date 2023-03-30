from flask import current_app
from flask import g
import psycopg2
from settings import DATABASE, USER, PASSWORD

#current_app.config.from_mapping(
#    DATABASE=DATABASE,
#    USER=USER,
#    PASSWORD=PASSWORD)


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(database=current_app.config['DATABASE'], user=current_app.config['USER'],
                                password=current_app.config['PASSWORD'])
    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def drop_records(cursor, conn, table_name):
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()
