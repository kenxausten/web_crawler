import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
post_url = 'https://fanyi.baidu.com/sug'
word = input('enter a word:')
data = {
    'kw':word
}
response = requests.post(url = post_url,data = data,headers = headers)
dic_obj = response.json()
fileName = word + '.json'
fp = open(fileName,'w',encoding= 'utf-8')

#ensure_ascii = False,中文不能用ascii代码
json.dump(dic_obj,fp = fp,ensure_ascii = False)
print('over!')
