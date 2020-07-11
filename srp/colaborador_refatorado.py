import random
from usuario import Usuario

class ColaboradorRefatorado(Usuario):
    
    def __init__(self, nome):
        self._nome = nome
    
    def get_nome(self):
        return self._nome
    def set_nome(self, new_nome):
        self._nome = novo_nome

    def trabalhar(self):
        self.pegar_cafe()
        self.sentar_na_em_frente_ao_computador()
        super().logar_no_sistema()
        self.olhar_email()
        # uma probabilidade de haver ou não email
        if random.randint(1, 10) > 5:
            self.responder_email()

        lista_de_tarefas = self.olhar_lista_de_tarefas()
        tarefa_selecionada = self.escolher_tarefa(lista_de_tarefas)
        self.executar_tarefa(tarefa_selecionada)

    def pegar_cafe(self):
        print("Ir até a máquina e pegar um café")
    
    def sentar_na_em_frente_ao_computador(self):
        print("Sentar em frente ao seu computador")

    def olhar_email(self):
        print("Verificar sua lista de emails")

    def responder_email(self):
        print("Responder email")

    def olhar_lista_de_tarefas(self):
        print("Olhar lista de tarefas")
        return [
            "Ajustar ponto", 
            "Liberar acesso",
            "Gerar planilha",
            "Ajustar indicadores",
            "Gerar gráfico",
            "Imprimir relatório" 
        ]

    def escolher_tarefa(self, lista_de_tarefas):
        print("Escolher uma tarefa da lista: \n- %s" % "\n- ".join(lista_de_tarefas))
        tarefa_escolhida = random.randint(0, 5)
        return lista_de_tarefas[tarefa_escolhida]

    def executar_tarefa(self, tarefa):
        print("Executar a tarefa %s" % tarefa)
