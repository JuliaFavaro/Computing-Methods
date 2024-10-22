import multiprocessing as mp
import time
import os

def doingstuff(x):
    print ("Process: "+str(x)+" "+str(os.getpid()))
    time.sleep(1) #wait for 1 second between each print

if __name__=="__main__":
    start=time.time()
    pool = mp.Pool(processes=4)
    results = pool.map(doingstuff,range(1,10)) #sync mode
    end=time.time()
    print("elapsed time: "+str(end-start)) #nota bene, elapsed time è meno di 10 secondi, perché sono eseguiti parallelamente
    #print(results.get())
    
    # It will print first the first 4 processes, then the next 4, then the last one. 
    # Note i processi sono diversi, ma sono sempre gli stessi lavori che si redistribuiscono il loro lavoro.
    # This is because the 4 processes can be launch simultaneously and only when all of them have finished
    # the resources are available for the next quaturple.  The order in the quartuple is not fixed
