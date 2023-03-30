from flask import Flask, jsonify
# import psycopg2
from settings import DATABASE, USER, PASSWORD
from models.account import Account
from db import get_db, close_db


app = Flask(__name__, template_folder='template-folder')

app.config.from_mapping(
    DATABASE=DATABASE,
    USER=USER,
    PASSWORD=PASSWORD)


# @app.route('/accounts/')
# def show_accounts():
#     # conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'], password=app.config['PASSWORD'])
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM accounts;')
#     accounts = cursor.fetchall()
#     account_dicts = [Account(account).__dict__ for account in accounts]
#     # close_db()
#     return jsonify(account_dicts)



# @app.route('/accounts/<user_id>')
# def show_account(user_id):
#     #print(type(user_id))
#     with get_db() as conn, conn.cursor() as cursor:
#         if user_id.isdigit():
#         #conn = get_db()
#         #cursor = conn.cursor()
#             cursor.execute("SELECT * FROM accounts WHERE id = %s LIMIT 1;", (user_id,))
#             account_values = cursor.fetchone()
#             return jsonify(Account(account_values).__dict__)
#         else:
#             cursor.execute("SELECT * FROM accounts WHERE username like %s LIMIT 1;", (user_id,))
#             account_values = cursor.fetchone()
#             return jsonify(Account(account_values).__dict__)

@app.route('/accounts/')
def show_accounts():
    with get_db() as conn, conn.cursor() as cursor:
        account_details = Account.get_all(cursor)
        return account_details


@app.route('/accounts/<user_id>')
def show_account(user_id):
    #print(type(user_id))
    with get_db() as conn, conn.cursor() as cursor:
        #if user_id.isdigit():
        #conn = get_db()
        #cursor = conn.cursor()
            account_details = Account.find_by_id(cursor, user_id)
            return account_details
       # else:
        #    cursor.execute("SELECT * FROM accounts WHERE username like %s LIMIT 1;", (user_id,))
        #    account_values = cursor.fetchone()
        #    return jsonify(Account(account_values).__dict__)

#@app.route('/accounts/<username>')
#def show_account_username(username):
#    conn = get_db()
#    cursor = conn.cursor()
#    cursor.execute("SELECT * FROM accounts WHERE username = %s LIMIT 1;", username)
#    account_values = cursor.fetchone()
#    return jsonify(Account(account_values).__dict__)


if __name__ == "__main__":
    app.run(debug=True)
