from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def living(self):
        pass

class dog (Animal):
    def __init__(self,name):
        self.name=name

    def living(self):
        print("dog is moving")

germanshephard = dog("germanshephard")
germanshephard.living()