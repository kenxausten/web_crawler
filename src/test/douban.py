import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
url = "https://movie.douban.com/j/chart/top_list"

params = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',#从第几部电影开始取
    'limit': '20'#一次取出的电影的个数
}
response = requests.get(url,params = params,headers = headers)
list_data = response.json()
fp = open('douban.json','w',encoding= 'utf-8')
json.dump(list_data,fp = fp,ensure_ascii= False)

print('over!!!!')
