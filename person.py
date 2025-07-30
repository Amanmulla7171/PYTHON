class Collage:
    def __init__(self,name,heigth,age):
       self.name=name
       self.age=age
       self.height=heigth


    def persons(self):
        print(f'{self.name} with the heigth {self.height} and age {self.age}')


dkte=Collage('karan',5.5,20)
dyp=Collage('Ram',7.2,35)


dkte.persons()
dyp.persons()