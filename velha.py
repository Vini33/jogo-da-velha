import time
velha = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ok = False

def validar_numero(pos):
    ok = False
    while ok == False:
        mode = str(input(pos))
        if mode.isnumeric():
            ok = True
            return int(mode)
        elif mode in " ":
            print('\033[1;31m voce deixou em branco \033[m')
        else:
            print('\033[1;31m voce digitou uma letra \033[m')


nome1 = input('digite seu nome jogador X:')
nome2 = input('digite seu nome jogador O:')
contador = 0

def terminar(ou):
    if ou == True:
        pass
    return ou

def ganhador(validor, nome, nome3, ok):
    #linha 0
    if validor[0][0] == 'X' and validor[0][1] == 'X' and validor[0][2] == 'X':
        print(f"o {nome} ganhou...")
        ok = True
        return ok
        #terminar(ok)
    #linha 1
    if validor[1][0] == 'X' and validor[1][1] == 'X' and validor[1][2] == 'X':
        print(f"o {nome} ganhou")
        ok = True
        return ok
    #linha 2
    if validor[2][0] == 'X' and validor[2][1] == 'X' and validor[2][2] == 'X':
        print(f"o {nome} ganhou")
        ok = True
        return ok
    #coluna 0
    if validor[0][0] == 'X' and validor[1][0] == 'X' and validor[2][0] == 'X':
        print(f"o {nome} ganhou")
    #coluna 1
    if validor[0][1] == 'X' and validor[1][1] == 'X' and validor[2][1] == 'X':
        print(f"o {nome} ganhou")
        ok = True
        return ok
    #coluna 2
    if validor[0][2] == 'X' and validor[1][2] == 'X' and validor[2][2] == 'X':
        print(f"o {nome} ganhou...")
        ok = True
        return ok
    #o que forma um x no jogo
    if validor[0][0] == 'X' and validor[1][1] == 'X' and validor[2][2] == 'X':
        print(f"o {nome} ganhou")
        ok = True
        return ok
    #o que forma um x no jogo
    if validor[0][2] == 'X' and validor[1][1] == 'X' and validor[2][0] == 'X':
        print(f"o {nome} ganhou")
        ok = True
        return ok

    #linha 0
    if validor[0][0] == 'O' and validor[0][1] == 'O' and validor[0][2] == 'O':
        print(f"o {nome3} ganhou...")
        ok = True
        return ok
    #linha 1
    if validor[1][0] == 'O' and validor[1][1] == 'O' and validor[1][2] == 'O':
        print(f"o {nome3} ganhou")
        ok = True
        return ok
    #linha 2
    if validor[2][0] == 'O' and validor[2][1] == 'O' and validor[2][2] == 'O':
        print(f"o {nome3} ganhou")
        ok = True
        return ok
    #coluna 0
    if validor[0][0] == 'O' and validor[1][0] == 'O' and validor[2][0] == 'O':
        print(f"o {nome3} ganhou")
        ok = True
        return ok
    #coluna 1
    if validor[0][1] == 'O' and validor[1][1] == 'O' and validor[2][1] == 'O':
        print(f"o {nome3} ganhou")
        ok = True
        return ok
    #coluna 2
    if validor[0][2] == 'O' and validor[1][2] == 'O' and validor[2][2] == 'O':
        print(f"o {nome3} ganhou...")
        ok = True
        return ok
    #o que forma um x no jogo
    if validor[0][0] == 'O' and validor[1][1] == 'O' and validor[2][2] == 'O':
        print(f"o {nome3} ganhou")
        ok = True
        return ok
    #o que forma um x no jogo
    if validor[0][2] == 'O' and validor[1][1] == 'O' and validor[2][0] == 'O':
        print(f"o {nome3} ganhou")
        ok = True
        return ok


print("coloque 'x' ou 'o', no lugar dos numeros")
#aqui e um determinado tempo pra ele espera, logo depois mostra as mensagem...
time.sleep(5)
print('\n' * 30)

#aqui pecorremos a matriz para mostra na tela...
for d in velha:
    for c in d:
        print(c, end=" ")
    print()

while ok == False:
   #aqui nos validamos a entrada de um numero, caso o usuario digite uma letra
    n = validar_numero(f'onde voce quer colocar X {nome1} :')
    for d in range(0, 3):
        for c in range(0, 3):
            if velha[d][c] == n:
                velha[d][c] = 'X'
                contador += 1
            print(velha[d][c], end=" ")
        print()
    #terminar o loop quando todos os numero sao preenchido...
    if contador == 9:
        ok = True
        print("\033[1;32m o jogo empatou \033[m")
        break
    #aqui termina o jogo
    if ganhador(velha, nome1, nome2, ok):
       break
    vol = validar_numero(f'onde voce quer colocar O {nome2}:')
    for d in range(0, 3):
        for c in range(0, 3):
            if velha[d][c] == vol:
                velha[d][c] = 'O'
                contador += 1
            print(velha[d][c], end=" ")
        print()
       #aqui termina o jogo
    if ganhador(velha, nome1, nome2, ok):
        break
