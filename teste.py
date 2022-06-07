
""" 1 - tipo de veiculo
2 - fabricante
3 - modelo / motor
4 - capacidade de oleo
5 - numero do produto / nome do produto """


#Criar veiculo
def Tipo_de_veiculo(Veiculo,Modelo_motor, Capacidade_Oleo):
    ListaVeiculo.append(Veiculo)
    ListaModelo_Motor.append(Modelo_motor)
    ListaCapacidade_Oleo.append(Capacidade_Oleo)

#Criar Produtos
def Produtos(Fabricante,Nome_Produto):
    ListaFabricante.append(Fabricante)
    ListaNome_Produto.append(Nome_Produto)

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



""" def MostrarNota(nome):
    for x in ListaNomes:
        if x == nome:
            matricula = ListaNomes.index(nome)
        print("A nota de {} é {}".format(ListaNomes[matricula],ListaNotas[matricula]))

def RemoverNota(nome):
    for x in ListaNomes:
        if x == nome:
            matricula = ListaNomes.index(nome)
    ListaNotas.pop(matricula)
    ListaNomes.pop(matricula) """

""" escolha = 9
while escolha != 0:
    print('-'*30)
    print("Bom dia, o que deseja? ")
    print("Para cadastrar notas digite 1")
    print("Para modificar notas digite 2")
    print("Para mostrar notas digite 3")
    print("Para listar todas as notas digite 4")
    print("Para remover notas digite 5")
    print("Para encerrar digite 0")
    print('-'*30)

escolha = int(input())
while True:
    if escolha == 1:
        print('-'*30)
        aluno = str(input("Qual aluno?"))
        print('-'*30)
        nota = int(input("Qual a Nota?"))
        print('-'*30)
        AdicionarAluno(aluno,nota)
        print("Operação concluida.")
        print('-'*30)
        break
    elif escolha == 2:
        print('-'*30)
        aluno = input("Qual aluno?")
        print('-'*30)
        nota = input("Qual a nova Nota?")
        print('-'*30)
        ModificarNota(aluno,nota)
        print("Operação concluida.")
        print('-'*30)
        break
    elif escolha == 3:
        print('-'*30)
        aluno = input("Qual aluno?")
        print('-'*30)
        MostrarNota(aluno)
        print('-'*30)
        print("Operação concluida.")
        break
    elif escolha == 4:
        print('-'*30)
        MostrarTodasNota()
        print('-'*30)
        print("Operação concluida.")
        print('-'*30)
        break
    elif escolha == 5:
        print('-'*30)
        aluno = input("Qual aluno?")
        print('-'*30)
        RemoverNota(aluno)
        print('-'*30)
        print("Operação concluida.")
        break
    elif escolha == 0:
        print("fim do programa")
        break
    else:
        print("Desculpe, valor digitado é inválido")  
        break """