# classe com alto acomplamento fora do princípio SRP
from colaborador import Colaborador

pedro = Colaborador("Pedro")
for dia in range(29, 32):
    print("************************* DIA %s ******************************" % dia)
    pedro.trabalhar()
    pedro.receberSalario(dia)
    print("************************ FIM DIA %s ****************************\n" % dia)


# classe com baixo acomplamento seguindo o princípio SRP
from colaborador_refatorado import ColaboradorRefatorado
from usuario import Usuario
from administrativo import Administrativo

pedro = ColaboradorRefatorado("Pedro")
administrativo = Administrativo()
for dia in range(29, 32):
    print("************************* DIA %s ******************************" % dia)
    pedro.trabalhar()
    administrativo.receberSalario(dia, pedro)
    print("************************ FIM DIA %s ****************************\n" % dia)

