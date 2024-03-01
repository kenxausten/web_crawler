import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
word = input('请输入一个地址：')
params = {
    'cname': '',
    'pid': '',
    'keyword': word,
    'pageIndex': '1',
    'pageSize': '10'
}
response = requests.post(url,params = params ,headers = headers)
page_text = response.text
fileName = word + '.txt'
with open(fileName,'w',encoding= 'utf-8') as f:
    f.write(page_text)
