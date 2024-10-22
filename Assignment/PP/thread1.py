import threading 
import os 

def task1(): 
	print("Task 1 assigned to thread: "+threading.current_thread().name) 
	print("ID of process running task 1: "+str(os.getpid())) 
def task2(): 
	print("Task 2 assigned to thread: "+threading.current_thread().name) 
	print("ID of process running task 2: "+str(os.getpid()))  #same id
#MAIN
if __name__=="__main__":
        # print ID of current process 
        print("ID of process running main program: "+str(os.getpid())) 
        # print name of main thread 
        print("Main thread name: "+threading.main_thread().name) 
        
        # creating threads 
        t1 = threading.Thread(target=task1, name='t1') 
        t2 = threading.Thread(target=task2, name='t2') 
        # starting threads 
        t1.start() 
        t2.start() 
        # wait until all threads finish 
        t1.join() 
        t2.join() 
        
#A thread is the minimum part of the code that can be executed. There might be more than one thread within a process. It is the smallest performing unit for the OS. 
#threads have the same ID (part of the same process). They are faster and have the same memory
#you can not kill a single thread but you need to kill the entire program

