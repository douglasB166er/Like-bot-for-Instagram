from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Dougl\geckodriver\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)

        #INSERIR USUARIO
        user_element = driver.find_element_by_xpath('//input[@name="username"]')
        user_element.clear()
        user_element.send_keys(self.username)

        #INSERIR SENHA
        sen_element = driver.find_element_by_xpath('//input[@name="password"]')
        sen_element.clear()
        sen_element.send_keys(self.password)

        #APERTA A TECLA ENTER
        sen_element.send_keys(Keys.RETURN)
        time.sleep(3)
        self.curtir_fotos("programação")

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(5)

        for x in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            hrefs = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
            [href for href in pic_hrefs if hashtag in href]
            print(hashtag + 'Fotos:' + str(len(pic_hrefs)))

            for pic_href in pic_hrefs:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    driver.find_element_by_class_name('//button[@class="_9AhH0"]').click()
                    driver.find_element_by_class_name('//button[@class="_9AhH0"]').click()
                    time.sleep(10)
                except Exception as e:
                    time.sleep(5)

#Insira seu nome EMAIL e SENHA abaixo para realizar o login no Instagram
i = InstagramBot('EMAIL', 'SENHA')
i.login()