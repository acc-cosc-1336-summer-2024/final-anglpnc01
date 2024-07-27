#add import
from question_a import stock_purchase_history

def display_menu():

    print('1 - Display Stock Purchase History: ')
    print('2 - Exit')

def run_menu():

    choice == '1'

    while(choice != '3'):

        display_menu()

        choice = input('Enter option: ').strip()

        handle_menu()

def handle_menu(choice):

    if(choice == '1')    :

        select_1()

    else:
        print('Exiting..')
        exit()

def select_1():

    result = stock_purchase_history

    print(f'Recent stock purchases are: {result}')
