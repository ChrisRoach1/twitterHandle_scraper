import requests
import re
import database

regex = 'https://twitter.com/[a-zA-Z0-9$&+,:;=?@#|<>.^*''()%!-]*'
conn = database.connect()

file = input("enter file path: ")


sites = [site.rstrip('\n') for site in open(file)]
for site in sites:
    page_data = requests.get(site)
    twitter_handle = re.findall(regex, page_data.text)
    for handle in twitter_handle:
        handle = handle[8:]
        returned_handle = '@' + handle[12:]
        print(returned_handle)
        database.insert_data(conn, returned_handle)









