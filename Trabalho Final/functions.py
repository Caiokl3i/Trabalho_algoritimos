import eventos
import participantes


def exibir_menu(titulo):
    print(f'=' * 25 + " " + titulo.upper() + " " + '=' * 25)

def menu():
    while True:
        exibir_menu('menu')
        print("1 - Ver eventos")
        print("2 - Lista de participantes por evento")
        print("3 - Buscar participante")
        print("0 - Sair")
        print()

        opcao = int(input(": "))

        if opcao == 1:
            listar_eventos()
        elif opcao == 2:
            lista_participantes()
            break
        elif opcao == 3:
            buscar_participantes()
            break
        elif opcao == 0:
            print('saindo')
            break
        else:
            print('opção inválida')
            print()

def listar_eventos():
    while True:    
        exibir_menu('evento')
        for evento in (eventos.list_events):
            print(f"{evento['nome']}")
        print()
        print()
        exibir_menu('escolha')
        print('1 - Ver participantes através do evento')
        print('0 - Voltar')
        print()
        print()
        opcao = int(input(''))
        print()
        print()
        
        if opcao == 1:
            lista_participantes()
            break
        elif opcao == 0: 
            break
        else:
            print('Opção inválida')

def lista_participantes():
    while True:
        exibir_menu('eventos')
        for i, evento in enumerate(eventos.list_events):
            print(f"{i + 1} - {evento['nome']}")
        print()
        print()
        event_chosen = int(input("Escolha qual é o numero do evento para listar os participantes (somente numeros): "))
        print()
        print()
        print('Participantes do evento:')
        print()
        
        for i, evento in enumerate(eventos.list_events):
            if event_chosen == i:
                for participantes in evento['participantes_event']:
                    print(participantes['nome'])
                    
        print()
        print()
        exibir_menu('escolha')
        print('1 - Listar participantes de outros eventos')
        print('0 - Voltar')
        print()
        print()
        opcao = int(input(''))
        print()
        print()
        if opcao == 1:
            lista_participantes()
        elif opcao == 0: 
            break
        else:
            print('Opção inválida')


    print()

def buscar_participantes():
    exibir_menu('codigo do particpante')
    print("Insira o codigo do participante para ver os dados (somente numeros)")
    print()
    
    cod_participante = int(input(": "))
    cod_participante = 'P' + str(cod_participante)

    for i, item in enumerate(participantes.list_participantes):
        if cod_participante == item['cod']:
            print(participantes.list_participantes[i])
    print()