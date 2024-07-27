#add import
from question_d import Stock



def main():

    stocks = \
    [Stock('AAPL', 'Apple Inc'), 
    Stock('CAT', 'Caterpillar'),
    Stock('EK', 'Eastman Kodak'),
    Stock('GOOG', 'Google Inc'),
    Stock('MSFT', 'Microsoft')]

    #display symbol and company name

    print('Here is a stock report: ')
    print('Company\t\tSymbol')
    
    for i in stocks:
        
        print(f"{i.get_company_name():<15} {i.get_symbol()}")

main()