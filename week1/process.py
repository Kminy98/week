from multiprocessing import Process
import os
# 코드로 스레드 만들기


# ----------동일한 작업을 하는 스레드 생성하기----------
def foo():
    print('child process', os.getpid())
    print('my parent is', os.getppid())

if __name__ == '__main__':
    print('parent process', os.getpid())
    #foo라는 프로세스를 만들거야? 실행해?
    child = Process(target=foo).start()
    child = Process(target=foo).start()
    child = Process(target=foo).start()

# 결과
# parent process 10380
# child process 50544
# my parent is 10380
# child process 52784
# my parent is 10380
# child process 36392
# my parent is 10380

# ----------다른 작업을 하는 스레드 생성하기----------
def bar():
    print('This is bar:', os.getpid())

def baz():
    print('This is baz:', os.getpid())
    
def qux():
    print('This is qux:', os.getpid())

if __name__ == '__main__': 
    child4 = Process(target=bar).start()  
    child5 = Process(target=baz).start() 
    child6 = Process(target=qux).start()

# 결과
# This is bar: 21444
# This is baz: 26616
# This is qux: 50564
