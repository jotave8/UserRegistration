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
    print('Cadastrar Usuario')
    usuario = {
        "nome": input('Informe o nome: ').upper(),
        "idade": int(input('Informe a idade: ')),
        "email": input('Infome o email: ').upper()
    }

    lista_usuarios[qtd_usuario] = usuario
    qtd_usuario += 1
    print('Usuário cadastrado com sucesso!')


while sair != 1:
    opcao = menu_geral()

    match opcao :
        case 0 :
            sair = 1
        case 1 :
            sair = 0