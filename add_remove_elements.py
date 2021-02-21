import unittest
from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver

class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Add/Remove Elements').click()


    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?' ))
        elements_remove = int(input('How many elements will you remove?' ))

        total_elemetns = elements_added - elements_remove

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            sleep(1)
            add_button.click()

        for i in range(elements_remove):
            try:
                delete_button = driver.find_element_by_class_name('added-manually')
                sleep(1) ##########
                delete_button.click()
            except:
                print('You\'re triying to delete more elements than the existence')
                break  
        
        if total_elemetns > 0:
            print(f'there\'re {total_elemetns} elements on screen')
        else:
            print('there are 0 elements on screen')             
        pass    

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)            