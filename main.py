class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)      
    def perimeter(self):
        return 3.14*(self.radius*2)
number = float(input("Enter a radius: "))
my_circle = Circle(number)

print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())