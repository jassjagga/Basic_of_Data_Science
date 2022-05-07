Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> iteam1="bread"
>>> iatem3="pasta"
>>> item4="fruits"
>>> items=["bread","pasta","fruits","vegiies"]
>>> items
['bread', 'pasta', 'fruits', 'vegiies']
>>> item[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    item[0]
NameError: name 'item' is not defined
>>> items[0]
'bread'
>>> items[0]="chips"
>>> items
['chips', 'pasta', 'fruits', 'vegiies']
>>> items[0:2]
['chips', 'pasta']
>>> items[:2]
['chips', 'pasta']
>>> items[3:]
['vegiies']
>>> items[-1]
'vegiies'
>>> items=["bread","pasta","fruits","vegiies"]
>>> items
['bread', 'pasta', 'fruits', 'vegiies']
>>> items.append("butter")
>>> items
['bread', 'pasta', 'fruits', 'vegiies', 'butter']
>>> items.insert(1,"Pea butter")
>>> items
['bread', 'Pea butter', 'pasta', 'fruits', 'vegiies', 'butter']
>>> bathroom=["shamoo", "soap"]
>>> item= items+bathroom
>>> item
['bread', 'Pea butter', 'pasta', 'fruits', 'vegiies', 'butter', 'shamoo', 'soap']
>>> food+"soda"
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    food+"soda"
NameError: name 'food' is not defined
>>> len(items)
6
>>> len(item)
8
>>> "bread" in items
True
>>> "soda" in items
False
>>> 