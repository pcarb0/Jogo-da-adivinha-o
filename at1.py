class Jogo():
    __resp = 64
    __cartoes = [
        '''
        01 03 05 07 09 11 13 15
        17 19 21 23 25 27 29 31
        33 35 37 39 41 43 45 47
        49 51 53 55 57 59 61 63
        ''',
        '''
        01 02 05 06 09 10 13 14
        17 18 21 22 25 26 29 30
        33 34 37 38 41 42 45 46
        49 50 53 54 57 58 61 62
        ''',
        '''
        01 02 03 04 09 10 11 12
        17 18 19 20 25 26 27 28
        33 34 35 36 41 42 43 44
        49 50 51 52 57 58 59 60
        ''',
        '''
        01 02 03 04 05 06 07 08
        17 18 19 20 21 22 23 24
        33 34 35 36 37 38 39 40
        49 50 51 52 53 54 55 56
        ''',
        ''' 
        01 02 03 04 05 06 07 08
        09 10 11 12 13 14 15 16
        33 34 35 36 37 38 39 40
        41 42 43 44 45 46 47 48
        ''',
        '''
        01 02 03 04 05 06 07 08
        09 10 11 12 13 14 15 16
        17 18 19 20 21 22 23 24
        25 26 27 28 29 30 31 32
        '''
    ]
    def apresentar():
        print("Jogo dos cartões:")
        print("")
        print("Escolha um número de 1 a 64")
        print("Vamos mostrar carõtoes de números á voce")
        print("e vc tera que dizer se o numero que vc")
        print("escolheu está ou não no cartão")
        print("")
        print("vamos começar!!!")
        print("")

    def mostrar():
        cont = -1
        for card in Jogo.__cartoes:
            print(card)
            while True:
                try:
                    re = input("O seu número está ai?[S/n]: ")
                    print("")
                    if re.upper() != "S" and re.upper() != "N":
                        raise TypeError
                    break
                except:
                    print("Digite algo válido!!!")
                    print("")
                finally:
                    cont+=1
                    if re.upper() == "S": 
                        Jogo.__resp -= 2**cont

    def final():
        print("Deixa eu adivinhar...")
        print("o número que você pensou foi o %i"%Jogo.__resp)
        print("adivinhei não é?")
        print("HAHHAHAHAHAHAHAH")

    def __init__(self):
        Jogo.apresentar()
        Jogo.mostrar()
        Jogo.final()

Jogo()
