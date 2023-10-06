itens = [" ", "Pedra.", "Papel.", "Tesoura."]
flag1 = 0
JG_1 = ''
JG_2 = ''
opcao = ""
print("-=" * 70)

while opcao in "sS":
    while (flag1 != 1):
        JG_1 = int(input("Jogador(1) por favor, escolha digitando (1~3) para selecionar uma das opções a seguir: (1-Pedra, 2-Papel, 3-Tesoura): "))

        if (JG_1 == 1) or (JG_1 == 2) or (JG_1 == 3):
            print("O Jogador 1 escolheu: {}".format(itens[JG_1]))
            flag1 += 1
        else:
            print("Opção invalida por favor, tente novamente.")

    JG_2 = int(input("Jogador(2) por favor, escolha digitando (1~3) para selecionar uma das opções a seguir: (1-Pedra, 2-Papel, 3-Tesoura): "))
    while (flag1 != 2):
        if (JG_2 == 1) or (JG_2 == 2) or (JG_2 == 3):
            print("O Jogador 2 escolheu: {}".format(itens[JG_2]))
            flag1 += 1
        else:
            JG_2 = int(input("Opção invalida por favor, escolha digitando (1~3) para selecionar uma das opções a seguir: (1-Pedra, 2-Papel, 3-Tesoura): "))

    if (JG_1 == JG_2):
        print("-=" * 70)
        print("Empate !")
    elif (JG_1 == 1 and JG_2 == 3) or (JG_1 == 2 and JG_2 == 1) or (JG_1 == 3 and JG_2 == 2):
        print("-=" * 70)
        print("Jogador 1 VENCEU esta partida, parabéns!\nMais sorte na próxima jogador 2...")
    else:
        print("-=" * 70)
        print("Jogador 2 VENCEU esta partida, parabéns!\nMais sorte na próxima jogador 1...")

    JG_1 = ""
    JG_2 = ""
    flag1 = 0
    opcao = input("Deseja continuar jogando (s/n)?: ")