from colorama import Fore, Style, Back

perguntas = []


def criarPergunta(texto: str, certa: int, *alternativas: str):
    pergunta = {
        'texto': texto,
        'certa': certa,
        'alternativas': alternativas
    }

    perguntas.append(pergunta)


def perguntar(pergunta, numero):
    print(Fore.BLUE + "Pergunta número {}:".format(numero))

    print(Fore.WHITE + pergunta["texto"])

    for resp in range(0, len(pergunta["alternativas"])):
        print(Fore.YELLOW + "({}) - {}".format(resp +
              1, pergunta["alternativas"][resp]))

    try:
        resp = int(input(Fore.GREEN + "responda: "))
    except ValueError:
       return 'insira apenas números inteiros'

    print(Fore.WHITE + f"{resp} {pergunta['certa']}")

    if resp == pergunta["certa"]:
        return True
    else:
        return False


def iniciarQuiz():
    pontos = 0


    print(Fore.YELLOW+"Iniciando quiz:")

    for index in range(0, len(perguntas)):
        pergunta = perguntas[index]
        respondido = False

        while not respondido:
            resposta = perguntar(pergunta, index+1)
            
            if resposta == True:
                pontos += 1
                respondido = True

                print(Fore.GREEN + "Parabéns, acertou!")
                print(Fore.GREEN + f"Pontuação atual: {pontos} \n")

            elif resposta == False:
                respondido = True
                print(Fore.RED + "Pena, errou :(")
                print(Fore.RED + f"Pontuação atual: {pontos} \n")
            
            else:  
                print(Back.RED + Fore.BLACK + resposta + Back.RESET + "\n")

    print(Fore.CYAN+"\n Esse foi o quiz de hoje")
    print(Fore.CYAN+f"Pontuação total {pontos}")


criarPergunta("3 abalblalbabalb", 3, "1", "2", "3", "4")
criarPergunta("4 aablealbelebleblbealbleblb", 3, "1", "2", "3", "4")
criarPergunta("5 ablibliblbiblib", 3, "1", "2", "3", "4")

iniciarQuiz()
