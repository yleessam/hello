import requests

print('haha')

import requests
url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)
#r.status_code
print(r.json())