import re
import optparse
import os
import csv
from xml.etree import ElementTree as etree

def write_data(data, filename):
	'''
	Given data (a list of row), write it to filename
	Print each row as it's being added to the file
	'''
	
	# open the output file for writing
	file = open(filename, 'w')
	spamWriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for row in data:
		assert isinstance(row, list)
		print row
		spamWriter.writerow(row)

def example_using_mysql():
	import mysql
	connection = mysql.connect('my.databaseserver.com', username='', password='')
	res = connection.execute('select * from blah')
	for row in res:
		do_something(row) # define do_something elsewhere

def fix_body(body):
	text = body.text
	# sometimes the body text is empty; if so, just skip
	if text is None:
		return
	key = '}\n\n\n\n'
	index = text.rfind(key)
	if index > 0:
		# the chop point is the index we found plus the length of those
		#  characters
		chop = index+len(key)
		# remove everything after the chop point
		fixed_text = text[chop:]
		# now that we've patched the text, replace it in the body
		body.text = fixed_text
	body.text = body.text.replace('&amp;nbsp;', '')

def patch_xml_file(filename):
	"""Read the xml file, fix the body tags, then save it to output.xml"""
	tree = etree.parse(filename)
	bodies = tree.iter('Body')
	for body in bodies:
		fix_body(body)
	# re-write the modified xml back to a file
	tree.write('output.xml', encoding='utf-8')

def read_raw_file(filename):
	"""
	Given a filename of some file, read in the data, and
	optionally transform the data.
	"""
	file = open(filename)
	data = file.read()
	return process_data(data)

def process_data(data):
	"""
	Take dirty data and return clean data
	"""
	# Now you have the file as a string in the variable called data.
	# Now you can use regular expressions to locate the chunks and replace them.
	start = re.escape('<w:')
	end = re.escape('latin;}')
	anything = '.*?'  # the question mark means get the shortest possible match
	pattern_string = start + anything + end
	print "using pattern:", pattern_string
	pattern = re.compile(start + anything + end, re.DOTALL) # I use dotall to include carriage returns

	# now replace all matches with the empty string
	replacement = ''
	clean_data = pattern.sub(replacement, data)
	return clean_data

def save_clean_data(data):
	# to make this quick and easy, just use output.dat as the filename
	# to save.
	file = open('output.dat', 'w')
	file.write(data)

def main():
	"The main entry point into our program"
	# parse the command line arguments
	parser = optparse.OptionParser()
	# provide no options
	# now parse options and arguments
	options, args = parser.parse_args()
	# check to make sure a filename was provided
	if not len(args) == 1:
		print "You didn't give me a filename"
		raise SystemExit(1)
	filename = args[0]
	if not os.path.isfile(filename):
		print "The name you gave me doesn't appear to be a file"
		raise SystemExit(1)
	patch_xml_file(filename)

if __name__=='__main__':
	pass 
	main()
