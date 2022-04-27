import requests
from bs4 import BeautifulSoup
import pandas as pd
def to_std(string):
    temp= ' '
    temp= string.strip("$")
    temp = temp.split(',')
    temp = temp[0]+temp[1]
    temp = temp.split(' ')
    temp = int(temp[0])
    return temp
url = 'https://www.airbnb.com.tw/s/%E6%8B%89%E6%96%AF%E7%B6%AD%E5%8A%A0%E6%96%AF/homes?adults=2&checkin=2022-06-20&checkout=2022-06-21&date_picker_type=calendar&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&languages%5B%5D=1&languages%5B%5D=128&min_bathrooms=1&min_bedrooms=1&min_beds=1&price_max=2000&price_min=1700&query=%E7%BE%8E%E5%9C%8B%E5%85%A7%E8%8F%AF%E9%81%94%E5%B7%9E%E6%8B%89%E6%96%AF%E7%B6%AD%E5%8A%A0%E6%96%AF&refinement_paths%5B%5D=%2Fhomes&room_types%5B%5D=Private%20room&search_type=filter_change&source=structured_search_input_header&superhost=true&tab_id=home_tab&federated_search_session_id=68dd0177-2055-4ad1-a558-e6078022676a&pagination_search=true'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text,'html.parser')
temp_grade = 0
temp_price = 0
temp_name = ''
grade = sp.find_all(class_= "rpz7y38 dir dir-ltr")
price = sp.find_all(class_=["_tyxjp1"])#.text
name = sp.find_all(class_="ts5gl90 tl3qa0j t1nzedvd dir dir-ltr")#.text
list = [['','','']]
df = pd.DataFrame(list)
df = df.reindex(columns = ['Name','grade','price'])
for i in range(0,20):
    temp_name = name[i].text
    temp_price = price[i].text
    if i >= 10:
        temp_grade = float(grade[i-1].text)
    else:
        temp_grade = float(grade[i].text)
    temp_price = to_std(temp_price)
    df = df.append({'Name':temp_name,'grade':temp_grade,'price':temp_price},ignore_index=True)
df = df.sort_values(by = ['grade'],ascending= False)
print(df[0:10])
