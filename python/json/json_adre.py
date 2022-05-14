book = {}
book['tom'] = {
    'name' : 'Tom',
    'address': '1 red street,ON',
    'phone': 9898989898
}
book['bob'] = {
    'name' : 'bob',
    'address': '5 red street,ON',
    'phone': 907989898898
}

import json
s= json.dumps(book)
with open("c://data//book.txt","w") as f:
    f.write(s)
