# todos os teste de coisas que eu aprendo ficam aqui
from datetime import datetime
import sys
import music_player
t = datetime.now()
h = t.hour
m = t.minute
s = t.second

while True:
    try:
        sys.stdout.write('\r{}:{}:{}'.format(h, m, s))
        sys.stdout.flush()
        h = int(datetime.now().hour)
        m = int(datetime.now().minute)
        s = int(datetime.now().second)
    except KeyboardInterrupt:
        print('\nRelógio desligado')
        break
    if h == 15 and m == 0:
        print('\nhora de lanchar')
        music_player.rtocar('pvz.mp3.mp3')
        break

