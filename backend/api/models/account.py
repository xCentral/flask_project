from db import get_db


class Account:
    __table__ = 'accounts'
    columns = ['id', 'username', 'email', 'ip_address', 'created_at']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    @classmethod
    def find_by_id(cls, cursor, user_id):
        if user_id.isdigit():
            cursor.execute(f"SELECT * FROM {cls.__table__} WHERE id = %s LIMIT 1;", (user_id,))
            account_values = cursor.fetchone()
        else:
            cursor.execute(f"SELECT * FROM {cls.__table__} WHERE username like %s LIMIT 1;", (user_id,))
            account_values = cursor.fetchone()
        if account_values:
            return cls(account_values).__dict__

    @classmethod
    def get_all(cls, cursor):
        cursor.execute(f"SELECT * FROM {cls.__table__};")
        accounts = cursor.fetchall()
        return [cls(account).__dict__ for account in accounts]
        #return [cls(account.__dict__) for account in account_values]


#Account.find_by_id(1)
