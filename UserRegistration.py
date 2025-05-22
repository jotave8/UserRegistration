TAM_USUARIO = 100
qtd_usuario = 0
opcao: int
sair = 0

lista_usuarios = [None] * TAM_USUARIO

def menu_geral():
    print('╔═════════════════════════════════════════╗');
    print('║           Cadastro de Usuário           ║');
    print('║═════════════════════════════════════════║');
    print('║                Joao Victor              ║');
    print('╚═════════════════════════════════════════╝\n');
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Buscar')
    return int(input('Escolha: '))

def cadastrar_usuario(lista_usuarios, qtd_usuario):
    print('\nCadastrar Usuario')
    if qtd_usuario == TAM_USUARIO:
        print('Lista de usuarios cheia')
    else:
        usuario = {
            "nome": input('Informe o nome: ').upper(),
            "idade": int(input('Informe a idade: ')),
            "email": input('Infome o email: ').upper()
        }
        lista_usuarios[qtd_usuario] = usuario
        qtd_usuario += 1
        print('Usuário cadastrado com sucesso!\n')
    return qtd_usuario

def listar_usuarios (lista_usuarios, qtd_usuario):
    print('\nListar Usuario')
    if qtd_usuario == 0:
        print('Lista de usuarios vazia\n')
    else:
        for i in range(qtd_usuario):
            print(f'Nome: {lista_usuarios[i]["nome"]}  | Idade: {lista_usuarios[i]["idade"]}  | Email: {lista_usuarios[i]["email"]}')

while sair != 1:
    opcao = menu_geral()

    match opcao :
        case 0 :
            sair = 1
        case 1 :
            qtd_usuario = cadastrar_usuario(lista_usuarios, qtd_usuario)
        case 2 :
            listar_usuarios(lista_usuarios, qtd_usuario)