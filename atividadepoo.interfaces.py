#1 Criando uma interface
#Crie uma interface chamada Pagamento com um método abstrato processar(valor).
#Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. Mostre como chamar processar() para cada uma.

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R${valor} no cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R${valor} via boleto.")

cartao = CartaoCredito()
boleto = Boleto()
cartao.processar(100)
boleto.processar(200)


#2 Interface múltipla
#Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()).
#rie uma classe Computador que implemente ambas. Mostre seu uso.
from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado.")

    def desligar(self):
        print("Computador desligado.")

pc = Computador()
pc.ligar()
pc.desligar()


#3 Interface em herança múltipla
#Crie uma interface Imprimivel com o método imprimir().
#Crie outra interface Exportavel com o método exportar(). Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Relatório impresso.")

    def exportar(self):
        print("Relatório exportado.")

r = Relatorio()
r.imprimir()
r.exportar()

#4 Forçando contrato
#Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). 
#Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. 
# #que acontece quando você tenta instanciá-la? Corrija o código.

from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print("Objeto salvo na memória.")

#repo = RepositorioMemoria()  gera erro

#correção
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print("Objeto salvo na memória.")

    def buscar(self, id):
        print(f"Buscando objeto com id {id} na memória.")

repo = RepositorioMemoria()
repo.salvar("dados")
repo.buscar(1)
