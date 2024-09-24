from multiprocessing improt Process

def f(name):
	print('Hello '+ name)
	
#MAIN
if __name__="__main__":
	p=Process(target=f,args=('World',))
	p.start()
	#other stuffs
	p.join() #wait until the end of the process
