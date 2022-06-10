#Criar Carro
class Carro:
    def __init__(self,modelo_carro,veiculo_carro):
        self.veiculo_carro = veiculo_carro
        self.modelo_carro = modelo_carro
    def __str__(self):
        return self.veiculo_carro
    def __int__(self):
        return self.modelo_carro
def AddCarro(modelo_carro,veiculo_carro):
    ListaVeiculo_carro.append(veiculo_carro)
    ListaModelo_carro.append(modelo_carro)
ListaVeiculo_carro = []
ListaModelo_carro = []

#Criar Moto
class Moto:
    def __init__(self,veiculo_moto, modelo_moto):
        self.veiculo_moto = veiculo_moto
        self.modelo_moto = modelo_moto
    def __str__(self):
        return self.veiculo_moto
    def __str__(self):
        return self.modelo_moto
def AddMoto(veiculo_moto, modelo_moto):
    ListaVeiculo_moto.append(veiculo_moto)
    ListaModelo_moto.append(modelo_moto)
ListaVeiculo_moto = []
ListaModelo_moto = []

#Criar Capacidade Oleo
class Capacidade_Oleo:
    def __init__(self,Capacidade_Oleo):
        self.Capacidade_Oleo = Capacidade_Oleo
    def __float__(self,):
        ListaCapacidade_Oleo.append(Capacidade_Oleo)
        return self.Capacidade_Oleo
def AddCapacidade_Oleo(Capacidade_Oleo):
    ListaCapacidade_Oleo.append(Capacidade_Oleo)
ListaCapacidade_Oleo = []

#Criar Produtos
class Criar_Oleo:
    def __int__(self,fabricante,nome_produto):
        self.fabricante = fabricante
        self.nome_produto = nome_produto
    def __str__ (self):
        return self.Fabricante
    def __str__(self):
        return self.Nome_Produto
def AddProdutos(fabricante,nome_produto):
    ListaFabricante.append(fabricante)
    ListaNome_Produto.append(nome_produto)
ListaFabricante = []
ListaNome_Produto = []

#Ler Produto
def ConsultaProduto(Fabricante,Nome_Produto):

#Ler Veiculo
def ConsultaVeiculo(Veiculo,Modelo_motor):

#Ler Oleo
def ConsultaOleo(Veiculo,Modelo_motor,Capacidade_Oleo):

#Modificar veiculo
def ModificarVeiculo(Veiculo,Novo_Veiculo):

#Modificar Produtos
def ModificarProduto(Nome_Produto,Novo_Produto):

#Deletar veiculo
def DeletarVeiculo(Veiculo):

#Deletar Produtos
def DeletarProduto(Nome_Produto):

ListaVeiculo = []
ListaFabricante = []
ListaModelo_Motor = []
ListaCapacidade_Oleo = []
ListaNome_Produto = []