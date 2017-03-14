import unittest
import downloader
import os.path


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


class ftp_download_tests(unittest.TestCase):

    def test_ftp_1(self):
        url = "ftp://test.rebex.net/pub/example/KeyGeneratorSmall.png"
        downloader.protocol_dispatch[
            downloader.get_protocol_from_url(url)](url, "/tmp/")
        self.assertTrue(os.path.exists("/tmp/KeyGeneratorSmall.png"))
        downloader.remove_data('/tmp/', "KeyGeneratorSmall.png")


class sftp_download_tests(unittest.TestCase):

    def test_sftp_1(self):
        url = "sftp://test.rebex.net/pub/example/WinFormClient.png"
        downloader.protocol_dispatch[
            downloader.get_protocol_from_url(url)](url, "/tmp/")
        self.assertTrue(os.path.exists("/tmp/WinFormClient.png"))
        downloader.remove_data('/tmp/', "WinFormClient.png")


class http_download_tests(unittest.TestCase):

    def test_http_1(self):
        url = "http://github.com/kennethreitz/requests/tarball/master"
        downloader.protocol_dispatch[
            downloader.get_protocol_from_url(url)](url, "/tmp/")
        self.assertTrue(os.path.exists("/tmp/master"))
        downloader.remove_data('/tmp/', "master")


def main():
    unittest.main()

if __name__ == "__main__":
    main()
