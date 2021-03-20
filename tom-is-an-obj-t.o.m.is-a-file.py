#record of a session in which I called the file "theongoingmoment" as tom and discovered that the abreviation tom didn't cover when I wanted to point to the file.

Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import theongoingmoment as tom
>>> tom.a
'The'
>>> tom.b
'Ongoing'
>>> tom.c
'Moment'
>>> tom.title
'Geoff Dyer "The Ongoing Moment"'
>>> from importlib import reload
>>> reload(tom)
<module 'theongoingmoment' from 'C:\\code\\theongoingmoment.py'>
>>> tom.title
'Geoff Dyers "The Ongoing Moment"'
>>> from tom import title
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    from tom import title
ModuleNotFoundError: No module named 'tom'
>>> from theongoingmoment import title
>>> title
'Geoff Dyers "The Ongoing Moment"'
>>> reload(tom)
The Ongoing MomentakaGeoff Dyers "The Ongoing Moment"
<module 'theongoingmoment' from 'C:\\code\\theongoingmoment.py'>
>>> reload(tom)
The Ongoing Moment aka Geoff Dyers "The Ongoing Moment"
<module 'theongoingmoment' from 'C:\\code\\theongoingmoment.py'>
>>> tom.a
'The'
>>> tom.b
'Ongoing'
>>> tom.c
'Moment'
>>> dir(tom)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'title']
>>> 
