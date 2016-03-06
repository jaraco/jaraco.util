#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools_scm

extensions = [
    'sphinx.ext.autodoc',
	'sphinx.ext.viewcode',
]

# General information about the project.
project = 'jaraco.util'
copyright = '2005-2016 Jason R. Coombs'

# The short X.Y version.
version = setuptools_scm.get_version(root='..', relative_to=__file__)
# The full version, including alpha/beta/rc tags.
release = version

master_doc = 'index'
