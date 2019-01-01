def clock():
    from datetime import datetime
    import sys
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
        except KeyboardInterrupt as e:
            break



