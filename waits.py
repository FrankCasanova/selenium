import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Modulo para poder seleccionar del dropdown
from time import sleep
from selenium.webdriver.common.by import By #Hacer referencia a un elemento del sitio web, para interactuar
from selenium.webdriver.support.ui import WebDriverWait # Modulo para  manejo de esperas explicitas
from selenium.webdriver.support import expected_conditions as EC #esperas explicitas




class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/') #poner la direccion

    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()



    def test_create_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))


    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)