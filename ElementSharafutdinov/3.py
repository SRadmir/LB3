class ElementSharafutdinov:
    def __init__(self, name, symbol, number):
        self.__name = name 
        self.__symbol = symbol  
        self.__number = number  
    @property
    def name(self):
        return self.__name  

    @property
    def symbol(self):
        return self.__symbol  

    @property
    def number(self):
        return self.__number  

    def dump(self):
        print(f'Name: {self.name}')  
        print(f'Symbol: {self.symbol}')  
        print(f'Number: {self.number}') 
hydrogen = ElementSharafutdinov("Calcium", "Ca", 20)
hydrogen.dump()
