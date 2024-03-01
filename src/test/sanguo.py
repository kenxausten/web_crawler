from bs4 import BeautifulSoup
import requests
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth
import re


def get_sanguo() -> None:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    url = "http://sanguo.5000yan.com/"

    page_text = requests.get(url, headers=headers).content
    # print(page_text)

    soup = BeautifulSoup(page_text, 'lxml')

    # with open('./sanguo_xml.txt', 'w', encoding='utf-8') as fp2:
    # fp2.write(soup.prettify())

    li_list = soup.select('main ul li')

    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = li.a['href']
        detail_page_text = requests.get(detail_url, headers=headers).content
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_="grap")
        # content = ''
        # for div in div_tag.children:
        # if div != '\n':
        # content += div.get_text().replace('\r', '')
        content = div_tag.text.replace('\n', '')
        # print(content)
        fp.write(title+":"+content+'\n')
        print(title, '爬取成功！！！')

    fp.close()


def test():
    tplt = "{0:<10}\t{1:<15}\t{2:<10}\t{3:<10}"
    print(tplt.format('姓名', '年龄', '性别', '身高'))


def test12306():
    urllib3.disable_warnings()
    logger_req = requests.Session()

    res = logger_req.get('https://10.230.194.47/edge_local_front/login.html',
                         verify=False, timeout=(10, 30), auth=HTTPBasicAuth('admin', 'Test1234'))
    print(res.headers)
    print(res.headers.get('Authorization'))
    print(res.status_code)
    print(res.content)

    # res = logger_req.get('https://10.230.194.47/edge-local-web/v2/register/info')
    # print(res.status_code)
    # print(res.content)
    # with open('register.html', 'w', encoding='utf-8') as fp:
    # fp.write(str(res.content))


def re_test():
    content = 'Hello 123 4567 World_This is a Regex Demo\ntest just for\n'
    result = re.match('(.*?)(\d+)(.*)\n(.*)', content)
    print('len=%d' % len(content))
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))


# test()
# test12306()
re_test()
