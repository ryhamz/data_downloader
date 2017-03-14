import unittest
import downloader


class get_protocol_from_url_tests(unittest.TestCase):

    def test_http_1(self):
        res = downloader.get_protocol_from_url("http://my.path.to/thisfile")
        self.assertEqual(res, "http")

    def test_http_2(self):
        res = downloader.get_protocol_from_url("http://my.path.to/thisfile")
        self.assertNotEqual(res, "ftp")


class get_filename_from_url_tests(unittest.TestCase):

    def test_filename_1(self):
        res = downloader.get_filename_from_url(
            "http://my.path.to/thisfile.dat")
        self.assertEqual(res, "thisfile.dat")

    def test_filename_2(self):
        res = downloader.get_filename_from_url(
            "ftp://my.path.to/otherfile.txt")
        self.assertNotEqual(res, "otherfile")


def main():
    unittest.main()

if __name__ == "__main__":
    main()
