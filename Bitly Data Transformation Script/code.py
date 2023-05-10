import json
import pandas as pd 
from pandas import DataFrame, Series

records = [json.loads(line) for line in open('usa.gov_click_data.json')]

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
final_frame['longitude']=frame['ll'].str[0]
final_frame['latitude']=frame['ll'].str[1]
final_frame['timeZone']=frame['tz'].replace('','un known')


final_frame['timeIn']=pd.to_datetime(frame['t'],unit='s')
final_frame['timeOut']=frame['hc'].apply(lambda x: datetime.datetime.fromtimestamp(x).ctime())


clean_tz=final_frame['timeZone'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
final_frame['timeaZone']=clean_tz

final_frame.to_csv('task2_Indexed3.csv')
