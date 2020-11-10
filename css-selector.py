from selenium import webdriver
from time import sleep

#打開 google
driver=webdriver.Chrome()
sleep(2)
driver.get("http://www.google.com")
sleep(2)
#定位搜索欄
# <input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Google 搜尋" value="" aria-label="搜尋" data-ved="0ahUKEwiq-_rujPXsAhUNiZQKHRLWA_MQ39UDCAY">
driver.find_elements_by_css_selector("html>body>div>div>from>div>div>div>div>div>input").send_keys("基隆")
