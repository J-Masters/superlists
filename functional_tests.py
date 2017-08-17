from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # you're invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 
            'Enter a to-do item')

        # type "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # hit enter, page updates and now lists
        # "1: Buy peacock feathers" as a to-do list item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table")

        # there is still a text box inviting you to add another item
        # type "Use peacock feathers to make a fly"
        self.fail('Finish the test!')

        # the page updates and shows both items on the list

        # the site has generated a unique URL so it can be revisted

        # visit the URL, the to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
