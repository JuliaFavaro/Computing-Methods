import multiprocessing 

def withdraw(balance):	 
        for x in range(10000): 
                balance.value = balance.value-1
def deposit(balance):	 
	for x in range(10000): 
		balance.value = balance.value + 1

def perform_transactions(): 
	# initial balance (in shared memory) 
	balance = multiprocessing.Value('i', 100) 
	# creating new processes 
	p1 = multiprocessing.Process(target=withdraw, args=(balance,)) 
	p2 = multiprocessing.Process(target=deposit, args=(balance,)) 
	# starting processes 
	p1.start() 
	p2.start() 
	# wait until processes are finished  (parallel)
	p1.join() 
	p2.join() 
	# print final balance 
	print("Final balance = {}".format(balance.value)) 

#MAIN
for x in range(10): 
    # perform same transaction process 10 times 
    perform_transactions() 

#every run they are accessing to a different balanced shared because they are always working with whatever the other process has done to the shared memory -> the result is randomic

# we need to ensure that two concurrent processes do not execute at the same time a particular program segment
