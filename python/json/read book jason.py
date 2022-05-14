Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f=open("c://data//book.txt","r")
>>> s=f.read()
>>> s
'{"tom": {"name": "Tom", "address": "1 red street,ON", "phone": 9898989898}, "bob": {"name": "bob", "address": "5 red street,ON", "phone": 907989898898}}'
>>> import json
>>> json.loads(s)
{'tom': {'name': 'Tom', 'address': '1 red street,ON', 'phone': 9898989898}, 'bob': {'name': 'bob', 'address': '5 red street,ON', 'phone': 907989898898}}
>>> book=json.loads(s)
>>> book
{'tom': {'name': 'Tom', 'address': '1 red street,ON', 'phone': 9898989898}, 'bob': {'name': 'bob', 'address': '5 red street,ON', 'phone': 907989898898}}
>>> book['bob']
{'name': 'bob', 'address': '5 red street,ON', 'phone': 907989898898}
>>> bob['bob']['phone']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    bob['bob']['phone']
NameError: name 'bob' is not defined
>>> book['bob']['phone']
907989898898
>>> for person in book:
	print(book[person])

	
{'name': 'Tom', 'address': '1 red street,ON', 'phone': 9898989898}
{'name': 'bob', 'address': '5 red street,ON', 'phone': 907989898898}
>>> 
>>> 