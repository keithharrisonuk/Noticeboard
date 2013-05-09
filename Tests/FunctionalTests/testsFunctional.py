import unittest
from selenium import webdriver
#from ghost import Ghost


class HomePageTitleTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def testTitlePage(self):
        #host = Ghost()
        #page, extra_resources = ghost.open('http://127.0.0.1:8000')
        #self.assertIn('Noticeboard', ghost.content.title())
        #assert page.http_status==200 and 'jeanphix' in ghost.content

        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Noticeboard', self.browser.title)

if __name__ == '__main__':
    unittest.main()