import os
from selenium import webdriver
import datetime
import time
from os import path

d = path.dirname(__file__)
abspath = path.abspath(d)
chromedriver = abspath + "\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        # time.sleep(0.1)
        # driver.find_element_by_id('J_Static2Quick')
        print("请在20秒内完成扫码")
        time.sleep(20)
        driver.get("https://item.taobao.com/item.htm?spm=a1z0d.6639537.1997196601.4.262f74842RgQ1E&id=601026548638")
    time.sleep(3)
    # 这里需要自己在购物车里面选择要结算的商品
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while 1:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 判断时间，时间到就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                driver.find_element_by_xpath('//ul[contains(@data-property,"高度")]/li/a').click()
                if driver.find_element_by_id('J_LinkBuy'):
                    driver.find_element_by_id('J_LinkBuy').click()
                    time.sleep(0.1)
                    while True:
                        driver.find_element_by_xpath('//div[@class="wrapper"]//a').click()


            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)
if __name__ == "__main__":
    times = input("请输入抢购时间：")
    login()
    buy(times)
