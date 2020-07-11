from permissoes import Permissoes

class Usuario(Permissoes):
    def logar_no_sistema(self):
        print("Utilizar as credenciais para acessar o sistema")
        super().verificar_permissao()