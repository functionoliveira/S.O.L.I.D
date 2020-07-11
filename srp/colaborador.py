import random 

class Colaborador:

    def __init__(self, nome):
        self.nome = nome

    def verificar_permissao(self):
        print("Verificar as permissões do usuário atual")

    def logar_no_sistema(self):
        print("Utilizar as credenciais para acessar o sistema")

    def trabalhar(self):
        print("Executar tarefa administrativa")
        print("Ir até a máquina e pegar um café")
        print("Sentar em frente ao seu computador")
        self.logar_no_sistema()
        self.verificar_permissao()
        print("Verificar sua lista de emails")
        print("Responder email")
        print("Olhar lista de tarefas")
        tarefas =  [
            "Ajustar ponto", 
            "Liberar acesso",
            "Gerar planilha",
            "Ajustar indicadores",
            "Gerar gráfico",
            "Imprimir relatório" 
        ]
        print("Escolher uma tarefa da lista: \n- %s" % "\n- ".join(tarefas))
        tarefa_escolhida = tarefas[random.randint(0, 5)]
        print("Executar a tarefa %s" % tarefa_escolhida)

    def receberSalario(self, dia):
        if dia == 31:
            print("Receber pagamento no fim do mês")