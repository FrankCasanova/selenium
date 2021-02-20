import unittest
from selenium import webdriver

class Home_page_tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.get('https://madison-island.com/search?q=')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('SearchInput')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name('input-group__field')

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name('btn--link')

    def test_count_of_navs(self):
        navs_list = self.driver.find_element_by_class_name('site-nav')
        navs = navs_list.find_elements_by_class_name('site-nav__link')
        self.assertEqual(3,len(navs))

    def test_refer_friend(sefl):
        refer_friend = sefl.driver.find_element_by_xpath('/html/body/div/a[1]')    
    
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('site-header__icons-wrapper a.site-header__icon')
        


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)