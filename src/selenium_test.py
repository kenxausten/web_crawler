from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # => 引入Chrome的配置
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import traceback

# 配置
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36'
ch_options = Options()
# ch_options.add_argument("--headless")  # => 为Chrome配置无头模式
ch_options.add_argument(f'user-agent={user_agent}')
ch_options.add_argument('--ignore-certificate-errors')
ch_options.add_argument('--start-maximized')
ch_options.add_experimental_option('excludeSwitches', ['enable-automation'])
ch_options.add_experimental_option('detach', True) #does not close browser automatically

# 在启动浏览器时加入配置
driver = webdriver.Chrome(options=ch_options)  # => 注意这里的参数
driver.implicitly_wait(10)

# url = 'http://baidu.com'
url = 'https://10.230.194.47/edge_local_front/login.html'
driver.get(url)

username = 'admin'
password = 'Test1234'

try:
    # Step1: login
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)
    driver.find_element(
        By.XPATH, "//input[@type='password']").send_keys(password)

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='submit']")))
    driver.execute_script("arguments[0].click()", element)
    # driver.switch_to.window(driver.window_handles[-1])

    # Step2:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//span[@title='设备注册']"))).click()

    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
    driver.switch_to.frame(iframe)

    # Step3:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table')))
    # driver.switch_to.window(driver.window_handles[-1])

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[1]/div/div[2]/div/table/tbody/tr[3]/td[2]/i'))).click()

    # print(driver.page_source)

    driver.save_screenshot('./ch.png')
    table = driver.find_element(By.XPATH, "//table")
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    tds = tbody.find_elements(By.TAG_NAME, 'td')
    ths = tbody.find_elements(By.TAG_NAME, 'th')
    # print(tds)
    if len(ths) == len(tds):
        for i, th in enumerate(ths):
            print("%-13s:%s" % (ths[i].text, tds[i].text))
    # table_html = tbody.get_attribute('innerHTML')
    # print(table_html)

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="container"]/div/div[1]/div/div[2]/div/table/tbody/tr[1]/td[1]')))
    name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/table/tbody/tr[1]/td[1]')
    connection = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div[2]/div/table/tbody/tr[3]/td[1]/span/span[2]')
    # print(name.text, connection.text)

    driver.switch_to.parent_frame()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-ModuleSelection']"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@title='运维管理']")))

    # with open('reg.html', 'w+', encoding='utf-8') as f:
        # f.write(driver.page_source)
    om = driver.find_element(By.XPATH, "//span[@title='运维管理']")
    ActionChains(driver=driver).move_to_element(om).perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/section/header/div/div[1]/div[2]/div/div[3]/div[2]/div[2]/ul/li/ul/li[7]/span[2]/ul/li[1]'))).click()


    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
    driver.switch_to.frame(iframe)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div/table/tbody/tr/td')))
    time.sleep(2)
    location = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div/table/tbody/tr/td')
    print('%-13s:%s' % ('localtion', location.text))

    # iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
    # driver.switch_to.frame(iframe)

    # driver
    # exit_or_not = input("Please input Enter to exit:\n")
    # if exit_or_not == '\n':
        # driver.quit()

except Exception as e:
    print("catch an exception", str(e))
    print(traceback.format_exc())

# time.sleep(200000)

# 只有截图才能看到效果咯
# driver.save_screenshot('./ch.png')

# driver.quit()
