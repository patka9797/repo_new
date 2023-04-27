import random, string

class Robot:

    def __init__(self):
        self.name=self.name_robot()
    def reset(self):
        self.name=self.name_robot()
    def name_robot(self):
        random.seed()
        letters=random.choices(string.ascii_uppercase, k=2)
        digits=random.choices(string.digits, k=3)
        
        return ''.join(letters+digits)
