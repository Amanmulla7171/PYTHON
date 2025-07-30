class Car:
    def set_details(self,brand,color):
        self.brand=brand
        self.color=color

    def show_details(self):
            print(f'This car is a {self.brand} and {self.color}')
        

car1=Car()
car1.set_details('tesla','blue')
car1.show_details()

car2=Car()
car2.set_details('TATA','white')
car2.show_details()
