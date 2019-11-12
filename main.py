
import argparse
from  Src.functions import *

def parse():
    parser= argparse.ArgumentParser()  
    parser.add_argument('f', help = 'Enter a date between 1997-2015', type = int)
    parser.add_argument('s', help = 'Enter a semester 1 or 2. Semester 1 is from January to June and semester 2 is from July to December', type = int)
    '''parser.add_argument('t', help = 'It will give you the maximun, minimun and average temperatures', type = str)'''
	
    
    return parser.parse_args()

def main():
    args=parse()
    print ('La fecha es {} y el semestre {}'.format(args.f, args.s))
    df =importCsv()
    print(df)
    filtered_df = filter(args.f, args.s,df)
    '''filter_temperatur= filter_temperature(args.t)'''
    print(filtered_df)
        


if __name__=='__main__':
	main() 