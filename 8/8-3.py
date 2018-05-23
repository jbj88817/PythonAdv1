from threading import Event, Thread


def f(e):
    print 'f 0'
    e.wait()
    print 'f 1'


e = Event()
t = Thread(target=f, args=(e,))

t.start()
e.set()
e.clear()
