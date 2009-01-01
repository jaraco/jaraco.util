#!/usr/bin/python
# -*- coding: utf-8 -*-

'''dvdinfo.py [--title n] [dvd device]
dvdinfo.py --help | -h

Displays information on the longest title on the DVD. If the dvd
device is not specified, /dev/dvd is used. You can also use a DVD
image as the device.

The title with the largest number of titles is considered the 'longest
title'. This is the feature film on the majority of the DVDs.

If you want to display the information on a specific title, pass the
title number with the --title option.
'''

# Changes:
#
# Version 1.1, 2006-08-13 13:00
#
#    - Only consider a title the main movie if it has an audio track.
#      This ensures that picture-titles with one chapter per picture
#      aren't considered the main movie, even though such titles can
#      have a lot of chapters.
#
#    - Added the ability to specify which title to read.
#
#    - Display 1/? instead of 1/1 if the total number of titles is
#      unknown.
#
# Version 1.0, released 2006-06-12 23:05
#
#    - Initial release

# COPYING: this software is released under the GPL licence. For more
# information, see http://www.stuvel.eu/licence

import re
from os import popen4
import sys
import getopt

__author__ = '$Author$'[9:-2]
__email__ = 'jaraco@jaraco.com'
__revision__ = '2.0'
__url__ = 'http://www.jaraco.com'

device = 'd:'

def banner():
	'''Display the banner'''

	print 50*'='
	print 'dvdinfo.py version %s' % __revision__
	print '%s <%s>' % (__author__, __email__)
	print __url__
	print 50*'='
	print

class MetaTitleParser(type):
	"""
	A metaclass for title parsers that keeps track of all of them.
	"""
	
	_all_parsers = set()
	
	def __init__(cls, name, bases, attrs):
		if name == 'TitleParser': return # don't add the base class
		cls._all_parsers.add(cls)

class TitleParser(object):
	__metaclass__ = MetaTitleParser
	
	def __init__(self, info):
		# info is the object that stores title info
		self.info = info
		self.pattern = re.compile(self.pattern)
	
	def __call__(self, line):
		self.parse(line)

	def parse(self, line):
		match = self.pattern.search(line)
		match and self.handle(match)
	
	@classmethod
	def create_all(cls, info):
		"Create all of the title parsers associated with this info"
		return [parser(info) for parser in cls._all_parsers]

class MaxTitlesParser(TitleParser):
	pattern = '^There are (?P<max_titles>\d+) titles'
	def handle(self, match):
		self.info['max_titles'] = int(match.groupdict()['max_titles'])

class ChaptersParser(TitleParser):
	pattern = '^There are (?P<chapters>\d+) chapters'
	def handle(self, match):
		self.info['chapters'] = int(match.groupdict()['chapters'])

class AudioParser(TitleParser):
	pattern = '^audio stream: (?P<stream>\d+) format: (?P<format>.+) language: (?P<language>.+) aid: (?P<aid>\d+)'
	def handle(self, match):
		'''Parse a single audio-channel line'''
		d = match.groupdict()
		d['aid'] = int(d['aid'])
		self.info['audiotracks'][d['aid']] = d

class SubtitleParser(TitleParser):
	pattern = '^subtitle \(\s*sid\s*\): (?P<sid>\d+) language: (?P<language>.*)'
	def handle(self, match):
		'''Parse a single subtitle-channel line'''
		d = match.groupdict()
		d['sid'] = int(d['sid'])
		self.info['subtitles'].append(d)

class NaviParser(TitleParser):
	pattern = 'Found NAVI packet!'
	def handle(self, match):
		self.info['navi_count']+=1

class TitleInfo(dict):
	def __init__(self, *args, **kwargs):
		self.update(max_titles=0, chapters=0, audiotracks={}, subtitles=[], navi_count=0)
		dict.__init__(self, *args, **kwargs)

def title_info(title):
	'''Returns title information about a single title.
	
	Returns a tuple max_titles, chapters, audiotracks, subtitles.
	'''

	options_to_consider = '-identify'
	# need at least two -v to get "Found NAVI packet"
	mpcmd = 'mplayer -v -v -v -nosound -frames 0 -dvd-device %s dvd://%i -vo null'

	(mplayer_stdin, mplayer) = popen4(mpcmd % (device, title))
	
	mplayer_stdin.close()

	info = TitleInfo()

	parsers = TitleParser.create_all(info)

	for line in mplayer:
		for parser in parsers:
			parser(line)
		if info['navi_count'] > 100: break
	
	mplayer.close()
	#mplayer.wait()
	
	return (info['max_titles'], info['chapters'], info['audiotracks'],
			info['subtitles'])

def main():
	'''The main function'''

	global device

	# Set to the real value after the first read.
	max_title = '?'

	# Info of the longest title
	longest_title = 0
	chapters = None
	audiotracks = None
	subtitles = None

	title = 1
	find_longest = True

	banner()

	# Parse options
	opts, args = getopt.gnu_getopt(sys.argv[1:], 'ht:', ('help',
		'title='))
	opts = dict(opts)

	if '-h' in opts or '--help' in opts:
		print __doc__
		return

	if '-t' in opts:
		title = int(opts['-t'])
		find_longest = False
	if '--title' in opts:
		title = int(opts['--title'])
		find_longest = False

	if args:
		device = args[0]

	if find_longest:
		# Walk through all titles
		while max_title == '?' or title <= max_title:
			sys.stdout.write('Reading title %i/%s   \r' % (title, max_title))
			sys.stdout.flush()

			max_title, c, a, s = title_info(title)

			# Remember info about the title with the most chapters,
			# but only if it has audio tracks.
			if a and (chapters is None or c > chapters):
				chapters = c
				audiotracks = a
				subtitles = s
				longest_title = title

			title += 1

		print 'Done reading.            '

		print 'Longest title: %s' % longest_title
	else:
		print 'Reading title: %i' % title
		# Get info about given title
		max_title, chapters, audiotracks, subtitles = title_info(title)
	
	if not max_title:
		raise SystemExit("Unable to find any titles on %s" % device)

	print 'Chapters: %s' % chapters

	print 'Audio tracks:'
	for info in audiotracks.itervalues():
		print '\taid=%(aid)3i lang=%(language)s fmt=%(format)s' % info

	print 'Subtitles:'
	for info in subtitles:
		print '\tsid=%(sid)3i lang=%(language)s' % info

if __name__ == '__main__':
	main()
