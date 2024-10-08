from dataclasses import dataclass
from loguru import logger

@dataclass #decorator
class Reading:
    """"Small container class representing a single voltage reading"""
    timestamp:float #i eliminated the constructor, this will input the attributes to the class
    adc:float

    def voltage(adc):
        '''function read lines in the file and converts 
        ADC counts to a physical voltage in V'''
        return 1.653*adc+ 0.456
    
    #i also eliminated the __str__ special method
    

class VoltageData:
    """Simple interface to a set of voltage readings."""

    def __init__(self,file_path):
        logger.info(f'Reading voltage data from {file_path}...')
        with open(file_path) as input_file:
            self._readings=[self._parse_line(line) for line in input_file.readlines()]
        logger.info(f'Done, {len(self._readings)} values read.')
        self._iterator=iter(self._readings) #this built in function creates an iterator for an iterable object

    def _parse_line(self,line):
    '''Parse a single line from a text file and returns a Reading object.'''
        timestamp, adc=line.split() #all of these are strings
        timestamp=float(timestamp) #casting
        adc=float(adc)
        return Reading(timestamp,adc) #composition    

    def __iter__(self): #now this is an iterable Object, calls the iterator for the first time
        return self

    def __next__(self): 
        return next(self._iterator) #built in function next
    
    def _getitem_(self,index):
        """Ïf you want access to a specific reading"""
        return self._readings[index]

if __name__='__main__':
    data=VoltageData('voltage_data.txt') #an istance of an iterable class that reads the entire file
    for reading in data:
        print(reading, reading.timestamp, reading.adc, reading.voltage()) #you can access to any element of the reading object
    
    print('Done')
    print(data[3]) #this interface works similarly to a list, which is an iterable object infact