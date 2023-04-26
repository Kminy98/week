import threading
import os

# 코드로 스레드 만들기


# ----------동일한 작업을 하는 스레드 생성하기----------
def foo():
    print('process id', os.getpid())

if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

# 결과
# process id 11232
# process id 11232
# process id 11232

# ----------다른 작업을 하는 스레드 생성하기----------
def foo():
    print('This is foo', os.getpid())

def bar():
    print('This is bar', os.getpid()) 

def baz():
    print('This is baz', os.getpid())

if __name__ == '__main__':
    thread4 = threading.Thread(target=foo).start()  
    thread5 = threading.Thread(target=bar).start()  
    thread6 = threading.Thread(target=baz).start()

# 결과
# This is foo 11232
# This is bar 11232
# This is baz 11232