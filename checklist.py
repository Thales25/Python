# Define a lista vazia para armazenar as tarefas
checklist = []

# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    checklist.append(tarefa)

# Função para exibir a lista de tarefas
def exibir_checklist():
    print("Lista de tarefas:")
    for tarefa in checklist:
        print("- " + tarefa)

# Função principal que permite ao usuário escolher o que fazer
def main():
    while True:
        print("\nO que você deseja fazer?")
        print("1 - Adicionar uma tarefa")
        print("2 - Exibir a lista de tarefas")
        print("3 - Sair")
        escolha = input("Digite sua escolha (1/2/3): ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            exibir_checklist()
        elif escolha == "3":
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == '__main__':
    main()
