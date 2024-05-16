import os

def exibir_nome_do_programa():
    print("""""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝█████╗░░╚█████╗░  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗██╔══╝░░░╚═══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║███████╗██████╔╝  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

print("1. Cadrastrar restaurante")
print("2. Listrar restaurantes")
print("3. Ativar restaurante")
print("4. Sair\n")

opcao_escolhida = int(input("Escolha uma opção: "))
# opcao_escolhida = int(opcao_escolhida) 

def finalizar_app():
    os.system("cls")
    
    print("Finalizando o app")

if opcao_escolhida == 1:
   print("Cadastrar resutaurante")
elif opcao_escolhida == 2:
   print("Listar resutaurantes")
elif opcao_escolhida == 3:
   print("Ativar resutaurante")
else: 
    finalizar_app()
   
def main():
    exibir_nome_do_programa()

if __name__ == "__main__":
    main()

