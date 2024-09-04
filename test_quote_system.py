import unittest
from io import StringIO
import sys
from unittest.mock import patch
import quote_system


class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("\n"))
    def test_1_choose_quote_file(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        self.assertEqual(quote_system.ask_file_name('quotes.txt'),"quotes.txt")
    
    @patch("sys.stdin", StringIO("\n"))
    def test_2_choose_quote_file_blank_input(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        self.assertEqual(quote_system.ask_file_name(''),"quotes.txt")
      
    def test_3_file_not_found(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        quote_system.read_file("mock.txt")
        self.assertEqual("""FileNotFoundError successfully handled
[Errno 2] No such file or directory: 'mock.txt'\n""", text_capture.getvalue())

    def test_4_file_sucessfully_opened(self):

            text_capture = StringIO()
            sys.stdout = text_capture

            quote_system.read_file("quotes.txt")
            self.assertEqual("""File successfully opened...\n\n""", text_capture.getvalue())
            self.assertEqual(type(quote_system.read_file("quotes.txt")),str)


    def test_5_choose_random_quotee(self):

            self.assertEqual(quote_system.select_random_quotee(["Eleanor Roosevelt"]), "Eleanor Roosevelt")

    def test_6_find_quote_aginst_quotee(self):

        self.assertEqual(quote_system.find_quote("Thomas Edison",["Thomas Edison ~ \"I failed my way to success.\""]),
         "Thomas Edison ~ \"I failed my way to success.\"")

    def test_7_quote_does_not_exist(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        self.assertEqual(quote_system.find_quote("Walt Disney",[["""Estee Lauder ~ "I never dreamed about success, I worked for it."
Thomas Edison ~ "I failed my way to success.",
Alexander Graham Bell ~ "Before anything else, preparation is the key to success."""]]), "Quote/quotee does not exist.")

    @patch("sys.stdin", StringIO("\n"))
    def test_8_find_quote_against_quotee_2(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        self.assertEqual(quote_system.ask_file_name('quotes.txt'),"quotes.txt")
        self.assertEqual(quote_system.find_quote("Anne Frank",["Anne Frank ~ \"I failed my way to success.\""]),
         "Anne Frank ~ \"I failed my way to success.\"")

    def test_9_final_output(self):

            text_capture = StringIO()
            sys.stdout = text_capture

            quote_system.final_output("Albert Einstein ~ \"We cannot solve our problems with the same thinking we used when we created them.\"","Albert Einstein")
            self.assertEqual("""Quote found in file:
'Albert Einstein': "We cannot solve our problems with the same thinking we used when we created them."\n""", text_capture.getvalue())

    @patch("sys.stdin", StringIO("myfile.txt\n"))
    def test_10_unique_text_file(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        self.assertEqual(quote_system.ask_file_name('myfile.txt'),"myfile.txt")
        quote_system.read_file("myfile.txt")
        self.assertEqual(quote_system.find_quote("Walt Disney",["""Walt Disney ~ \"All our dreams can come true,if we have the courage to pursue them.\""""]),
"""Walt Disney ~ \"All our dreams can come true,if we have the courage to pursue them.\"""")
        quote_system.final_output("Walt Disney ~ \"All our dreams can come true,if we have the courage to pursue them.\"","Walt Disney")
        self.assertEqual("""File successfully opened...\n
Quote found in file:
'Walt Disney': "All our dreams can come true,if we have the courage to pursue them."\n""", text_capture.getvalue())
    
if __name__ == '__main__':
    unittest.main()
