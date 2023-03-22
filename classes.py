class Calculation:
    def display(self):
        print("this is display function from calculation class")
    def add(self, x ,y):
        print(f'{x} and {y} is equal to : {x+y}')
    
cal = Calculation()
cal.display()
cal.add(2,3)
