# -*- coding: UTF-8 -*-

"""
Setup script for building jaraco.util distribution

Copyright © 2004-2010 Jason R. Coombs
"""

try:
	from distutils.command.build_py import build_py_2to3 as build_py
	# exclude some fixers that break already compatible code
	from lib2to3.refactor import get_fixers_from_package
	fixers = get_fixers_from_package('lib2to3.fixes')
	for skip_fixer in ['import']:
		fixers.remove('lib2to3.fixes.fix_' + skip_fixer)
	build_py.fixer_names = fixers
except ImportError:
	from distutils.command.build_py import build_py

import sys
import subprocess

from setuptools import find_packages, Command

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import py.test
        raise SystemExit(py.test.main(args=[]))

name = 'jaraco.util'

setup_params = dict(
	name = name,
	use_hg_version=True,
	description = 'General utility modules that supply commonly-used functionality',
	long_description = open('README').read(),
	author = 'Jason R. Coombs',
	author_email = 'jaraco@jaraco.com',
	url = 'http://pypi.python.org/pypi/'+name,
	packages = find_packages(exclude=['tests']),
	namespace_packages = ['jaraco',],
	license = 'MIT',
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
	],
	entry_points = {
		'console_scripts': [
			'roll-dice = jaraco.util.dice:do_dice_roll',
			'calc-prorate = jaraco.dateutil:calculate_prorated_values',
			],
	},
	install_requires=[
	],
	extras_require = {
		'image':
			['pil>=1.1.6'],
	},
	dependency_links = [
	],
	tests_require=[
		'pytest>=2',
	],
	setup_requires=[
		'hgtools>=0.4',
	],
	cmdclass=dict(
		build_py=build_py,
		test=PyTest,
	),
)

if __name__ == '__main__':
	from setuptools import setup
	setup(**setup_params)
