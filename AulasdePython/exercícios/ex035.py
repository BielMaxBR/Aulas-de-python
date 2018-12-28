from music_player import ntocar
v1 = float(input('primeiro segmento: '))
v2 = float(input('segundo segmento: '))
v3 = float(input('terceiro segmento: '))

if v3 > v2 and v3 > v1:
    if v1 + v2 > v3:
        print('dá pra fazer um triângulo :)')
        ntocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndOrientalDubstep.mp3')
    else:
        print('não dá pra fazer um triângulo :(')
        ntocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndIntimate.mp3')
    """botão de parar"""
    parar = input('escreva algo pra parar')
    if parar == str:
        import sys

        sys.exit()

if v2 > v1 and v2 > v3:
    if v3 + v1 > v2:
        print('dá pra fazer um triângulo :)')
        ntocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndOrientalDubstep.mp3')
    else:
        print('não dá pra fazer um triângulo :(')
        ntocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndIntimate.mp3')
    """botão de parar"""
    parar = input('escreva algo pra parar')
    if parar == str:
        import sys

        sys.exit()

if v1 > v3 and v1 > v2:
    if v3 + v2 > v1:
        print('dá pra fazer um triângulo :)')
        ntocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndOrientalDubstep.mp3')
    else:
        print('não dá pra fazer um triângulo :(')
        ntocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndIntimate.mp3')
    """botão de parar"""
    parar = input('escreva algo pra parar')
    if parar == str:
        import sys

        sys.exit()
