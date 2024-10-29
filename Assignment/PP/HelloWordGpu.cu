#include <cuda.h>
#include <stdio.h>

__global__ void mykernel(void) { //this will be executed in the GPU, DEVICE
  printf("Hello World from GPU! (block: %d thread: %d)\n",blockIdx.x,threadIdx.x); //built in variables of the Cuda programming
}

int main(void) { //this will be executed in the PC, HOST
  mykernel <<<3,4>>>(); //launch KERNEL (with the number of blocks and threads we want to use. The numbering starts from 0 up to n-1
  cudaDeviceSynchronize(); //Kernel is asynchronous by default. You are asking to wait for the results of the kernel before moving to the next line
  printf("Hello World from Host!\n");
  return 0;
}
// it will show on the screen the execution in parallel by different threads in different blocks. The order of printing is different in every run (like in normal parallel programming) 
//you cannot assume to use the results from one threads to be entry data for another threads because you will never know the order of execution
// if you comment the cudaDEviceSynchronize you will only see on screen the "Hello world from host" line
