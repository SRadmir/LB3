class ElementSharafutdinov:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(f'Name: {self.name}')
        print(f'Symbol: {self.symbol}')
        print(f'Number: {self.number}')
hydrogen = ElementSharafutdinov("Calcium", "Ca", 20)
hydrogen.dump()
