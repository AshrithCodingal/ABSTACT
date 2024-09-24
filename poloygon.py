from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class dog (Animal):
    def __init__(self,name):
        self.name=name
    def move(self):
        print("I can bark")
        print("dog")


class  human (Animal):
    def __init__(self,name):
        self.name=name
    def move(self):
        print("I can walk")
        print("Human")

class cat (Animal):
    def __init__(self,name):
        self.name=name
    def move(self):
        print("I can meow")
        print("cat")

class cow (Animal):
    def __init__(self,name):
        self.name=name
    def move(self):
        print("I can moo")
        print("cow")

H=human("human")
H.move()

D=dog("dog")
D.move()

C=cow("cow")
C.move()

C=cat("cat")
C.move()
