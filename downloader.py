from ftplib import FTP
import pysftp
import requests
import sys
import os


def get_filename_from_url(url):
    # Helper function that returns filename
    # from a given url
    return url.split("/")[-1]


def get_protocol_from_url(url):
    # Helper function that returns the protocol
    # from a given url.
    return url.split(":")[0]


def get_address_from_url(url):
    return url.split("://")[1].split('/')[0]


def sftp_download(url, path):
    filename = get_filename_from_url(url)
    address = get_address_from_url(url)

    with pysftp.Connection(address, username='demo', password='password') as sftp:
        print sftp.exists('readme.txt')
        try:
            print "sftp output: "
            print sftp.get(filename,  localpath=path + filename,)
            print "end sftp output"
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            remove_data(path, filename)
    return


def ftp_download(url, path, username=None, password=None):
    filename = get_filename_from_url(url)
    address = get_address_from_url(url)
    ftp = FTP(address)
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
    if not total == int(content_length):
        remove_data(path, filename)
    remove_data(path, filename)
    return

# Remove a file at the given path.
# Will be used to remove incomplete data after partial downloads


def remove_data(path, filename):
    os.remove(path + filename)


# Dispatch table containing our supported protocols as keys
# and their handlers as values
protocol_dispatch = {
    "http": http_download,
    "ftp": ftp_download,
    "sftp": sftp_download
}

if __name__ == "__main__":
    print get_filename_from_url("http://my.file.com/file")
    print get_protocol_from_url("http://something.com/myfile")

    ftp_download("sftp://test.rebex.net/readme.txt",
                 "/Users/ryhamz/Desktop/", "demo", "password")
    # url = "http://github.com/kennethreitz/requests/tarball/master"
    # protocol_dispatch[get_protocol_from_url(url)](
    #    url, "/Users/ryhamz/Desktop/")
