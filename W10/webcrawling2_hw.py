import requests
from bs4 import BeautifulSoup
import pandas as pd
def hours_to_std(ori):
    stri = ori.split(' ')
    if stri[0] =='不可':
        hour = 0
    else:
        hour = stri[2]
    return hour
url = 'https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text,'html.parser')
list = [['','','','','']]
df = pd.DataFrame(list)
df = df.reindex(columns = ['活動名稱','認證時數','已報名人數','報名日期時間','活動日期時間'])
for i in range (0,10):
    hours = sp.find( id = 'BodyContent_gvActs_lblGv_xsl_check_'+str(i))
    hours = hours_to_std(hours.text)
    name = sp.find(id = 'BodyContent_gvActs_lblGv_act_name_'+str(i)).text
    reg_dt = sp.find(id = 'BodyContent_gvActs_lblGv_reg_dt_'+str(i)).text
    act_dt = sp.find(id = 'BodyContent_gvActs_lblGv_act_dt_'+str(i)).text
    reg_num = sp.find(id = 'BodyContent_gvActs_lblGv_reg_num_'+str(i)).text
    df = df.append({'活動名稱':name,'認證時數':hours,'已報名人數':reg_num,'報名日期時間':reg_dt,'活動日期時間':act_dt},ignore_index=True)
df = df.drop(index=0)
print(df)