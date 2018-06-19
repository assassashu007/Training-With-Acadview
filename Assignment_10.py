print("Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.\n")


import threading
import time

t = threading.Thread()
t.start()
print(threading.currentThread().getName())
time.sleep(5)
print("MESSAGE DISPLAYED.........")







print("\n\nQ2. Make a thread that prints numbers from 1-10, waits for 1 sec between.\n")

import threading
import time

class mythread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("\nThread Starting.........")
        i=1
        while i<=10:
            print(i)
            time.sleep(1)
            i+=1
        print("\nThread Ended...........")

t = mythread()
t.run()









print("\n\nQ3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.")
print("Delay goes like 2sec-4sec-6sec-8sec-10sec\n")

import threading
import time

class mythread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Thread starting....")


threads = ['1', '2', '3', '4', '5']
i = 1
for t in threads:
    t = mythread()
    t.run()
    time.sleep(2)
    print(2*i)
    i=i+1
    print("Thread Ending........")











print("\n\nQ4. Call factorial function using thread.\n")

import threading
import math

class f(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        global result
        temp = math.factorial(self.num)
        print(str(self.name) + " calculates " + str(self.num) + " factorial is : " + str(temp))
        result += temp

result = 0
threads = []

def test():
    for i in range(1,6):
        t = f(i)
        threads.append(t)
    for i in range(5):
        threads[i].start()
    for i in range(5):
        threads[i].join()

print("Calling Factorial 1 to 5 :\n")
if __name__ == '__main__':
    test()