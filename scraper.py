import requests
import re

url = 'http://programmingchris.com/'
page_data = requests.get(url)

regex = 'https://twitter.com/[a-zA-Z0-9$&+,:;=?@#|<>.^*''()%!-]*'


twitter_handle = re.findall(regex, page_data.text)


for handle in twitter_handle:
    handle = handle[8:]
    returned_handle = '@' + handle[12:]
    print(returned_handle)