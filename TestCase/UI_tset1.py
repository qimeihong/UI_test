from selenium import webdriver
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    # driver.get打开一个指定网页
    driver.get('http://192.168.60.146:8080/demo1.html')
    import time

    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    # 输入值
    input_el.send_keys("祁美宏")
    time.sleep(2)
    # clear:清除
    input_el.clear()
    time.sleep(2)

    checkbox_els = driver.find_elements_by_class_name('checkbox')
    print(checkbox_els)
    checkbox_els[0].click()
    time.sleep(1)
    checkbox_els[1].click()
    time.sleep(1)
    checkbox_els[2].click()
    time.sleep(1)

    button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    button_el.click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)

    driver.find_element_by_xpath('//input[@type="password"]').send_keys("123456")
    number_el = driver.find_element_by_xpath('//input[@type="number"]')
    number_el.send_keys('20')
    driver.find_element_by_xpath('//textarea').send_keys('祁美宏')
    time.sleep(2)

    select_el = driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(12) > td:nth-child(2)> select')
    s = Select(select_el)
    s.select_by_index(1)
    time.sleep(1)
    s.select_by_value('z1')
    time.sleep(1)
    s.select_by_visible_text('周龙3')
    time.sleep(1)

    # 定位超链接(超链接的名字全写)
    driver.find_element_by_link_text('当当').click()
    time.sleep(3)
    # 后退
    driver.back()
    time.sleep(1)
    # 定位超链接 (超链接的名字写一部分 就可以)
    driver.find_element_by_partial_link_text('度娘').click()
    time.sleep(3)
    driver.back()
    time.sleep(1)
    # 前进
    driver.forward()
    time.sleep(3)
    # 刷新
    driver.refresh()
    time.sleep(3)

    driver.quit()

    pass
