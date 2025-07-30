class Bird():
    def sound(self):
        print("birds make sound")

class Crow(Bird):
    def sound(self):
        print('crows sound "caw caw"')

class Parrot(Bird):
    def sound(self):
        print('parrot sound "squak"')
    

birds1=Crow()
bird2=Parrot()


birds1.sound()
bird2.sound()