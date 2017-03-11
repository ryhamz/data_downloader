from ftplib import FTP
import pysftp


def get_filename_from_url(url):
    return url.split("/")[-1]


def get_protocol_from_url(url):
    return url.split(":")[0]


def sftp_download(filename):
    with pysftp.Connection('test.rebex.net', username='demo', password='password') as sftp:
        print sftp.exists('readme.txt')
        sftp.get(filename)
    return

print get_filename_from_url("http://my.file.com/file")
print get_protocol_from_url("http://something.com/myfile")

sftp_download("readme.txt")
