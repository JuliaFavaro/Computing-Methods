from dataclasses import dataclass

from loguru import logger
import numpy as np
import matplotlib.pyplot as plt

@dataclass #decorator

class Reading:
    """"Small container class representing a single voltage reading"""
    timestamp:float #i eliminated the constructor, this will input the attributes to the class
    adc:float
    
    _CONVERSION_SLOPE=1.653 
    _CONVERSION_OFFSET=0.456
    
    @staticmethod
    def voltage(adc):
        '''function read lines in the file and converts 
        ADC counts to a physical voltage in V'''
        return Reading._CONVERSION_SLOPE*adc+ Reading._CONVERSION_OFFSET
    
    #i also eliminated the __str__ special method
    

class VoltageData:
    """Simple interface to a set of voltage readings."""

    def __init__(self,timestamps, adcs): #self is refering to the specific istance of a class
        logger.info(f'Initializing {self.__class__.__name__} from arrays...')
        #zip allows you to iterate over several iterables in parallel producing tuple
        print(timestamps, adcs)
        self._readings=[Reading(timestamp, adc) for (timestamp, adc) in zip(timestampds, adcs)] 
        logger.info(f'Done, {len(self._readings)} values read.')
        self._iterator=iter(self._readings) #this built in function creates an iterator for an iterable object

    @classmethod #it gives out also a reference to the class type
    #remember you can't have more than 1 function named __init__
    def from_file(cls, file_path): #cls stands for class type,
        '''Initialize with using a file and without changing the constructor of this class'''
        logger.info(f'Reading voltage data from {file_path}...')
        timestamps=[]
        adcs=[]
        with open(file_path) as input_file:
            for line in input_file.readlines():
                timestamp, adc=cls._parse_line(line)
                timestamps.append(timestamp)
                adcs.append(adc)
        return cls(timestamps, adcs)
    
    @staticmethod
    #i can now use this function even without using an instance of the VoltageData class
    def _parse_line(self,line):
    '''Parse a single line from a text file and returns a Reading object.'''
        timestamp, adc=line.split() #all of these are strings
        timestamp=float(timestamp) #casting
        adc=float(adc)
        return timestamps, adcs
        #return Reading(timestamp,adc) #composition    

    def __iter__(self): #now this is an iterable Object, calls the iterator for the first time
        return self

    def __next__(self): 
        return next(self._iterator) #built in function next
    
    def _getitem_(self,index):
        """Ïf you want access to a specific reading"""
        return self._readings[index]

if __name__='__main__':
    



    t=np.linspace(1.,10.,10)
    a=np.full(t.shape,127)
    data1=VoltageData.from_arrays(t,a)
    for reading in data1:
        print(reading, reading.timestamp, reading.adc, reading.voltage()) #you can access to any element of the reading object

    print('Done')
    print(data1[3]) #this interface works similarly to a list, which is an iterable object infact

    #with staticmethod you can also do this
    print(VoltageData._parse_line('1., 127.'))

    data2=VoltageData.from_file('voltage_data.txt') #an istance of an iterable class that reads the entire file
    for reading in data2:
        print(reading, reading.timestamp, reading.adc, reading.voltage()) #you can access to any element of the reading object