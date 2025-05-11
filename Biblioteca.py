"""
Menu:
1- Listar
2- Adicionar
3- Remover
4- Sair
"""
class Agenda:
    def _init_(self):
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
        print("Tarefa cadastrada com sucesso!")

    def removerTarefa(self):
        self.listarTarefas()
        posicao = int(input("Insira a posição da tarefa que deseja remover: "))

        if posicao != "" and posicao [0] in "123456789":
            j = int(posicao) - 1
            if j < len(self.tarefas):
                tarefaRemovida = self.tarefas.pop(j)
                print(f"Tarefa: {tarefaRemovida} removida com sucesso! ")

            else:
                print("Posição fora do alcance: ")

        else:
            print("Entrada Invalida! Insira um numero inteiro positivo")



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