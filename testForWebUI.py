# 導入selenium 和 WebDriver
from selenium import webdriver
from time import sleep
# 通過自動化的方式叫出chrome瀏覽器
# 實例化的chromeDriver來對瀏覽器操作
driver = webdriver.Chrome()
# 通過瀏覽器，訪問指定URL
driver.get('http://www.google.com')

# 在搜尋欄中輸入 關鍵字"基隆"
driver.find_element_by_name('q').send_keys('基隆')

driver.find_element_by_name('btnK').click()
# 等待，等瀏覽器開好網頁
sleep(2)
# 點擊基隆市WIKI的條目
driver.find_element_by_xpath('//*[@id="rso"]/div[3]/div/div[1]/a/h3/span').click()
