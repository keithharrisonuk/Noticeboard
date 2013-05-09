import unittest
from django.conf import settings
from Noticeboard import settings as noticeBoardSettings
if not settings.configured:
    settings.configure(settings=noticeBoardSettings, DEBUG=True)

from NoticeboardApp.models import Notice


class NoticeUnitTests(unittest.TestCase):

    def testGetName(self):
        notice = Notice()
        notice.FirstName = "a"
        notice.LastName = "b"
        self.assertEqual(notice.name(), "a b")

    def testNoLastName(self):
        notice = Notice()
        notice.FirstName = "a"
        self.assertEqual(notice.name(), "a")

    def testNoFirstName(self):
        notice = Notice()
        notice.LastName = "b"
        self.assertEqual(notice.name(), "b")
if __name__ == '__main__':
    unittest.main()