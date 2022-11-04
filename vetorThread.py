import threading
from threading import Thread
import time
import random

def par(vetor, name):
    threading.current_thread().name = name
    for i in vetor:
        if vetor[i]%2==0:
            print(f"{threading.current_thread().name} - {vetor[i]}")
    time.sleep(2)
   
def impar(vetor, name):
    threading.current_thread().name = name
    for i in vetor:
        if vetor[i]%2!=0:
            print(f"{threading.current_thread().name} - {vetor[i]}")
    time.sleep(2)

if __name__ == '__main__':    
    N = 15
    a = []

    print("Vetor original:")
    for i in range(N):
        a.append(random.randint(0,10))
    print(a)

    t = Thread(target=par,args=(a, "par",))
    t1 = Thread(target=impar,args=(a, "impar",))

    t.start()
    t1.start()

