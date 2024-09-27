class Animal:
    def __init__(self,name):
        self.name =name
        
    def speak(self):
            
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woff"
        
        
        
class Cat(Animal):
        def speak(self):
            return f"{self.name} says meong"
        
dog = Dog("Buudy")
cat = Cat("whiskers")

print(dog.speak())
print(cat.speak())
