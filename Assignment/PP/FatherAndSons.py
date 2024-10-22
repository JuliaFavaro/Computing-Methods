from multiprocessing import Process
import os

#check: remember that if you write on the terminal ps-> you will get all the process that are playing at the same time 
#emacs: lancia processi che vanno in background
def f0(name):
    print()
    print("-----> function "+name)
    print ("I am still the main process with ID "#it gives away what process he is running
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))  #the father of the main is the Bash, terminal

def f1(name):
    print()
    print("-----> function "+name)
    print ("I am the first sub-process with ID "
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))
    f2('two') #different IDs identify different programs, f2 is called in the process f1 so they will have the same ID number


def f2(name):
    print()
    print("-----> function "+name)
    print ("I am still the first sub-process with ID "
           +str(os.getpid())+" my father is ID:"+str(os.getppid())) #father will always be the father of f1: the bash terminal
    print("This is the end!")

#MAIN
if __name__=="__main__":
    print ("I am the main process with ID: "+str(os.getpid()))
    f0('zero') #the function defined in the same program
    p = Process(target=f1, args=('one',)) #process where f1 is executed with ID 'one'
    p.start()
    p.join()
