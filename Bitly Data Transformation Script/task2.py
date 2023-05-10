import argparse
import json
import pandas as pd
import time
from pandas import DataFrame, Series
import os
import datetime

bt=time.time()
 
parser = argparse.ArgumentParser(description = 'task2 :converting jason to csv' )

parser.add_argument("path", help = "Enter json flle path you want to convert")
parser.add_argument("-u", action="store_true", dest="unix", default=False, help="WITH unix format")
args = parser.parse_args()

directory = args.path

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if f.endswith('.json'):
            print(f)
            

if args.unix:


    records = [json.loads(line) for line in open(f)]
    frame = DataFrame(records)
    final_frame = frame[['a','c']]
    # web_server
    final_frame['web_server']=final_frame['a'].str.extract(r"(\w+)",expand=True)
    #operating system
    final_frame['Operating_System']=final_frame['a'].str.extract(r"\((.*?)\)" , expand=True)

    final_frame["from_URL"]=frame['r'].str.extract(r"https?://\s*(.*?)(?:/|$)", expand=False)
    final_frame['to_URL']=frame['u'].str.extract(r"https?://\s*(.*?)(?:/|$)", expand=False)
    final_frame['city']=frame['cy']
    final_frame.drop(columns=["a","c"] ,inplace=True)
    final_frame['longitude']=frame['ll'].str[0].fillna("missing")
    final_frame['latitude']=frame['ll'].str[1].str[0].fillna("missing")
    final_frame['timeZone']=frame['tz']

   

    clean_tz=final_frame['timeZone'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    final_frame['timeaZone']=clean_tz

    count_row = final_frame.shape[0]

    print(f[:-5]+'.csv')

    
    final_frame.to_csv (f[:-5]+'.csv')

    st=time.time()
    print("Number of rows:", count_row)
    
    print("Time Excuted " +  (time.time() - st))

 



else:



    records = [json.loads(line) for line in open(f)]

    frame = DataFrame(records)
    final_frame = frame[['a','c']]
    # web_server
    final_frame['web_server']=final_frame['a'].str.extract(r"(\w+)",expand=True)
    #operating system
    final_frame['Operating_System']=final_frame['a'].str.extract(r"\((.*?)\)" , expand=True)
    
           
    final_frame["from_URL"]=frame['r'].str.extract(r"https?://\s*(.*?)(?:/|$)", expand=False)
    final_frame['to_URL']=frame['u'].str.extract(r"https?://\s*(.*?)(?:/|$)", expand=False)

    final_frame['city']=frame['cy']
    final_frame.drop(columns=["a","c"] ,inplace=True)
    final_frame['longitude']=frame['ll'].str[0].fillna("missing")
    final_frame['latitude']=frame['ll'].str[1].fillna("missing")
    final_frame['timeZone']=frame['tz'].replace('','un known')

 
    
    final_frame['timeIn']=pd.to_datetime(frame['t'],unit='s')


    # datetime.fromtimestamp(timestamp_string)
    #frame['hc'] = frame['hc'].str[0:10]
    
    #final_frame['timeOut']=frame['hc'].apply(lambda x: datetime.datetime.fromtimestamp(x).ctime())

    final_frame['timeOut']=pd.to_datetime(frame['hc'],unit='s', errors='coerce').fillna("wrong format")
    
                #f_2['time_in'] = df['t'].apply(lambda x: datetime.datetime.fromtimestamp(x).ctime())

    
    clean_tz=final_frame['timeZone'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    final_frame['timeaZone']=clean_tz

    


    count_row = final_frame.shape[0]



    print(f[:-5]+'.csv')

    #Final filtered form of data
    final_frame.to_csv (f[:-5]+'.csv')

    et=time.time()
    
    
    print('Number of rows:', count_row )
    
    print("Time Excuted " +  str(( et- bt)))
        
    








