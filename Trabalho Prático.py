# Trabalho Prático de Estrutura de Dados em Python
# Vence 2 de dezembro de 2024 às 23:59
# Instruções
# Objetivo do Trabalho
# O objetivo deste trabalho é praticar os conceitos básicos de Estruturas de Dados, como listas, no desenvolvimento de um sistema simples de gerenciamento de tarefas. Esse sistema deve organizar, exibir e manipular tarefas de um usuário com base em prioridades e estados (pendente ou concluída).

# Descrição do Cenário
# Você foi contratado para desenvolver um sistema que gerencia uma lista de tarefas pessoais. O sistema deve permitir ao usuário adicionar, remover e organizar tarefas, bem como realizar algumas operações, como listar tarefas pendentes e concluídas.

# Funcionalidades principais:

# Adicionar tarefas à lista.
# Marcar tarefas como concluídas.
# Remover tarefas da lista.
# Listar todas as tarefas separadas por estado (pendente ou concluída).
# Pesquisar tarefas pelo nome.
# Dicas para o Desenvolvimento
# Estruturas a serem usadas:

# Listas:
# Use uma lista para armazenar as tarefas.
# Cada tarefa será representada como uma string, e outra lista pode armazenar o estado das tarefas (pendente ou concluída).
# Funcionalidades sugeridas:

# Adicionar tarefa: Insira o nome de uma tarefa na lista de tarefas.
# Marcar como concluída: Atualize o estado da tarefa correspondente.
# Remover tarefa: Remova a tarefa da lista.
# Listar tarefas: Exiba todas as tarefas, indicando o estado (pendente ou concluída).
# Pesquisar tarefa: Verifique se uma tarefa existe na lista e exiba detalhes.
# Estrutura de armazenamento:

# Use duas listas paralelas:
# Uma para os nomes das tarefas.
# Outra para o estado de cada tarefa (pendente ou concluída).

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        self.estados = []
        
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        self.estados.append("pendente")
        print(f'Tarefa adicionada: "{tarefa}"')
        
    def marcar_concluida(self, tarefa):
        if tarefa in self.tarefas:
            index = self.tarefas.index(tarefa)
            self.estados[index] = "concluída"
            print(f'Tarefa "{tarefa}" marcada como concluída')
        else:
            print(f'Tarefa "{tarefa}" não encontrada')
            
    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            index = self.tarefas.index(tarefa)
            self.tarefas.pop(index)
            self.estados.pop(index)
            print(f'Tarefa "{tarefa}" removida')
        else:
            print(f'Tarefa "{tarefa}" não encontrada')
            
    def listar_tarefas(self):
        print("\nTarefas pendentes:")
        for i in range(len(self.tarefas)):
            if self.estados[i] == "pendente":
                print(f'- {self.tarefas[i]}')
                
        print("\nTarefas concluídas:")
        for i in range(len(self.tarefas)):
            if self.estados[i] == "concluída":
                print(f'- {self.tarefas[i]}')
                
    def pesquisar_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            index = self.tarefas.index(tarefa)
            estado = self.estados[index]
            print(f'Tarefa "{tarefa}" encontrada - Estado: {estado}')
        else:
            print(f'Tarefa "{tarefa}" não encontrada')

def main():
    gerenciador = GerenciadorDeTarefas()
    
    while True:
        print("\nGerenciador de Tarefas")
        print("1 - Adicionar tarefa")
        print("2 - Marcar tarefa como concluída")
        print("3 - Remover tarefa")
        print("4 - Listar tarefas")
        print("5 - Pesquisar tarefa")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            gerenciador.adicionar_tarefa(tarefa)
        elif opcao == "2":
            tarefa = input("Digite o nome da tarefa a ser marcada como concluída: ")
            gerenciador.marcar_concluida(tarefa)
        elif opcao == "3":
            tarefa = input("Digite o nome da tarefa a ser removida: ")
            gerenciador.remover_tarefa(tarefa)
        elif opcao == "4":
            gerenciador.listar_tarefas()
        elif opcao == "5":
            tarefa = input("Digite o nome da tarefa a ser pesquisada: ")
            gerenciador.pesquisar_tarefa(tarefa)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()