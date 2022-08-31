def title(msg):
    print('=' * 50)
    print(msg.center(50))
    print('=' * 50)


def subtitle():
    menu = dict()
    menu[1] = 'Proposta de Crédito [ $ ]'
    menu[2] = 'Cadastrar Usuário \t[ + ]'
    menu[3] = 'Remover Usuário \t[DEL]'
    menu[4] = 'Sair do Sistema \t[ ! ]'
    for k, v in menu.items():
        print(f'{k} - {v}')
    print('=' * 50)


def user_db():
    print('=' * 50)
    title('[=] BANCO DE DADOS'.center(50))


def submenu():
    print('=' * 50)
    print('[1] - Pessoa Física\n'
          '[2] - Pessoa Jurídica')
    print('=' * 50)


def error_code():
    print('[ERROR] - Digite um número válido.')


def Real(price, coin='R$'):     # Formata para Real BR.
    return f'{coin} {price:.2f}'.replace(".", ",")
