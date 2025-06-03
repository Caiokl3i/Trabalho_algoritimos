'''
Processo de gest˜ao de eventos

Dever´a oferecer funcionalidades b´asicas como exibi¸c˜ao
da lista de eventos, listagem dos participantes por evento, busca por participantes a partir
de seu c´odigo, e a gera¸c˜ao de estat´ısticas ´uteis para os organizadores, como os participantes
mais ativos e os temas mais frequentes.
'''

import functions


opcao = functions.menu()

if opcao == 1:
    functions.listar_eventos()
elif opcao == 2:
    functions.lista_participantes()
elif opcao == 3:
    functions.buscar_participantes()
elif opcao == 0:
    print('saindo')
else:
    print('opção inválida')
