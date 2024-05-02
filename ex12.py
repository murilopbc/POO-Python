class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade  # Atributo protegido

    def cumprimentar(self):
        return f"Olá, eu sou {self.nome}!"

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("A idade não pode ser negativa.")


# Criando uma instância
pessoa1 = Pessoa(nome="João", idade=25)

# Obtendo e imprimindo a idade usando o método getter
idade_atual = pessoa1.idade
print(f"Idade atual: {idade_atual}")  # Saída: Idade atual: 25

# Usando o método setter para modificar a idade
pessoa1.idade = 30

# Obtendo e imprimindo a nova idade usando o método getter
nova_idade = pessoa1.idade
print(f"Nova idade: {nova_idade}")  # Saída: Nova idade: 30

# Tentando definir uma idade negativa
pessoa1.idade = -5  # Isso imprimirá "A idade não pode ser negativa."
