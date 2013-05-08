import unittest
from selenium import webdriver


class HomePageTitleTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Noticeboard', self.browser.title)

if __name__ == '__main__':
    unittest.main()