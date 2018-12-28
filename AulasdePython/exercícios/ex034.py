sal = float(input('Qual é o salário do funcionário? R$'))
mais_sal = sal / 100 * 10
menos_sal = sal / 100 * 15
if sal <= 1250.0:
    novo_sal = sal + menos_sal
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(sal, novo_sal))
else:
    novo_sal = sal + mais_sal
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(sal, novo_sal))
import music_player

music_player.ntocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\OrientalInsomniac.mp3')
