#add import
from question_a import stock_purchase_history
from question_a import Stock

def display_menu(choice):

    stocks = stock_purchase_history()

    print('1 - Display Stock Purchase History: ')
    print('2 - Exit')

    choice == input('')

    if choice == '1':

        display_stock_report(stocks)

        continue_option()

    elif choice == '2':

        exit()

    else:

        print('Invalid option')

def display_stock_report(stocks):

    print()

    for symbol, stock in stocks.items():

        company_name = stock.get_company_name()

        print(f'{company_name}, {symbol}')

### this has to print

def continue_option():

    print('Continue?: ')
    print('1 - Yes')
    print('2- No')

    cont_choice = int(input(''))

    if cont_choice == 1:

        display_menu()

    elif cont_choice == 2:

        print('Exiting..')
        exit()

    else:
        print('Invalid entry!')
        cont_choice()

display_menu()

##DON'T KNOW WHY ERROR "CANNOT IMPORT NAME"