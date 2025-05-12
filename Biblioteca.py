"""
Menu:
1- Listar
2- Adicionar
3- Remover
4- Sair
"""
class Agenda:
    def __init__(self):
        self.tarefas = []

    def listarTarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada!")

        else:
            print("Tarefas:")
            i = 1
            for tarefa in self.tarefas:
                print(f"{i}.{tarefa}")
                i += 1

    def adicionarTarefa(self):
        novaTarefa = input("Insira a tarefa: ")
        self.tarefas.append (novaTarefa)
        print("Tarefa cadastrada!")

    def removerTarefa(self):
        self.listarTarefas()
        try:
            posicao = int(input("Insira a posição da tarefa que deseja remover: "))
            if 1 <= posicao <= len(self.tarefas):
                tarefaRemovida = self.tarefas.pop(posicao - 1)
                print(f"Tarefa: '{tarefaRemovida}' removida!")
            else:
                print("Posição fora do alcance.")
        except ValueError:
            print("Entrada inválida! Insira um número inteiro.")

    def menu(self):
        while True:
            print("\n--- Menu da Agenda ---")
            print("1 - Adicionar tarefa")
            print("2 - Remover tarefa")
            print("3 - Listar tarefas")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionarTarefa()
            elif opcao == "2":
                self.removerTarefa()
            elif opcao == "3":
                self.listarTarefas()
            elif opcao == "4":
                print("Saindo da agenda...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")