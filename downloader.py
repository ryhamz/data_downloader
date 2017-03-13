from ftplib import FTP
import pysftp
import requests
import sys


def get_filename_from_url(url):
    return url.split("/")[-1]


def get_protocol_from_url(url):
    return url.split(":")[0]


def completeness_check(a, b):
    print a, b
    print 'goodbye'


def sftp_download(url, path):
    filename = get_filename_from_url(url)
    with pysftp.Connection('test.rebex.net', username='demo', password='password') as sftp:
        print sftp.exists('readme.txt')
        sftp.get(filename,  localpath=path + filename,
                 callback=completeness_check)
    return


def ftp_download(filename, path, username=None, password=None):
    ftp = FTP('test.rebex.net')
    ftp.login(user=username, passwd=password)

    local_file = open(path + filename, 'wb')
    ftp.retrbinary('RETR ' + filename, local_file.write, 1024)

    # Clean up
    ftp.quit()
    local_file.close()


def http_download(url, path):
    filename = get_filename_from_url(url)
    r = requests.get(url, stream=True)
    content_length = r.headers['Content-Length']
    total = 0
    with open(path + filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                total += len(chunk)
                f.write(chunk)
                print sys.getsizeof(f)
    print total, content_length
    print total == int(content_length)
    return

protocol_dispatch = {
    "http": http_download,
    "ftp": ftp_download,
    "sftp": sftp_download
}

print get_filename_from_url("http://my.file.com/file")
print get_protocol_from_url("http://something.com/myfile")

#sftp_download("test.rebex.net/readme.txt", "/Users/ryhamz/Desktop/")
url = "http://github.com/kennethreitz/requests/tarball/master"
protocol_dispatch[get_protocol_from_url(url)](url, "/Users/ryhamz/Desktop/")
