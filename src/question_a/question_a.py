#write functions here, don't add input('') statements here!
def test_config():
    return True

class Stock:

    def __init__(self, symbol, company_name):

        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):

        return self.__symbol

    def get_company_name(self):

        return self.__company_name

    def stock_purchase_history():

        stock1 = Stock('AAP', 'Apple Inc')
        stock2 = Stock('CAT', 'Caterpillar Inc.')
        stock3 = Stock('EK', 'Eastman Kodak')
        stock4 = Stock('GOOG', 'Google')
        stock5 = Stock('MSFT', 'Microsoft')

        stocks = { 'Stock 1': stock1, 'Stock 2': stock2, 
                  'Stock 3': stock3, 'Stock 4': stock4, 'Stock 5': stock5}
        
        for key, stock in stocks.items()
            print((f"{key}: Symbol = {stock.get_symbol()}, Company Name = {stock.get_company_name()}"))

            