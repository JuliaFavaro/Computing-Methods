#The argparse module makes it easy to write user-friendly command-line interfaces. The argparse module also automatically generates help and usage messages.
import argparse
import time 

from loguru import logger #write messages about events happening in your code.
import numpy as np
from unidecode import unidecode
import matplotlib.pyplot as plt

#if you write from terminal python wordstats.py --help you get the help documentation that you have written here
parser=argparse.ArgumentParser(prog='wordcount',description='Count the letter frequency in a text')
parser.add_argument('in_file') #compulsory input
parser.add_argument('--plot', action='store_true',  #it's an optional argument that plot, store_true means that it's by default always off unless you specify otherwise
                    help='Plot a bar chart of the character frequencies ')

def letterFrequency(file_path,plot):
    #This is a doc string. It gives away the documentation of the function.
    """Process one file and count the occurrences of each characters.

    Arguments
    ---------
    file_path: string
        Path to the input file
    --plot: boolean
    	If true, it will plot a hystogram of the occurences
    """
    logger.info(f'Opening input file {file_path}...')#this is the correct string formation when you need to print also a variable
    with open(file_path) as input_file:
        data=input_file.read()
        data=unidecode(data) #it clears the file from any characters that Python doesn't support
        
    start_time=time.time()
    alpha_char= list(filter(str.isalpha, data.lower())) #creates a list of all alphabetical characters (CASE INSENSITIVE)
    unique, counts = np.unique(np.array(alpha_char), return_counts=True) #returns unique values occured and the frequencies
    all_freq = dict(zip(unique, counts/len(alpha_char)))
    logger.info('Printing the relative frequence of each letter of the alphabet')
    print(all_freq)
    
    if plot:
        logger.info('Starting the histogram...')
        plt.bar(unique, counts)
        plt.title('Letter frequency')
        plt.xlabel('Letters')
        plt.ylabel('Occurences')
        plt.show()
        
    elapsed_time=time.time()-start_time
    print(f'Total elapsed time: {elapsed_time} seconds')
    logger.info('Done')

#Python module: you may want to execute from terminal or to import the module from terminal
#the following lines execute whatever you want from the module when called as the MAIN program
#any statement that gets executed must be in a function definition

if __name__=='__main__':
    args=parser.parse_args() 
    letterFrequency(args.in_file, args.plot)
