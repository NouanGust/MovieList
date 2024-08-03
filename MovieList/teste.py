import random
# Lista de filmes

filmes = ["Alice", "Miranha", "Indiana Jones", "X-men"]


# Adicionar filmes

def adicionarFilmes():
    filme = input("Digite o filme para adicionar: ")
    filmes.append(filme)

# Vizualizar filme

def listarFilmes():
    for i in filmes:
        print(i)
        

# Sortear filmes da lista
def sortear():
    index = random.randint(0, len(filmes))
    print(index)
    print(filmes[index])
    filmes.pop(index)
    
while True:
    print("Lista de Filmes")
    print("1 -- Ver Lista")
    print("2 -- Adicionar filme")
    print("3 -- Sortear filme")
    print("4 -- Sair")
    escolha = input("Ecolha a opção: ")

    match escolha:
        case "1":
            listarFilmes()
        case "2":
            adicionarFilmes()
        case "3":
            sortear()
        case "4":
            quit()

# Mostrar filme sorteado e tirar da lista (Marcar como visto)