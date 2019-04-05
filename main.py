import json
import os
import requests


def save(link,filename,path):
    # https://stackoverflow.com/questions/17518937/saving-a-json-file-to-computer-python
    solditems = requests.get(link)  # (your url)
    data = solditems.json()
    name = path + "/" + filename + '.json'
    with open(name, 'w') as f:
        json.dump(data, f)



data = []
with open("posts.json", "r") as read_file:
    data = json.load(read_file)


count = 0
for post in data['posts']:
    cmd = 'mkdir {0}'.format(post)
    os.system(cmd)

    comments_json = 'https://api.pushshift.io/reddit/search/comment/?link_id={0}'.format(post)
    post_json = 'https://api.pushshift.io/reddit/submission/search/?ids={0}'.format(post)

    save(post_json, "post", post)
    save(comments_json, "comments",post)

    cmd2 = 'cd ..'
    os.system(cmd2)
    if count % 100 == 0:
        text = str(count) + " files downloaded"
        print(text)
    count += 1



