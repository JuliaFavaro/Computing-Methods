from loguru import logger

class Reading:
    """"Small container class representing a single voltage reading"""

    def __init__(self, timestamp, adc):
        self.timestamp=timestamp
        self.adc=adc

    def voltage(adc):
        '''function read lines in the file and converts 
        ADC counts to a physical voltage in V'''
        return 1.653*adc+ 0.456
    
    def __str__(self): #special method called to read the line
        return f"Reading at {self.timestamp} s: {self.adc} ADC counts ({self.voltage()}) V."
    

class VoltageData:
    """Simple interface to a set of voltage readings.
    To have a casual """

    def __init__(self,file_path):
        logger.info(f'Reading voltage data from {file_path}...')
        with open(file_path) as input_file:
            self._lines=input_file.readlines() #you should not mess with lines
        logger.info(f'Done, {len(self._lines)} values read.') #self._lines is a list, an iterable object
        self._line_iterator=iter(self._lines) #this built in function creates an iterator for an iterable object
        self.__index=0

    def _parse_line(self,line):
    '''Parse a single line from a text file and returns a Reading object.'''
    #not this method NEVER uses the self, meaning that can and it should be rewritten
        timestamp, adc=line.split() #all of these are strings
        timestamp=float(timestamp) #casting
        adc=int(adc)
        return Reading(timestamp,adc) #composition    

"""
#IF YOU REALLY WANT TO RESET AND CALL YOUR ITERATOR FOREVER. YOU SHOULD NOT USE IT THOUGH
    def reset(self):
        self._line_iterator=iter(self._lines)
"""

    def __iter__(self): #now this is an iterable Object, calls the iterator for the first time
        #you will call __iter__ the first time, and then you will pass to __next__
        #logger.debug(f'Calling {self.__class__.__name__}.__iter__()')
        return self

    def __next__(self): #when to the final element of the iterable, will StopIteration raise exception
        #logger.debug(f'Calling {self.__class__.__name__}.__next__()')
        return self._parse_line(next(self._line_iterator))

    """
    #Another way to see this implementation is:
    def __next__(self):
        if self.__index==len(self._lines):
            raise StopIteration
        reading=self._parse_line(self._lines[self.__index])
        self.__index=+1
        return reading
"""

if __name__='__main__':
    r=Reading(1., 120)  #single voltage reading
    for reading in VoltageData('voltage_data.txt'): #an istance of an iterable class that reads the entire file
        print(reading)
    v=VoltageData(file_path)