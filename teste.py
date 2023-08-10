from rich.table import Table
from rich.console import Console

console = Console()
functions = Table(title='Comandos', title_style='bold red')
functions.add_column('Players revidados por usuários', style='cyan')
functions.add_column('Pesquisas sobre tags de jogadores')
functions.add_row('user id_do_usuário','tags tag1 tag2 tag3 etc...', style='cyan')
functions.add_row('\n-Exemplo: user 65733', '\n-Exemplo: tags Brazil Dribbler ', style='italic light_sky_blue3')


console.print(functions)
console.print('Para sair escreva "quit()" ', style='grey69',width=50)

command = ''
while command != 'quit()':
    command = input()
    aux = command.split(' ')
    if aux[0] == 'user':
        if len(aux) > 2:
            console.print('ERRO: COMANDO MAL FORMATADO :angry:', style='bold red')
        else:
            userId = int(aux[1])
            print(f'userId: {userId}')
    elif aux[0] == 'tags':
        tags = ','.join(aux[1:len(aux)])


    else:
        console.print('ERRO: COMANDO MAL FORMATADO :angry:', style='bold red')

    