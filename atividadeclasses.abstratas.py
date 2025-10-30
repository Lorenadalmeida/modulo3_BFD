#1
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

c = Cachorro()
g = Gato()
print(c.falar())  
print(g.falar())  
#2 
#a = Animal()
#TypeError: Can't instantiate abstract class Animal with abstract method falar

#3 
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

r = Retangulo(4, 5)
print("Área:", r.area())        
print("Perímetro:", r.perimetro())  

#4
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("Carro em movimento")

# Teste
#carro = Carro() dá erro

#correção
class Carro(Transporte):
    def mover(self):
        print("Carro em movimento")

    def parar(self):
        print("Carro parado")

# Teste corrigido
carro = Carro()
carro.mover()  
carro.parar()



