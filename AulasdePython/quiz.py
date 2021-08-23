perguntas = []

def criarPergunta(texto: str, certa: int, *alternativas: str):
    pergunta = {
        'texto': texto,
        'certa': certa,
        'alternativas': alternativas
    }
    
    perguntas.append(pergunta)


def iniciarQuiz():
    for pergunta in perguntas:

criarPergunta("3",3,"1","2","3","4")
criarPergunta("3",3,"1","2","3","4")
criarPergunta("3",3,"1","2","3","4")

iniciarQuiz()