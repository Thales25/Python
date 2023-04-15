
import hashlib

usuarios = {}
# tela de opções

opcao = input(' digite uma opções abaixo:\n para realizar cadastro digite (1)\n para realizar login digite (2)\n lista de usuarios cadastrados(3)\n --> ')

while opcao not in ['1','2','3']:
       opcao = input (" opção invalida! digite uma das opções abaixo:\n para realizar cadastro digite (1)\n para realizar login digite (2)\n --> ")
    

if opcao == '1':
    
    print("Seja bem vindo a tela de cadastro!\n Digite a baixo seu nome:")
    nome = input("-->")
    
    print(f"Perfeito {nome}, vamos agora criar uma senha. Digite a baixo sua senha:")
    senha = input("-->")
    
    usuarios[nome] = hashlib.md5(senha.encode()).hexdigest() 
    print("Cadastro realizado com sucesso!")
    
    

elif opcao == '2':
    print("Bem vindo! faça agora o seu login: ")
    login = input("Digite seu nome: ")
    senha = input ("Digite sua senha: ")
        
    if login in usuarios and usuarios[login] == hashlib.md5(senha.encode()).hexdigest():
      print ("login realizado com sucesso!")
      input("digite uma opção :")
elif opcao == '3':
    print("usuarios cadastrados: ")
    for usuario in usuarios:

        continue
