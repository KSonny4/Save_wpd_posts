# Save_wpd_posts
This script saves all preserved posts at pushshift.io from deleted wpd subreddit using their API.
Usage:
Run script "main.py" together with "posts.json" file.
post IDs are stored in "posts.json" file. The script saves "comments.json" and "post.json" for each post ID into the folder named by post ID.

Second option is to use faster "async_donwloader.py".
The first argument specifies the path, the rest arguments separated by space specifies the urls that should be downloaded.

Example:
python3 async_downloader.py /home/... https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/170px-Tux.svg.png https://cdn.pixabay.com/photo/2013/07/13/11/43/tux-158547_960_720.png


