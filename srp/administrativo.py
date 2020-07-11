class Administrativo:
    def receberSalario(self, dia, colaborador):
        if dia == 31:
            print("Pagar colaborador %s no fim do mês" % colaborador.get_nome())