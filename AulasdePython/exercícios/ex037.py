import music_player
#-------------------C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndBarbra.mp3
music_player.tocar(r'C:\Users\MAXIMUS\Documents\biel\RhythmDoctorOffline\assets\sounds\sndOrientalDubstep.mp3')
#-----------------------------------------------------------------------------------------------------

num = int(input('digide um número inteiro:'))
print("""
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL""")

opcao = int(input('Sua opção:'))

if opcao == 1:
    print(num, bin(num)[2:])
elif opcao == 2:
    print(num, oct(num)[2:])
elif opcao == 3:
    print(num, hex(num)[2:])
#easter egg
elif opcao == 7070:
    print('se não deu certo 70 dnovo.')
#easter egg
else:
    print('isso não é escolha seu RACKER!')
