url_list=$1 # e.g. url_list.txt
target_directory=$2 


cat $url_list | parallel -j2 "python downloader.py {} $target_directory"
echo "done"