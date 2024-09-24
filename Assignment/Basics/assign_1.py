#Standard library modules
import argparse  #user-friendly command-line interfaces. The argparse module also automatically generates help and usage messages.
import string

#Third Party packages
from logoru import logger 
import matplotlib.pyplot as plt
import numpy as np

def count_characters(file_path,plot): #always section your code in multiple functions
        #This is a doc string. It gives away the documentation of the function.
    """Process one file and count the occurrences of each characters.

    Arguments
    ---------
    file_path: string
        Path to the input file
    --plot: boolean
    	If true, it will plot a hystogram of the occurences
    """
    counts={char:0 for char in string.ascii_lowercase} #dictionary, vectorized way

    with open(file_path) as input_file: #closes automatically the file in case of corruption and after loading the file
        data =input.file.read()
        logger.debug(f'Reading input data form {file_path}...')
        data=input_file.read()
    logger.debug(f'Done, {len(data)} characters found.}')
    logger.info('Counting characters...')
    for char in data.lower(): # so that the text is case insensitive 
        if char in counts:
            counts[char]+=1
    logger.info(f'Character counts: {counts}')

    num_characters=sum(counts.values()) #remember that this is the way to get to the numbers in a dict.
    for key, value in counts.items():
        counts[key]=value/num_characters
    logger.info(f'Character frequencies: {counts}') 
    if plot:
        logger.info('Starting the histogram...')
        plt.bar(unique, counts)
        plt.title('Letter frequency')
        plt.xlabel('Letters')
        plt.ylabel('Occurences')
        plt.show()

#Python module: you may want to execute from terminal or to import the module from terminal
#the following lines execute whatever you want from the module when called as the MAIN program
#any statement that gets executed must be in a function definition

if __name__=='_main_': #every modules have a __name__ member. There's only one main for each Python execution
    parser.ArgumentParser(description='Count the characters in a text file') #--help on terminal will print this
    parser.add_argument('file') #compulsory input
    parser.add_argument('--plot', action='store_true',  #it's an optional argument that plot, store_true means that it's by default always off unless you specify otherwise
                        help='Plot a bar chart of the character frequencies ')
    args=parser.parse_args()
    count_characters(args.file, args.plot)