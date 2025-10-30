#1 
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

pessoa = Pessoa("Lorena")
livro = Livro("Python para Iniciantes")

print(f"{pessoa.nome} está lendo '{livro.titulo}'")

#2
class Onibus:
    def embarcar(self):
        print("Embarcando no ônibus...")

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def ir_para_escola(self, onibus):
        print(f"{self.nome} está indo para a escola.")
        onibus.embarcar()


onibus = Onibus()
aluno = Aluno("Carlos")
aluno.ir_para_escola(onibus)

#3 
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

f1 = Funcionario("Ana")
f2 = Funcionario("João")

dep = Departamento("RH")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)

print(f"Departamento {dep.nome} tem os funcionários:")
for f in dep.funcionarios:
    print(f"- {f.nome}")

#4
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)


j1 = Jogador("Pedro", "Atacante")
j2 = Jogador("Lucas", "Goleiro")

time = Time("Estrelas FC")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)

print(f"Time {time.nome} tem os jogadores:")
for j in time.jogadores:
    print(f"- {j.nome} ({j.posicao})")

#5
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor("V8")


carro = Carro("Mustang")
print(f"Carro: {carro.modelo}, Motor: {carro.motor.tipo}")


del carro

#6
class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]


casa = Casa()
print("Comodos da casa:")
for c in casa.comodos:
    print(f"- {c.nome}")


