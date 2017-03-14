This module can be used to download data from multiple sources and protocols to local disk.

The list of sources will be given as input in the form of urls (e.g. http://my.file.com/file, ftp://other.file.com/other, sftp://and.also.this/ending etc)

This module downloads all the sources to a configurable locations.

### Installing Dependencies

GNU parallel: `apt-get install parallel`

`pip install -r requirements.txt`

### Call the script on its own: 

python dependencies: `python downloader.py [URL] [target_path]`

### Call with the use of GNU parallel and an input list of URLs:

`bash entrypoint.sh [url_list.txt] [target_path]`

Consider:

### The program should extensible to support different protocols

Approach: dispatch table with protocols as keys and handlers as values. 
Just need to write a handler and update the table (1 line).

### Some sources might very big (more than memory)

Approach: make use of streaming and ensure our block size is not too large.

### Some sources might be very slow, while others might be fast

Make use of threads via GNU parallel to run n jobs at once. By using this,
we can have, for example, 5 fast sources finish while 2 slow ones are downloading in parallel.

### Some sources might fail in the middle of download. \
We don't want to have partial data in the final location in any case.

Approach: If there are exceptions during a download or the size of the download 
is smaller than what is expected in the header, trigger file removal.



