import requests
from src.models.debit import DebitModel


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response:
        return response.json()
    return {'message': 'Request not found!.'}, 404

def with_debits():
    users = get_users()
    debtors = []
    for user in users:
        if DebitModel.query.filter_by(user_id=user['id']).first():
            debtors.append(user)
    return debtors
