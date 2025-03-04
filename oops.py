'''
#instances variable and methods
class dog:
    #constructor
    def __init__(self,name ,age):
        self.name=name
        self.age=age
#create a age
dog1=dog("Buddy",3)
print(dog1)
print(dog1.name)
print(dog1.age)


class car():
    def acclerate(self,name):
        print(f" Hello {name}, Let's drive ")
my_car=car() #Object initialization
my_car.acclerate("Raja")
my_car2=car()
my_car2.acclerate("Siva")
'''
class calculate():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        pass
    def add(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def multiply(a,b):
        return a*b
    
    def div(a,b):
        return a/b
x=calculate.add(3,5)
print(x)
y=calculate.sub(8,7)
print(y)
z=calculate.multiply(2,2)
print(z)
a=calculate.div(8,2)
print(a)