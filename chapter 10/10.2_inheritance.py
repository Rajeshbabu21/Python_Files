class human:
    def eat(self):
        print("i can eat")

        def work(self):
            print("i can work")

class male(human): # ist derive class and base class
    def flirt(self):
        print("i can flirt")

        def work(self):
            super().work() #for both
            print("i can code") #it will overwrite
        

male_1 = male()
male_1.eat()
male_1.flirt()

