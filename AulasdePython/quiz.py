from colorama import Fore, Style

perguntas = []


def criarPergunta(texto: str, certa: int, *alternativas: str):
    pergunta = {
        'texto': texto,
        'certa': certa,
        'alternativas': alternativas
    }

    perguntas.append(pergunta)


def iniciarQuiz():
    print(Fore.GREEN+"Iniciando quiz:"+Style.RESET_ALL)
    for index in range(0, len(perguntas)):
        print(Fore.YELLOW+"Pergunta número")


criarPergunta("3", 3, "1", "2", "3", "4")
criarPergunta("3", 3, "1", "2", "3", "4")
criarPergunta("3", 3, "1", "2", "3", "4")

iniciarQuiz()
