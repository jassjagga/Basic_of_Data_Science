>>> import numpy as np
>>> a=np.array([5,6,9])
>>> a[0]
5
>>> a[1]
6
>>> a=np.array([[1,2],[5,6]])
>>> a=np.array([5,6,9])
>>> b=np.array([[1,2],[5,6]])
>>> b.ndim
2
>>> a.ndim
1
>>> a.itemsize
4
>>> b.dtype
dtype('int32')
>>> b=np.array([[1,2],[5,6]],dtype=np.float64)
>>> a.itemsize
4
>>> b.itemsize
8
>>> b.dtype
dtype('float64')
>>> b
array([[1., 2.],
       [5., 6.]])
>>>
>>>
>>> b.size
4
>>> a.shape
(3,)
>>> b.shape
(2, 2)
>>>
>>>
>>> b=np.array([[1,2],[3,4],[5,6]],dtype=complex)
>>> b
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j],
       [5.+0.j, 6.+0.j]])
>>>
>>> np.zeros((3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones((3,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> l=range(5)
>>> l
range(0, 5)
>>> l{0}
  File "<stdin>", line 1
    l{0}
     ^
SyntaxError: invalid syntax
>>>
>>>
>>> l[0]
0
>>> l[1]
1
>>> np.arange(1,5)
array([1, 2, 3, 4])
>>> np.arange(1,5,2)
array([1, 3])
>>> c=np.arange(1,5,2)
>>> c
array([1, 3])
>>>
>>> np.linspace(1,5,10)
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
>>> np.linspace(1,5,5)
array([1., 2., 3., 4., 5.])
>>> np.linspace(1,5,20)
array([1.        , 1.21052632, 1.42105263, 1.63157895, 1.84210526,
       2.05263158, 2.26315789, 2.47368421, 2.68421053, 2.89473684,
       3.10526316, 3.31578947, 3.52631579, 3.73684211, 3.94736842,
       4.15789474, 4.36842105, 4.57894737, 4.78947368, 5.        ])
>>>
>>>
>>> b.shape
(3, 2)
>>> a.reshape(2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot reshape array of size 3 into shape (2,3)
>>> b.reshape(2,3)
array([[1.+0.j, 2.+0.j, 3.+0.j],
       [4.+0.j, 5.+0.j, 6.+0.j]])
>>> b.reshape(6,1)
array([[1.+0.j],
       [2.+0.j],
       [3.+0.j],
       [4.+0.j],
       [5.+0.j],
       [6.+0.j]])
>>> a.ravel()
array([5, 6, 9])
>>> b.ravel()
array([1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j, 5.+0.j, 6.+0.j])
>>>
>>>
>>>
>>>
>>>
>>> b=np.array([[1,2],[3,4],[5,6]])
>>> b
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> b.min
<built-in method min of numpy.ndarray object at 0x000001A26B027C90>
>>> b.min()
1
>>> b.max()
6
>>> a.sum()
20
>>> b.sum()
21
>>> b.sum(axis=0)
array([ 9, 12])
>>> added the rows and cloums
  File "<stdin>", line 1
    added the rows and cloums
          ^
SyntaxError: invalid syntax
>>>
>>>
>>> b.sum(axis=1)
array([ 3,  7, 11])
>>> now added the rows
  File "<stdin>", line 1
    now added the rows
        ^
SyntaxError: invalid syntax
>>>
>>>
>>> np.spqrt(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\anaconda\lib\site-packages\numpy\__init__.py", line 313, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'spqrt'
>>> np.sqrt(b)
array([[1.        , 1.41421356],
       [1.73205081, 2.        ],
       [2.23606798, 2.44948974]])
>>> b
array([[1, 2],
       [3, 4],
       [5, 6]])
>>>
>>>
>>> np.std(b)
1.707825127659933
>>> standaded deviation
  File "<stdin>", line 1
    standaded deviation
              ^
SyntaxError: invalid syntax
>>>
>>>
>>> basic mathis
  File "<stdin>", line 1
    basic mathis
          ^
SyntaxError: invalid syntax
>>>
>>> a = np.array([1,1],[0,1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Field elements must be 2- or 3-tuples, got '0'
>>> a = np.array([[1,1],[0,1]])
>>> b =np.array([[5,6],[7,8]])
>>> a
array([[1, 1],
       [0, 1]])
>>> b
array([[5, 6],
       [7, 8]])
>>> a+b
array([[6, 7],
       [7, 9]])
>>> a-b
array([[-4, -5],
       [-7, -7]])
>>> a*b
array([[5, 6],
       [0, 8]])
>>> a/b
array([[0.2       , 0.16666667],
       [0.        , 0.125     ]])
>>>
>>>
>>>
>>> a.dot(b)
array([[12, 14],
       [ 7,  8]])
>>> matrix product of these two arrays
  File "<stdin>", line 1
    matrix product of these two arrays
           ^
SyntaxError: invalid syntax
>>>
>>>
>>>
>>>
