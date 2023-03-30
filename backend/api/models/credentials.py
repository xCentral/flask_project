

class Credentials:
    __table__ = 'credentials'
    columns = ['first_name', 'last_name', 'current_employer', 'city_of_residence', 'invested_amount', 'account_id']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))