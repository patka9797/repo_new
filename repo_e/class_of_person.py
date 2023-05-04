class Person:
    
    def __init__(self, name : str, age : int):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f'Witaj {self.name}, {self.age}')

    


patrycja=Person('Patrycja',26)
print(patrycja.greet())
