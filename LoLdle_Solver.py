# Created by: 龍ONE
# Date Created: December 1, 2022
# Date Edited: December 1, 2022
# Purpose: Help solve classic mode in LoLdle

import pandas as pd
import LoLdle_Solver_Helper


def main():
    ''' Main method for interacting with user input
        and providing optimal guess or solution for
        LoLdle classic mode. 
    '''
    # read champion data and covert to Champion object
    champions_data = pd.read_csv('./champions.csv').to_dict('index')
    champions_list = []
    
    #print(champions_data)



# run main method for program
if __name__ == '__main__':
    main()
