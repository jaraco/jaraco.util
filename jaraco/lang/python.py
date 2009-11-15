#!python

from __future__ import print_function, division

# a couple of utilities based on those by Samuel Huckins
#  http://dancingpenguinsoflight.com/2009/11/a-better-way-to-search-for-methods-of-python-objects/

def mf(obj, term):
	"""
	Searches through the methods and attributes defined for obj,
	looks for those containing the term passed (case insensitive).
	Prints all matches or 'No matches' if none found.
	
	>>> mf('', 'SPLIT')
	['_formatter_field_name_split', 'rsplit', 'split', 'splitlines']
	"""
	methods = dir(obj)
	term = term.lower()
	result = [m for m in methods if term in m.lower()] or 'No matches'
	print(result)

def obinfo(obj):
	"""
	Print useful information about object.

	From http://www.ibm.com/developerworks/library/l-pyint.html
	"""
	if hasattr(obj, '__name__'):
		print("NAME:    ", obj.__name__)
	if hasattr(obj, '__class__'):
		print("CLASS:   ", obj.__class__.__name__)
	print("ID:      ", id(obj))
	print("TYPE:    ", type(obj))
	print("VALUE:   ", repr(obj))
	print("CALLABLE:", ['No', 'Yes'][callable(obj)])
	if hasattr(obj, '__doc__'):
		doc = getattr(obj, '__doc__')
		doc = doc.strip()
		topfive = doc.split('\n')[0:4]
		print("DOC:     ", "\n".join(topfive))
	else:
		print("No docstring. Yell at the author.")