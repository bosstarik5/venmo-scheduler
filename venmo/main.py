from venmo_api import Client
from getpass import getpass
import PySimpleGUI as sg

auth = False

while not auth:
    layout = [
        [sg.Text('Login')],
        [sg.Text('Username: ', size =(15, 1)), sg.InputText()],
        [sg.Text('Password: ', size =(15, 1)), sg.InputText('', key='Password', password_char='*')],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Login', layout)
    event, values = window.read()

    username, password = values[0], values[1]

    try:
        access_token = Client.get_access_token(username=username, password=password)
        auth = False
    except:
        window['-TEXT-'].update('Incorrect Authentication')

    window.close()

auth = False
while not auth:
    username = input('Username: ')
    password = getpass()
    try:

        auth = True
    except:
        print('Incorrect Authentication')

client = Client(access_token=access_token)
current_user = Client.my_profile(client)

users = client.user.get_user_friends_list(user_id=current_user.id)
print(users[34])
# for idx, user in enumerate(users):
#     print(idx, ": ", user.username)

