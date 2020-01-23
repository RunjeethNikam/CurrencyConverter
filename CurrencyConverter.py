import requests

class CurrencyConverter:
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amont):
        initialAmount = amont
        if from_currency != "EUR":
            amont = amont / self.rates[from_currency]
        amont = round(amont * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initialAmount, from_currency, amont, to_currency))

if __name__ == "__main__":
    url = "http://data.fixer.io/api/latest?access_key=419f66de4d6729aa1593eb27d69de63db"
    c = CurrencyConverter(url)
    from_currency = input("From Country: ")
    to_currency = input("to Country: ")
    amount = int(input("Amount: "))
    c.convert(from_currency, to_currency, amount)