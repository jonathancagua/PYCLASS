#!/usr/bin/python3

from threading import Thread
from threading import Lock
import time

class Counter:

    #mutex = Lock()

    def __init__(self):
        self.counter=0

    def inc(self):
        #Counter.mutex.acquire()
        self.counter+=1  # 1) get valor 2) incremento valor 3) set valor
        #Counter.mutex.release()

    def get_counter(self):
        return self.counter


class MyThread (Thread):

    def __init__(self, name, counter):
        super().__init__()
        self.name = name
        self.counter = counter

    def run(self):
        print ("Comienza thread:"+self.name)
        for i in range(0,100000): #cuenta 100mil veces
            self.counter.inc()
        print ("Saliendo de:"+self.name)


#Creamos objeto contador, compartido entre threads    
counter_obj = Counter()

# Creamos nuevos threads
thread1 = MyThread("Thread-1", counter_obj)
thread2 = MyThread("Thread-2", counter_obj)

# Iniciamos threads y esperamos que terminen
thread1.start()
thread2.start()

print("Espero finalizacion...")
thread1.join()
thread2.join()
print ("Terminaron los threads.")
print("Counter:{}".format(counter_obj.get_counter()))

