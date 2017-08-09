from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # check out the site's homepage
        self.browser.get('http://localhost:8000')

        # notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # you're invited to enter a to-do item

        # type "Buy peacock feathers" into a text box

        # hit enter, page updates and now lists
        # "1: Buy peacock feathers" as a to-do list item

        # there is still a text box inviting you to add another item
        # type "Use peacock feathers to make a fly"

        # the page updates and shows both items on the list

        # the site has generated a unique URL so it can be revisted

        # visit the URL, the to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
