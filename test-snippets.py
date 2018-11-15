import unittest

import snippets

class SnippetsTestCase(unittest.TestCase):
    def test_first(self):
        print ("1458365220000 -->" + snippets.prettytime(1458365220000))
        print ("200 -->" + snippets.prettytime(200))
        print ("2000 -->" + snippets.prettytime(2000))
        
        import datetime
        snippets.prettytime(datetime.datetime(1970,1,1,0,0,0,0))

if __name__ == '__main__':
    unittest.main()