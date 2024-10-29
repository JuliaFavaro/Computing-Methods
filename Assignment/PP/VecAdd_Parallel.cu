#include <stdio.h>

#define N 1048576
#define THREADS_PER_BLOCK 128

void RandomVector(int *a, int nn){ //the kernel should be adapted with an index to an architecture where the total number of threads is equal to the number of vectors you are actually summing
  for (int i=0;i<nn;i++) {
    a[i]=rand()%100+1; 
  }
}

//kernel
__global__ void VecAddGpu(int *a, int *b, int *c){
  int index = threadIdx.x + blockIdx.x*blockDim.x;
  c[index] = a[index]+b[index];
}

int main(void) {
  int *h_a, *h_b, *h_c;
  int *d_a, *d_b, *d_c;
  int size = N*sizeof(int);

  float time;
  cudaEvent_t start,stop;
  cudaEventCreate(&start);
  cudaEventCreate(&stop);

  //Alloc in Host (and filling)
  h_a = (int *)malloc(size); //you should always starts pointers in host with a h_name
  h_b = (int *)malloc(size);
  h_c = (int *)malloc(size); // where you want results
  RandomVector(h_a,N);
  RandomVector(h_b,N);

  //Alloc in Device
  cudaMalloc((void **)&d_a, size); //the pointers are defined in a different space than the memory of the host, d_name
  cudaMalloc((void **)&d_b, size);
  cudaMalloc((void **)&d_c, size);

  //Copy input vectors form host to device
  cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

  //start time
  cudaEventRecord(start);

  //Launch Kernel  on GPU
  VecAddGpu<<<N/THREADS_PER_BLOCK,THREADS_PER_BLOCK>>>(d_a,d_b,d_c); // if you want to optimize you need to ask for the minumum number of blocks necessary 
  cudaDeviceSynchronize();

  //stop time
  cudaEventRecord(stop);
  cudaEventSynchronize(stop);
  cudaEventElapsedTime(&time, start, stop);

  cudaError_t KernelError=cudaGetLastError(); // you should check for errors
  printf("Error %s\n",cudaGetErrorString(KernelError));

  //Copy back the results
  cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost); //opposite direction

  //Print Result
  //  for(int i=0;i<N;i++){
  //  printf ("%d) h_a:%d h_b:%d h_c:%d\n",i,h_a[i],h_b[i],h_c[i]);
  //}

  //print time
  printf("Time: %3.5f ms\n",time);

  //Cleanup. always necessary for dynamical memory
  free(h_a);
  free(h_b);
  free(h_c);
  cudaFree(d_a);
  cudaFree(d_b);
  cudaFree(d_c);

  return(0);
}

//if you execute N blocks with 1 thread : it will take way more than time the serial programm! Only 2 blocks can be executed at the same time: you are basically only executing 2 threads at a time
//if you execute 1 block with N threads: it will take way less time (a factor of 1000)!! You can only go up to 1024 with our GPU MODEL otherways you are taking more resources than available
// this is why you should know the caracteristics of your videocard for maximum explotation-> you should actually check if the division is an integer I guess
