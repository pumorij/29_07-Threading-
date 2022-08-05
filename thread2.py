from threading import *
def f(n):
    for x in range(n):
        print(x)

t1=Thread(target=f,args=[5],name='thread1')
t1.start()