from threading import Thread
from time import sleep


class Hi(Thread):
    def run(self):
        for number in range(10):
            print('Hi')
            sleep(1)


class Hello(Thread):
    def run(self):
        for number in range(10):
            print('Hello')
            sleep(1)


if __name__ == '__main__':
    thread1 = Hi()
    thread2 = Hello()
    # start() method internally call run() method.
    thread1.start()
    sleep(0.4)
    thread2.start()
    # There are total 3 threads Thread1, Thread2 & Main Thread.
    # Main thread is waiting until thread1 & thread2 complete.
    thread1.join()
    thread2.join()
    sleep(0.4)
    # After completion of two thread main thread is print now.
    print('Bye')
