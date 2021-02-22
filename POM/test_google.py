import  unittest
from selenium import webdriver
from google_page import Google_Page


class GoogleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='../chromedriver')
        
        

    def test_search(self):
        google = Google_Page(self.driver)
        google.open()
        google.search('Platzi')
        
        self.assertEqual('Platzi', google.keyword)
    
            
    @classmethod
    def tearDown(cls) -> None:
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)  