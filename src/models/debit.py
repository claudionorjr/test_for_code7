from data.sql_alchemy import database


class DebitModel(database.Model):
    __tablename__ = "debits"


    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer)
    reason = database.Column(database.String(120), nullable=False)
    debit_date = database.Column(database.DateTime)
    amount = database.Column(database.Float(precision=2))


    def __str__(self,user_id, reason, debit_date, amount):
        self.user_id = user_id
        self.reason = reason
        self.debit_date = debit_date
        self.amount = amount
