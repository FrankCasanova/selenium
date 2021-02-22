import unittest
from selenium import webdriver
from time import sleep



class TestingMercadoLibre(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()


    def test_search_ps4(self):
        driver = self.driver   

        country = driver.find_element_by_id('CO')
        country.click()
        sleep(2)
        print('1')

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(5)
        print('2')


        location = driver.find_element_by_xpath('/html/body/main/div/div/aside/section[2]/dl[16]/dd[1]/a/span[1]')
        sleep(1)
        driver.execute_script("arguments[0].click();", location)
        sleep(2)
        print('3')


        condition = driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        sleep(2)
        print('4')


        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        driver.execute_script("arguments[0].click();", order_menu)
        print('5')


        higher_price = driver.find_element_by_partial_link_text('Mayor precio')
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(2)
        print('6')


        articles = []
        prices = []

        for i in range(10):
            articles_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(articles_name)

            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
            prices.append(article_price)

        print(articles,prices)    


    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)            