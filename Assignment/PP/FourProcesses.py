import multiprocessing as mp

# define a example function
def Hello(pos,name):
    msg="Hello "+name
    output.put((pos, msg)) #it doesn't print in the Process, but just fill in the result in the correct container

if __name__=="__main__":
    # Define an output queue
    output = mp.Queue() #container shared by the main and the process

    # Setup a list of processes that we want to run
    processes = [mp.Process(target=Hello, args=(x, "Gianluca")) for x in range(4)] #you can use iterators to define 4 different process of a function
	#args are the parameters needed for Hello function

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()
            
    # Get process results from the output queue
    results = [output.get() for p in processes] #you fill the results list from the Queue
            
    print(results)
    
#Every time you run this code, the position  number order changes. The order of what process finishes before changes for every run
#You cannot rely on the order for writing the dependency in an algorithm

"""
However, the final order in which the results are printed is determined by the order in which they are retrieved from the Queue.
Since the Queue preserves the order in which items were put, the results will always reflect the order of pos values 
as they were put into the queue by the Hello function.

In your code:

    You start four processes.

    Each process puts its result into the queue with a unique pos value.

    You retrieve the results from the queue in the same order the processes put them in, ensuring the printed result reflects this order.

    
"""