#how to distribute work to workers-> the cpu cores assigned as resources to the different processes

import multiprocessing as mp
import os 

def cube(x):
    print (str(os.getpid())+" "+str(os.getppid())) #ID of processes + ID of the father
    return x**3


#MAIN
if __name__=="__main__":
    pool = mp.Pool(processes=4) #define 4 workers
    results = pool.map_async(cube,range(1,7)) #assign the work (function cube 7 times) to the workers in an async mode
    print(results)
    print(results.get(timeout=1))
    

#output = [p.get() for p in results]
#print(output)

#you will get 6 different process name that are running the cube processes from the same father (main)
#for every run you will get different processes: every time you launch the programm the pool will distribute differently the work to the workers, sometimes to all 4 workers, sometimes to only 2 etc...
