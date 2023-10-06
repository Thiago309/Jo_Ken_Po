itens = ('Opção INVALIDA escolha de (1~3) por favor.', 'Pedra.', 'Papel.', 'Tesoura.')

JG_1 = int(input("Jogador(1) por favor, escolha digitando (1~3) para selecionar uma das opções a seguir: (1-Pedra, 2-Papel, 3-Tesoura): "))
print("O Jogador 1 escolheu:{}".format(itens[JG_1]))
print("-=" * 70)

if (JG_1 == 1) or (JG_1 == 2) or (JG_1 == 3):  # O Jogo será executado somente se as opções desejadas de (1~3) forem selecionadas corretamente
    JG_2 = int(input("Jogador(2) por favor, escolha digitando (1~3) para selecionar uma das opções a seguir: (1-Pedra, 2-Papel, 3-Tesoura): "))
    print("O Jogador 2 escolheu:{}".format(itens[JG_2]))
    print("-=" * 70)

# -------------------------------CASO DA PEDRA-----------------------------------------------
if JG_1 == 1:  # Se o jogador 1 selecionar (Pedra).
    if JG_2 == 1:  # Caso Jogador 2 selecione tambem a mesma opção irá dar empata.
        print("Ambos jogadores EMPATARAM, tente novamente!")
    elif JG_2 == 2:  # Caso o jogador 2 escolha Papel, irá vencer pois Papel cobre pedra.
        print("Jogador 2 VENCEU esta partida, parabéns!")
        print("Mais sorte na próxima jogador 1...")
    elif JG_2 == 3:  # Caso o Jogador 2 escolha Tesoura, irá perder pois Pedra quebra tesoura
        print("Jogador 1 VENCEU esta partida, parabéns!")
        print("Mais sorte na próxima jogador 2...")
    else:  # Caso o jogador 2 não escolha a opção correta (1~5)
        print("Opção invalida Jogador 2, escolheU a opção novamente...")

# ---------------------------------CASO DO PAPEL---------------------------------------------
if JG_1 == 2:  # Se o jogador 1 selecionar (PAPEL).
    if JG_2 == 2:  # Caso Jogador 2 selecione tambem a mesma opção irá dar empata.
        print("Ambos jogadores EMPATARAM, tente novamente!")
    elif JG_2 == 1:  # Caso o jogador 2 escolha PEDRA, irá perder pois PAPEL vence.
        print("Jogador 1 VENCEU esta partida, parabéns!")
        print("Mais sorte na próxima jogador 2...")
    elif JG_2 == 3:  # Caso o Jogador 2 escolha TESOURA, irá vencer pois Tesoura corta papel
        print("Jogador 2 VENCEU esta partida, parabéns!")
        print("Mais sorte na próxima jogador 1...")
    else:  # Caso o jogador 2 não escolha a opção correta (1~5)
        print("Opção invalida Jogador 2, escolheU a opção novamente...")

# ---------------------------------CASO DA TESOURA-------------------------------------------
if JG_1 == 3:  # Se o jogador 1 selecionar (TESOURA).
    if JG_2 == 3:  # Caso Jogador 2 selecione tambem a mesma opção irá dar empata.
        print("Ambos jogadores EMPATARAM, tente novamente!")
    elif JG_2 == 1:  # Caso o jogador 2 escolha PEDRA, irá vencer pois Pedra quebra tesoura
        print("Jogador 2 VENCEU esta partida, parabéns!")
        print("Mais sorte na próxima jogador 1...")
    elif JG_2 == 2:  # Caso o Jogador 2 escolha PAPEL, irá perder pois Tesoura corta papel
        print("Jogador 1 VENCEU esta partida, parabéns!")
        print("Mais sorte na próxima jogador 2...")
    else:  # Caso o jogador 2 não escolha a opção correta (1~5)
        print("Opção invalida Jogador 2, escolheU a opção novamente...")