from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})
option.add_experimental_option("excludeSwitches", ["enable-logging"])

email = ''
password = ''

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=option)
    
    def fblogin(self):

        # open the website
        self.driver.get('https://www.facebook.com/')

        # 1. access the element
        username = self.driver.find_element_by_xpath('//*[@id="email"]')
        # 2. click the element
        username.click()
        # 3. enter the email
        username.send_keys(email)


        pwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pwd.click()
        pwd.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_b"]')
        login_btn.click()
        
        sleep(15)

        notifications = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/span/div/div[1]')
        notifications.click()


bot = Bot()
bot.fblogin()