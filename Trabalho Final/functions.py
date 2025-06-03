import eventos
import participantes

def menu():
    print("====================== MENU INICIAL ======================")
    print("1 - Ver eventos")
    print("2 - Lista de participantes por evento")
    print("3 - Buscar participante")
    print("0 - Sair")
    print()
    return int(input(": "))


def listar_eventos():
    print("====================== EVENTOS ======================")
    for i, evento in enumerate(eventos.list_events):
        print(f"{i + 1} - {evento['nome']}")


def lista_participantes():
    print("====================== EVENTOS ======================")
    for i, evento in enumerate(eventos.list_events):
        print(f"{i + 1} - {evento['nome']}")
    print()
    event_chosen = int(input("Escolha qual é o numero do evento para listar os participantes (somente numeros): "))
    
    for i, evento in enumerate(eventos.list_events):
        if event_chosen == i:
            for participantes in evento['participantes_event']:
                print(participantes['nome'])

def buscar_participantes():
    print("Insira o codigo do participante para ver os dados (somente numeros)")
    print()
    
    cod_participante = int(input(": "))
    cod_participante = 'P' + str(cod_participante)

    for i, item in enumerate(participantes.list_participantes):
        if cod_participante == item['cod']:
            print(participantes.list_participantes[i])