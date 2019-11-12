import pandas as pd

"""year=[1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
semester=[1,2]"""

def importCsv():
    path="./Output/resultados1.csv"
    df=pd.read_csv(path)
    return df


def filter(year, semester, df):
    filter_Year=df[df["year"] == year]
    filter_Year_sem=filter_Year[filter_Year['semester']==semester]
    
    return filter_Year_sem

   ''' filter_Year_sem=filter_Year[filter_Year['semester']==semester]
    
    


def filter_temperature(temperature):
    filter_Year_sem_temp=filter_Year_sem['Max Temp','Mean Temp','Min Temp']==temperature
    return filter_Year_sem_temp'''