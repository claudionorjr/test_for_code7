import requests

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response:
        return response.json()
    return {'message': 'Request not found!.'}, 404

#print(get_users()[0]['name'])
    #[Running] python -u "c:\Users\Blausius\Desktop\test-code7\src\users.py"
    #Leanne Graham

def with_debits():
    pass