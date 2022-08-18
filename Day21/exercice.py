from this import d


class Animal:
    
    def __init__(self):
        self.number_of_eyes = 2

    def breath(self):
        print("Inhale, exhale")


class Fish(Animal):
    
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Doing this in water")

    def Swim(self):
        print("Swimming in water")


nemo = Fish()

nemo.breath()