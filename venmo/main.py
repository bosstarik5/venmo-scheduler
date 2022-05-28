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



# access token = 7051ec720feeca9b8e678497ea8562637be9048f9cc6b48567a56bf25605d0ec
# aryanid = "2589517210976256921"
# # nidhiid = '2727255847469056507'
# client = Client(access_token=access_token)
# users = client.user.get_user_friends_list()
# for user in users:
#     print(user.username)

# client.user.get_user_transactions(user_id='0000000000000000000',
#                                      callback=callback)

# 94700242-76F1-4C93-55O5-7YL79V669MD6 -> 86806993-99G5-6Q41-34Y2-3RH66F485QK3 -> deviceid
