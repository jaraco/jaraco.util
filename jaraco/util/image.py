#!python
# -*- coding: utf-8 -*-

# $Id$

"""
This module requires PIL
Copyright © 2008 Jason R. Coombs
"""

from __future__ import division

import operator
from collections import namedtuple

def calc_aspect(size):
	"aspect = size[0] / size[1] # width/height"
	return reduce(operator.truediv, size)

Dimensions = namedtuple('dimensions', 'width height')

def replace_height(size, new_height):
	return Dimensions(size.width, new_height)

def replace_width(size, new_width):
	return Dimensions(new_width, size.height)

def resize_with_aspect(image, max_size, *args, **kargs):
	"""
	Resizes a PIL image to a maximum size specified while maintaining
	the aspect ratio of the image.
	
	>>> img = load_apng()
	>>> newimg = resize_with_aspect(img, Dimensions(10,15))
	>>> newdim = Dimensions(*newimg.size)
	>>> newdim.width <= 10 and newdim.height <= 15
	True
	"""

	max_size = Dimensions(*max_size)
	aspect = calc_aspect(image.size)
	target_aspect = calc_aspect(max_size)

	if aspect >= target_aspect:
		# height is limiting factor
		new_height = int(round(max_size.width/aspect))
		new_size = replace_height(max_size, new_height)
	else:
		# width is the limiting factor
		new_width = int(round(max_size.height*aspect))
		new_size = replace_width(max_size, new_width)
	return image.resize(new_size, *args, **kargs)

apng = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x03 \x00\x00\x02X\x08\x03\x00\x00\x00\xad\xa8rB\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00 cHRM\x00\x00z&\x00\x00\x80\x84\x00\x00\xfa\x00\x00\x00\x80\xe8\x00\x00u0\x00\x00\xea`\x00\x00:\x98\x00\x00\x17p\x9c\xbaQ<\x00\x00\x03\x00PLTE\x00\x00\x00\x01\x01\x01\x08\x08\x08\n\n\n\x0c\x0c\x0c\x10\x10\x10\x14\x14\x14\x18\x18\x18   %%%(((000444888999<<<>>>@@@GGGHHHPPPQQQXXX```ccchhhkkkmmmppptttwwwxxx\x7f\x7f\x7f\x85\x85\x85\x87\x87\x87\x8f\x8f\x8f\x94\x94\x94\x95\x95\x95\x97\x97\x97\x9f\x9f\x9f\xa1\xa1\xa1\xa3\xa3\xa3\xa7\xa7\xa7\xaf\xaf\xaf\xb1\xb1\xb1\xb7\xb7\xb7\xbf\xbf\xbf\xc7\xc7\xc7\xcc\xcc\xcc\xcf\xcf\xcf\xd1\xd1\xd1\xd7\xd7\xd7\xd9\xd9\xd9\xdf\xdf\xdf\xe6\xe6\xe6\xe7\xe7\xe7\xef\xef\xef\xf3\xf3\xf3\xf7\xf7\xf7\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ulsN\x00\x00\x00\x18tEXtSoftware\x00Paint.NET v3.30@\x84G\x10\x00\x00*\x90IDATx^\xed\x9diC\x1bMs\xb5;$\xbcl\xe1%\x04\x0c&\xc1as \x86\x07\x01\xc1\x18Y\xfd\xff\xffW\xbaGHHB\xd2l\xd5\xb5t\x1f\x7f\xb8\x173\xd3U}\xaa\x0esM\xcf\xe6v_<\xfe@\x01(\xb0T\x81\xc1\x96s\x1b\xb7\x10\x07\n@\x81e\n\\:\xe7\xce\x9d;\x19B\x1e(\x00\x05\x16\x15x\xdfw\x1b7\xce?l:`\x16\xba\x03\n,*\xf0\xb8\xe9\xb6\x9f\xbc\xf3\xfe-\x18\x05\x98\x85\x06\x81\x02s\n\\8w\x1c\xd0*\x18\xc4\xfb\xf0\xdf\xc0,\xf4\x07\x14\xf8T \xe0\x95\xbb\x8e\xff[\x19\xc4\x87\xa3\t0\x0b\xfd\x01\x05&\n\x04Cl=U\xff36\x88\xaf\xceG\xa0\x0f\x14\x80\x02\x1fHu\xf4\xb1r\xf5a\x90\n\xb3&\x7f\x07\x91\xa0@\xc9\nL\xf1j\xe6\x082\xc6\xac\x8f\xa3J\xc9\xe2`\xee\xc5+0o\x84\xe9\x11\xa4\xc2,wY\xbc<\x10\xa0p\x05\x16Pj\xc6 \x15f\x1d\xbe\x17\xae\x0f\xa6_\xb4\x02\xf1d\xbcZ\xbd\x9a\xfc\x993H\x85Y\x83\xa2\x05\xc2\xe4\x8bV`|qp\xb5A\x80YE\xb7G\xf1\x93\xff\xb88\xb8\xc6 \xc0\xac\xe2\x9b\xa4\\\x01\x96^\xeb\x98G\xac(\x0eV\xb3\xcam\x91\xa2g\x1e\xaf\x96\xcf\xe3\xd5\xfc2\xefT\x9c\xb9e\xe0\xa2%\xc3\xe4\xcbQ`\x14nk\x8f\xf7^-\xfe\xf9z\x04\t[\xe0\xa2a9\x8d\x81\x99V\n\xc4;v\x97\xdeJ\xb2\xd4 \xfeq\x0b\x17\r\xd19\x05)\x10\x9e\xf9Xq\x95|\xb9A\xfc\xfb\xe1\xc7\xcd\x8c\x05\x89\x84\xa9\x96\xaa@\xc4\xabU\xf7Y\xad0\x88\xf7\xe1iC\xdc\x9bUj\xc7\x945\xef\x80W\xe3[\xdb\x97\xfdYi\x10\x1f\x9eW\xc7\xbdYeuJ\x99\xb3]\x8dW+V\xb1&2\r\x8f\x80Ye\xb6LI\xb3^\x87W5\x06\xf1\xfe\x1a\x98UR\xaf\x948\xd7\xb5xUk\x10\xff\x04\xcc*\xb1k\xca\x99s\xfdU\xf1\xd5\xe7 \x95J\x11\xb3p\x0b|9\rS\xd8L\x1b\\\xf0\xab1H\x85Y\xb8\x05\xbe\xb0\xbe)d\xba\x8dn\x19\xa95H\x85Y\xb8\x05\xbe\x90\x9e)i\x9a_omo\xb7\xcc;\xdd:b\xd6EI\xcaa\xae%(\xb0\xe4\xd6\xf6\x8e\x06\xa90k\x1fO\x1a\x96\xd05\xc5\xcc\xb1\xf1k|\xea\x11+j\x160k\xf3\xb1\x18\xf10\xd1\xec\x15X~k{\xe7#HX\xcd\n\xf7f\x01\xb3\xb2\xef\x9bR&\xd8\x10\xaf\xea\xaf\x83\xcc\x08\x06\xcc*\xa5{\xb2\x9fgc\xbcje\x10`V\xf6\x8dS\xc8\x04\x9b\xad^M\xc4hv\x0eRm\x8d\xd5\xacB:(\xebi\x8eZ\xe0U\xbb#H\xd8\x1a\x98\x95u\xef\x940\xb9\x95O\x0e\xae\x9a|\x8b#\xc8\xc7j\xd6C\t:b\x8ey*\x10nm_x\xefU\xdd<\xdb\x19\xa4\xc2\xac\xf3Q\xdd\xa0\xf89\x14\xd0\xa8\xc0\xaa\x173\xac\xcb\xb5\xa5A\xbc\xbf\xd9p\xfb\xaf\x1ag\x8f\x9c\xa0\xc0z\x05^\xf7:|\xe3\xa3\xb5A\xfc\xd3\xb6\xdb\xbcG-\xa0\x805\x05\xee[\xe3U\xeb\x93\xf4\xb1$\xc3c\xe7\xce\x80Y\xd6\xfa\xa3\xf0|G\xa7\xcb\xdf{U\'K\xfb#H\x18\xf1v\xc3\xed\x01\xb3\xea\xa4\xc5\xcf\x15)\xd0\t\xaf:\x1eA\xc2n/\xbb\xc0,E\xd5G*u\nt\xc3\xab\xee\x06\x01f\xd5U\x04?W\xa4\xc0\xe8\xac\x1b^\xf50H\xb5\x9a\xb5\xf7&(\xc2\xdf\xdf\x9f\xc1\xff\xb12\x8f\xe7?5)>\x93L\xe1\xef\xf3s\x93\x81\x9e\x7f\x0e\xfe\x92\xc4\xc3 m\x14h}qpv\xf0N\xe7 \xd5\x00q5\xeb\xa1M\x9e$\xdb\xfe\xbc\xaa\xfe\xfc\xf4W\x07\xd3\xf1\xbe\xb9\x9f+\xc6\xfe\xedvV\xfc\xe4\xcf\xaf\xf1\x0fv\x9a4vm\xe6?\x0f\x0e\\\xfd@\x07;\x07\x07W\xcb\xc6\x1a\xe0\x89\xcdZ\x89\xbbo\xd0\xfe\xe2 \x8dA*\xccb\xbfh\xf8\xfd\xe0`\'\xf4\xd9\xf7Y\x83\x0c\xbe\xcd\x1cM\xe6\x85\xfc\xfec\x85\xb0\x13\x7f\xd1\x18\xa4\x91\xd3~\xee\xac:|,\xb7M\xf7\x96\xc0\x9e\x9f\n\xc4\x8b\x83\'K\xde\xda\xdeT\xa3\xeeG\x90\x10!\xacf\t<i8n\xa7\xd0\xe1\x7f\x16\x7fi\xff^\r:\xcf\x0b\xb05c\x90\xe7\x0f{}\xdd\xf9\xf7G\x80\xc9\xbf\xbd\xff\xdcv\xb2\xd3\xc4\x9b\x13\xa7MGy\x9el;)\xc5\xf4\x98\xf7g\x9a\xcb\xc7&0H\xd3vm\xbd]\xc4\xab\xdb\xd6{\xcd\xec\xd0\xcb \xd5j\x16;fM\x0c\xf2cgg\'\xb4\xe7U\xf8W\xd5\xc8\x7f\xc2\xb1e\xe7\xdb\xac\x18\xd3\xff\x8f\xdb\xcc\x1e+\xbe\xed\xec\xb8\xf1\xdf\xec\xfc<\xd8q\xdf\xc3N\xcfq\xef9\xd4\x19\xc4\xbf\t\x9bT?\x89G\xa2\xe9\xb6\x838\\\xb4iL\xe1`\xec\xa2\xf1\xf0?\xe3O\xe2\xb6\xd3M>\xf3\x99\x18$\x04\xaf\xd2\x9c\x0c7\xcee\x15\x0b\xf6).\xf6\rx\xb5\xfb\xd2K\x86~\x06\xf1\xc3\x13~\xcc\xfa0\x88;\xf8\xfb\xf7`\xec\x87qs~\x8fg%\x0b\'\xe5\xe3\xa6\xfc\xb3\xf3q\xc6\xf1\xb5[w\xc2\x8f~\xba\xe0\xb3\x9dp\x1e\xf3}\xb6K\xff\xec\x04\xdf\xc4\xe1\xe2\xbf\x7f\xb90\xc2t\xdb\x83h\x81\xc0KW\xc1Q\x7f\x0f\xc6\'C\xe3\x1c~\x87\x1d~\xee\x84\x7fL6\x99D|\x0e\x16\x18{\xf2\xdb\xc1\x1f\xff\x1c\xc7\x9c\x0e\xe7q\x04\xe9\xd5\xc3+w\xee\x8bWq\xe0\x9e\x06\x19c\x16\xefj\xd6\x87Ab3\x7f\xfcR\x1e7\xe7\xb7\xd8\x98\x0b\x7f\xc6\x1b\xfc\xfez\x16?E\xacx~\x1f\xf6\xffUyc\xf6(\xf3\xe3\xc3-\xe3\x9fD+F\x0fU\x9b\xc4\xf6\xae6\xaf\x8e\x15\xd1^s\xbb\xcen2\xcd\xe7\xf9\xf9\xc7A\\\xeb\xfaS\x1d\xa6\xe2\xe0\xd3\xe1`\x904\xfex\xed\x8bW$\x06\xe1\xc7\xac\xe99\xc8\x82A\x02b\x1d,.g}\xf8  \xd6\xf7\xf9\x95\xa2\xb9\x93\xf4\xd0\xd1W\xe1\xcc\x7f~)\xea\xe3\xc8\x10~\x12u\x8a\xdbW\xf6\x89\xff\x08\xfc\xf4-\x1e\x93\xc6\x07\xa6\xb1\xab>0/,"T\x0bZ\x93MfJ?\x0e\xf9\\\xd9\xf89\x1ad2\x1c\x0c\x92\xc4 \xe1\xe2`O\xbc\xa21H\x85Y\x9c\xf7f\xad2H8R\xfc\xd8\xf9\\\xfc\xadD\x9f\x9e\x18\xff\xfa\xe6\xe6\xae\x96|1H\xfc\xf5>w\x9a>o\x90\xc8o\x9f\x1d\xed\x07\xdf]8zT\xc7\x80?\xb3\x069\xf8\x16\x06\x19\xff\xc5x\x93\xaf\x06\xa9\x0e8\xf1\xb0\x04\x83$\xf1\xc5\xc7\xa0\xf1\xe2`\x9f\xd5\xabIn\xbd\x11+\x0e\xc4{o\xd6j\x83x\xff\x8f\x85\xcb\x113WK&\r?\x9e\xf9\xa2A~}\xe1\xb3\x1f\x1f\xab\xb2\x83\xb8\x12P\xd1\xd4\x8cA\xc6\x90\x14V\x9b\xc7\xbd>9\x82<\xc7\xf0\x1f\x06\x19o\xf2\xc5 cW\xcd\xfb\xad:a\xa9\xfe|[z\x9d$e#e:v\xbc\xf7\xaa\xd7\xea\x15\xa9Ax\xef\xcdZ0H\xb8t\xb8\xf3#\\9\xf4?\x7f=?\xcf\x9df\xff\xbd\xba\xfa\xb6su\xf5\xd7\xff\xbdz~\xfeU-;M\xff\x0c\xdc\x8f\xe7_\xe1<{\xda\xf4\x07\x07a\xf7\xd9M\xfe\xec\x84\xbf\xb9\n\xe68\xd8\xf9\x15\xc6\x9d\xdd\xf6j\xf0<\x88\'%\xffp\xdf\xc7\xe3Ns\xd8\xf9\xfe|\xb5\x13]2\xd9\xe4\xabA~\xec\\=_\xb9\x00|\x9f~\xbb\xda\xf9\xf9\\\xc1\xe1O\xb7\xf2ZI\xa6\x8d\x9chZ4x\x15\x93#9\x82\x84[\xe0\x191\xeb\xfb\xb8\x97\xe2o\xef\xf8\x8fH\xfd\xf1\xcaa\xf8\x8f\x9d\x83\xef\xb3\xe7\xe9\xbf\xab\x9f\x1c\xfc\xf6\xe1?B\xb7\xcf\xd7\xe2W\xf5\x13_]c\xac\xfeQ\xed>\xbb\xcd\x9f0\xf2\xb7xm/\xfc\xa4\x1aw\xba\xed\xb7\xb0i\xe5\xa5\x7f|\x8c;\xcd!\xfc\xc5\xb7\xe7\xb8\xddt\x93\xcf\x11\xab\x8c\xc3\x9f\xab\xb0M<!\xfa\x0c\x1d\xfej\xbc\x1e\xf7\xe7\xf3X\x92\xa8s\x8a\x18\x96\n\xaf\x08\r\xc2\x8dYE\xd4\x19\x93\xec\xa6\x00\x19^\x91\x1a\x84\x17\xb3\xba)\x87\xbdJP\x80\x0e\xafh\r\xc2\x8aY%\x14\x1as\xec\xa2@\xc4\xab\xd3\x1e\xf7^-\xc6$:\x07\x19\x0f\xcb\xbb\x9a\xd5E>\xec\x93\xb9\x02\x11\xaf\xee(\xe7Hj\x10\xff\x8a\'\r)\x8b\x83\xb1\xda*\x10\xf1\x8a\xf6apZ\x83\xf8\xf8h<\xe7E\xc3\xb6\x02b\xfb\x9c\x15\xa8\xf0\x8a\xf8u"\xc4\x06\xf1\xfe\x0e/t\xc8\xb9\x075\xcf\x8dt\xf5j2Qr\x83\x00\xb34\xf7\x90Tn\x83\xcb\xf4\x0fM\xd2\xae^\xa53\x88\x8f\x07:`\x96T+\xea\x8c{\x99\xfcc\xe2\x94\x17\x07g5\xa4?\x82\x84\xd1\xe9O\x95t\x96\x1dY5U \xb9A\x92\xe0\x15\xf1u\x90\x19\xb1\xc8\x17\xdb\x9a\x16\x02\xdb\xe9T\xe0\xd6\x9d%M\xac\xfb{\xaf\xea\xd2Jr\x04\xf1\x15fQ\xaf\'\xd4M\x05?\xd7\xab\xc0\x9d;M\x98\\\x9f\xf7^\xd5\xa5\x95\xc8 c\xcc\xea\xf74p]\xea\xf8\xb9\x1d\x05\x92\x1a\xa4\xf3kE\x9b\xe8\x97\xcc >\x19\x156\x99\x16\xb6\xd1\xa5@J\x83\xa4\xc3\xabt\xe7 UuR\xad+\xe8*=\xb2i\xa2@:\x83\xa4\xc4\xab\xc4\x06\x19c\xd6S\x13\xfd\xb0M\xe6\n$3HR\xbcJn\x90\n\xb3n2\xaf=\xa6\xd7@\x81T\x06I\x8bW\xe9\rRa\xd61\xe1\xcd\xc7\rj\x81M\x14*\x90\xc6 \x1c\xdd\x95\xee$\xfd\xa3L\xe9=\xae\xb0\x1f\x90\xd2\x82\x02I\x0c\xc2\xc2\'\xc9\r\xe2\xe3\xeb\xbb\x80Y\x85[&\x85Ax~\xf5\xa67\x88\xef\xf2\xf1\xdd\xc2\xfb)\xbb\xe9\xd3\x1b\x84\x03\xaf\x18\xceA\xc6\x95\xee\xf7\x85\x86\xec\xba\xa5\xc0\t\x91\x1b\x84\x05\xaf\xd8\x0c\xe2{}\xe3\xa7\xc0~\xcan\xca\xd4\x06\xe1\xc1+>\x83\x00\xb3\xb2k\xf9v\x13\xa25\x08\x17^1\x1a\x04\x98\xd5\xae\xa1r\xdb\x9a\xd4 lx\xc5j\x90\x88Y\xee:\xb7\xc2c>\xcd\x14\xa04H\xc4+\xbe\xdb`\x19V\xb1&\x12\xc6\xd5\xac#\\4l\xd6Q\x99mEg\x10N\xbc\xe2=\x82\x8cW\xb3\xb6poVf\xbd\xdfh:d\x06a\xc5+v\x83\x00\xb3\x1auS\x86\x1bQ\x19\x84o\xf5jR\x04F\xc4\x8a!G\x17\xc0\xac\x0c\xfb\xbfvJ4\x06\xe1\xc6+\xfe#H\x88\xf8\x08\xcc\xaam\xa7\xfc6 1\x08;^\x89\x18\xc4\xbfc5+?\x03\xd4\xcd\x88\xc2 \xfcx%c\x10\xef\x81Yu\xfd\x94\xdd\xcf\xfb\x1bD\x02\xaf\xa4\x0c\x02\xcc\xca\xce\x00u\x13\xeam\x10\x11\xbc\x123\x080\xab\xae\xa1r\xfby_\x83\xc8\xe0\x95\x9cA\x80Y\xb99\xa0f>\xfd\x0c"\x85W\x92\x06\xf1\x8f[\xb8hX\x8eKz\x19D\x0c\xafD\r\xe2\xdf\x0fqoV1\x0e\xe9c\x10\xd9W\x102_(\x9c\xeb\x88K\\4,\xc5!\xdd\r"\xfdv5I\x83\xf8\x010\xab\x10\x87t6\x88\xf8\xfb9E\r\x02\xcc*\xc4\x1f\xbe\xabA\xc2\xf7\xca\x84\xdf\xf0,k\x10\xef\x81YEx\xa4\x9bA\xe2\x17/O\x84\x1f\x90\x906\x080\x0b\x06Y\xa5@\xf8f\xf2\xc6\xad\xb4<\xe2\x06\xf1\xefGX\xcd\x92\xee\x82\xe4\xf1\xbb\x1cA\xe4\xf1Jv\x99\xf7\xb3(\xd7X\xcdJ\xde\xa1\xc2\x01\xda\x1bD\x03^i1\x88\x7f\xc2j\x96p\x03\xa7\x0e\xdf\xda *\xf0J\x8dA\xfc0`\xd6e\xea"a|9\x05\xda\x1a$\xe2\xd5\xab\\\xba3\x91\xe5\xcfA\xc6\xc9\x04\xcc:|W\xa1\x08\x92H\xa0@;\x83h\xc1+=G\x90\x90I\xc4\xac\xf4\x1f\x9bOP{\x0c\xd9@\x81V\x06Q\x83W\xaa\x0c\x02\xccj\xd0gf7ic\x10\x1d\xabW\x13\xa9\xb5 \x160\xcbl\xf37I\xbc\xb9A4\xe1\x95\xae#\xc8\x18\xb36\x1f\x9b\xe8\x8dm\x8c)\xd0\xd8 \xaa\xf0J\x9dA*\xcc\xba0V{\xa4\xdb@\x81\xa6\x06\xd1\x85W\xfa\x0cR\xadf\xedc5\xabA\xcb\xd9\xda\xa4\x99A\xb4\xe1\x95F\x83\xf8\xa7m`\x96\xad\xe6o\x92m#\x83\xa8\xc3+\x95\x06\xf1\xc3\xe3\x80Y\xa3&\xaac\x1b3\n41\x88>\xbc\xd2i\x10\xefo6\xdc\xfe\x9b\x99\xda#\xd1\x06\n\xd4\x1bD#^i5H\x85Y\x0f\rd\xc7&V\x14\xa85\x88J\xbcRk\x90\n\xb3\xce\x81YV\xda\xbf>\xcf:\x83\xe8\xc4+\xbd\x06\x01f\xd5\xf7\x9c\xa9-\xd6\x1bD+^i6H\x85Y\xf7\xa6\x9a\x00\xc9\xaeV`\xadA\xd4\xe2\x95j\x83T\x98u\x06\xcc\xca\xc3v\xeb\x0c\xa2\x17\xaft\x1b\xa4\xc2\xac=\x1d\x0f\x05\xe4\xd1\xa5\x82\xb3Xm\x10\xcdx\xa5\xdd \xfei\x17\x98%\xd8\xd5\x84\xa1\x1f\xdd\xd1\xf2\xd1T\xe3\x95z\x83\xf8\xe1\x89s\xa7\xc0,\xc2N\x15\x1aj\xe0\x0e\x97F\xd6\x8dW\xfa\r\xe2\xfd\xad\x9ag/\x85Z+\x8f\xb0\xcb\r\xa2\x1d\xaf,\x18\xc4\xbf\x84\x97#\xdd\xe5\xd1%\x05\xcfb\xa9A\xd4\xe3\x95\t\x83\x00\xb3r\xf0\xd52\x83\xe8\xc7+\x1b\x06\xf1\xde\x86\x929\xf4q\xb29|5\x88\x05\xbc\xb2b\x10o\xe2X\x9c\xac\xb9r\x18\xf8\x8bA\xcc\x94T\xd33\xe9\xab;\xc1\xca\xaf\x9b\x1cz9\xc9\x1c\x16\rb\x07\nl\x18\x04\x98\x95\xa4m\xf9\x06\x9d7\x88\xa5\xdfwV\x0c\xe2E?T\xc7\xd7I\x99F\x9a3\x88\x19\xbc2s\x0eRu\x8d\xe4\xa7N3m[\xbei\xcd\x1a\xc4\x0e^\xd92\x88\xf7r\x1f\xcb\xe6\xeb\xa4L#}\x1a\xc4\x12^Y3\x080\xcb\xac}\xa6\x061\x85W\xe6\x0c\xe2G\xe7\xce\x1d\x0b\x7f\x93\xcbl\x93J&>1\x88-\xbc\xb2g\x10\xef\x1f6\xdd\xf6\x93d\xa9\x11\xbb\x8b\x02c\x83X\xc3+\x8b\x06\xf1o\xfbn\xe3\xa6K\x8d\xb0\x8f\xa0\x02\x95A"^\x99\xbb\xad\xce\xcc2\xef\xb4\xba\xc0,\xc1F\xef\x1a:\x1aD\xcfGq\xda\xcc\xc2\x9eA\x80Ym\xea\xabd\xdb\x81\xfb\xb7\xf0Ig\x8b\x8f\xf6X4\x080KI\xdb7Oc\xe0\xfe\xd9 ^\x99<\x07\x19_4\xc4jV\xf3\xe6\xd4\xb0\xe5\x7f9-\xdf\x1cl\xab\x86\xc9#H\x98$V\xb3\xdaVZp\xfb\xb8z\xb5e\xf4\xc9i\xab\x06\x01f\t6|\xcb\xd0a\xf5\xea_V<\x93\xder$\x81\xcd\xcd\x1a\x04\x98%\xd0-\x9dB\x86\xd5\xab\xbd\xff\x81A:i\xd7o\'`V?\xfdX\xf6\x8exu6Z\xf5V\x13\x96\x14z\x05\xb1{\x04\t\xd3\xc6E\xc3^\xb5\xe7\xd89\xe0U|\x83,\x0c\xc2!\xf6\xd7\x18X\xcd\x92\xd1\xbdq\xd4\x88W\xf1\xe5\x980Hc\xc9\x887\x0c\x98\xb5\x85{\xb3\x88E\xa5\x1an\x8cWq4\x18\x84J\xd3\xd6\xe3\x04\xccr\xd7\xad\xf7\xc2\x0e\x0c\n|\xe0\x15\x0c\xc2\xa0\xf5\xba\x10\x17\xce\x1d\xe1\x16x\xe1",\t?\xc1+\x18D\xba6\x8f\xc0,\xe9\x12,9=\x9c\xe2\x15\x0c"^\x9dw`\x96x\r\x16\x12\x98\xc1+\x18DAq\x80Y\n\x8a0\x93\xc2,^\xc1 \x1aj\x131k\xa0!\x11\xe4\xe0\xfdp\x0e\xaf`\x10\x15=\x111\xebRE&\xc5\'\x11^\xc8\xbf\xf8yI,\xf3*\xe8\x8a\x80Y\x87\xef\n\xf2(=\x85\xf0I\x97/_\xce\x83A4t\xc5`\x0b\x98%^\x87\xf8Q\xb0\xaf\xdf^\x85A\xc4\x0b\x13\x13x?\x04f\t\x17b\t^\xe1\x1cD\xb8&\xb3\xe1/\x81Y\xa2\xd5X\x86W0\x88hI\x16\x82\x07\xcc\xda|\xd4\x94PI\xb9,\xc7+\x18DU\x0fD\xcc\xbaP\x95Q1\xc9\xac\xc0+\x18DY\x07\x04\xcc\xda\xc7j\x16\x7fQV\xe1\x15\x0c\xc2_\x8b\xf5\x11\x81Y\x02\x15Y\x8dW0\x88@9\xd6\x87|?\x02f1\x17e\r^\xc1 \xcc\xb5h\x12\xee\x1a\x98\xd5D&\xb2m\xd6\xe1\x15\x0cB&3\xe1@OX\xcd"T\xb3f\xa8\xf5x\x05\x83\xf0U\xa2E\xa4!0\xab\x85Z\xbd6\xad\xc1+\x18\xa4\x97\xba\xe9v\x06f\xa5\xd3vv\xe4:\xbc\x82Ax\xea\xd0>\n0\xab\xbdf\xad\xf7\xa8\xc7+\x18\xa4\xb5\xa8\\;\x00\xb3\x92+\xdd\x00\xaf`\x90\xe4U\xe8\x1e\x00\x98\xd5]\xbb&{6\xc1+\x18\xa4\x89\x92R\xdb\x00\xb3\x12*?Zzk\xfb\xb2\x80\xb8\xdd=a\x19\xfa\r\r\xcc\xea\xa7\xdf\x9a\xbd\x17^\xcc\xb0.\x0e\x0c\x92\xac\n\xfd\x07\x06f\xf5\xd7p\xd9\x08\x8b/f\x80A\xd2\xe8\x9c~T`V\x02\x8d?_+\xdadp\x1cA\x9a\xa8$\xb6M\x85YF\xbfp$&\xda\xfa\xc0-\xf0*\x0e\xf4\xe2\xf6\x94N\xa4.-\xd3\x9f?\xa8\x9b\xdc\xe7\xcf#f\xbd5\xdf\x1c[\xd6(\xd0\x06\xaf\xe2Pon\xdb\xa8\xa6\x85\x18\xc4G\xccz0Z#ui\xb7\xc3+\x18D]\x01\x97%\x141\xeb\x1c\x98EQ\xab\x96x\x05\x83P\x88\xce0\x060\x8bF\xe4\xb6x\x05\x83\xd0\xe8\x9e~\x94\xa7m`Vo\x95#^\x9d\xb6>\x12\xe3\x1c\xa4\xb7\xf0\x1c\x03\x0c\x8f\x81Y=u\x0e\xf7^m\xdc\xb5\x1f\x03\x06i\xaf\x99\xc8\x1e7\x1bn?~3\x0f\x7f\xba)\x10\xee\xbd\xda\xed\xa2\x1f\x0c\xd2Mo\xfe\xbd"f\x85\xaf\xae\xe2O\x17\x05\xe2\xad\xed\xed\xf1\n\xe7 ]\xb4\x16\xdb\'b\xd6\xd7w\xc7\x8a\xa5c)pG\xbc\x82A,\x159\xe4\xda\xf4\x16mc\xd3J\x9enW\xbc\x82A\x92\x97\x868@\xc3\x87|\x88\xa3\x1a\x1f\xae;^\xc1 \xe6J\xdf\xec1Qs\xd3J\x99p\x0f\xbc\x82AR\x16&\xd1\xd8].v%J\xc5\xc4\xb0}\xf0\n\x061Q\xe2\x85$;\xdc.aq\x9a49\xf7\xc3+\x18\x84\xa6\n\xcc\xa3\xb4\xbf\xe1\x8e9A=\xe1\x08\xce\xd9p\x1dDO9\x1bg\x120\xab\xd3E\xaf\xc6\x012\xd9\x90b\xd5\x0f\x06\xb1\xd8\x0c\x01\xb3\xba\xdc6aq\xaa\xdds\xa6Y\xd0\x80A\xbaW@p\xcfn7\xde\t&\xcc\x1f:\xe2\xd5C\xff\xb00H\x7f\rEF\x88\x98\xf5"\x12\xd9F\xd0\x80W$Ob\xc2 6\xea\xfd5\xcb\x88Y\xb7V\x93O\x9dw\xc4+\x9a\x87\xcc`\x90\xd4\xb5J6~\xc4\xac\x93a\xb2\xe1-\x0fL\x84WX\xe6\xb5\xdc\x04!\xf7\xbbM`\xd6\xb2\x12R\xe1\x15\x0cb\xdc \xfeu\x0f\x98\xf5\xa5\x86tx\x05\x83X7\x88\x1f\x9d\x01\xb3\x16\x8aH\x88W0\x88y\x83x\xff\x00\xcc\x9a\xabb\xbc8H\xf9\x1e1\x9c\xa4[7\xc9\xdb>0kZC\xfa\x87\xca`\x10\xeb\x06\xf1\xa3s`\xd6G\x11\x13<\x96\x0c\x83\x987\x88\xf7\x8f\xc0\xac\xaa\x8a\xe1\xc5\x16{]^\xcc\xb0\xae\x05`\x90\x0c\x0c\xe2\xdf\x81Y\xde\xd3\xe3\x15N\xd2s0\xc7x\x0e\x17\xc5cV\x02\xbc\x82A\xf21H\xc4\xac\xed\xa7\x8c\xe6\xd3v*)\xf0\n\x06i[\x05\xcd\xdbG\xcc\xba\xd1\x9c`\xca\xdc\xd2\xe0\x15\x0c\x92\xb2f\xfcc\x07\xcc:.\xf3\xde\xacDx\x05\x83\xf07q\xd2\x88\xa5bV*\xbc\x82A\x92\xb6\xab\xc0\xe0EbV:\xbc\x82A\x04z8q\xc8\xf20+!^\xc1 \x89\xbbUb\xf8\xc7\xad\xb2V\xb3R\xe2\x15\x0c"\xd1\xc1\xa9c\xbe\x1f\x16\xb4\x9a\x95\x16\xaf`\x90\xd4\xcd*3\xfe\xa5sGe\xacf%\xc6+\x18D\xa6\x81\x93G\x1dl\xb9\xad\x12.\x1a\xa6\xc6+\x18$y\xab\n\x05\x08\x98\xe5\xae\x85b\xb3\x85M\x8fWq*\xefn\x8bmF\xb4\x81J\xf9Nz7\xd5\xf2\xc7,\x06\xbc\xaa\xa4wV\x1b\xcdj\xde\xdd\x1a\xbe\xf5^\xb9c\x16\x07^\xc1 \xad\xdb\xce\xd0\x0eYc\x16\x0f^\xc1 \x86\xfa\xbdC\xaa\xf9b\x16\x17^\x01\xb1:\xb4\x9d\xa1]\x9e2]\xcd\x8a\x9f\xc4\xa6|1\xc3\xda\x92\xe2\x1c\xc4P\xc7\xb7Mux\xe4\xdce\xdb\x9d\xb4o\x1f\xf1\x8a\xe6\xb5\xa2\x8df\n\x834\x92\xc9\xeaF\xd7\xce\x1d\xbe[M~i\xde\x11\xaf\x1e\x18g\x04\x830\x8a-\x10*b\xd6@ n\xaa\x90\xacx\x85s\x90TeT4nV\x98\xc5\x8cW0\x88\xa2FN\x97J>\x98\xc5\x8dW0H\xba\xae\xd44r.\x98\xc5\x8eW0\x88\xa66N\x98K\x16\x98%\x80W0H\xc2\xa6\xd45\xf4\xf5\x86\xf5\xd5,\t\xbc\x82Atuq\xcalB\x7fm=\xa6\x0c\x90x\xecp"\xc5wqpv.X\xe6M\\Y-\xc3GB\xb9\xd0\x92L\xdb<"#2^\x1c\x84A\xda\x16(\x8b\xed\xe39\xae\xcd\x8b\x86a\x95\x81\xf5\xe2 \x0c\x92E\xc3\xb7\x9eD\xc4x\x8b\x98%\x86W8\x07i\xddc\xb6w0\x89Y\x82x\x05\x83\xd8\xee\xf7\x0e\xd9\xdb\xc3,I\xbc\x82A:\xb4\x98\xf1]\xaca\x96(^\xc1 \xc6\xbb\xbdK\xfa\xa60K\x18\xaf`\x90.\x1df~\x9f\xf0!X\x99K\n\xad\x95\x93\xc6+\x18\xa4u\xc9\xb2\xd8\x81\xf8S\xe2\xc94\x11\xc7+\x18$Ymu\x0f<<\x11\xbb\xee\xd6\\\x18\x05x\x05\x834/Wf[\xea\xc7,\rx\x05\x83d\xd6\xf6-\xa6\xa3\x1d\xb3T\xe0\x15\x0c\xd2\xa2\xa3r\xdbT5f)\xc1+\x18$\xb7\xaeo5\x1f\xbd\x98\xa5\x05\xaf`\x90V\r\x95\xdd\xc6Z1K\r^\xc1 \xd9\xf5|\xbb\t\xa9\xc4,Ex\x05\x83\xb4\xeb\xa7\x0c\xb7\xbe\xdbp{\xaf\xaa\xe6\xa5\t\xaf`\x10U\xad!\x92\xcc\xeb\xae\xdb\xbc\x17\x89\xbc<\xa8*\xbc\x82A\x14u\x86T*\xa3S\xe7\xceFR\xd1\x17\xe2*\xc3+\x18DI_\xc8\xa6\xa1\x07\xb3\xb4\xe1\x15\x0c"\xdb\x99Z\xa2k\xc1,ux\x05\x83hiQ\xe1<T`\x96B\xbc\x82A\x84\x1bSOxy\xcc\xd2\x88W0\x88\x9e\x0e\x95\xceD\x1a\xb3T\xe2\x15\x0c"\xdd\x96\x8a\xe2G\xcc:\x95Z\xcdR\x8aW0\x88\xa2\x06\x95O\xe5~\xd3\xed\xca\\4\xd4\x8aW0\x88|Wj\xca\xe0u\xcfm\xdc\t$\xa4\x16\xaf`\x10\x81n\xd0\x1crt&\x80Y\xef\xe1\xb5\xa2\x8a\xdf\x89\x8aw\xf3j\xeeX\xf6\xdc\xf81k\x10^+\xaa\xf9u\x8f0\x08{\x13\xaa\x0e\xc8\x8dY\xe1c\xee\xba_\x18\x0c\x83\xa8\xeeW\xfe\xe4X1\xeb\xfdP5^\xe1\x1c\x84\xbf\xff\x0cD\xe4\xc3,\xedx\x05\x83\x18hW\x81\x14#f\xdd2\xc4U\x8fW0\x08C\x17X\x0c1:w\xeed\x988s\x03x\x05\x83$\xee\x01\xbb\xc3?\x84\x8b\x86/I\xd3\xb7\x80W0H\xd2\x160=\xf8\xdb~Z\xcc2\x81W0\x88\xe9\x1eN\x9b|R\xcc2\x82W0H\xda\x1e3>z:\xcc\xb2\x82W0\x88\xf1\x16N\x9c~*\xcc2\x83W0H\xe2\x0e\xb3>|\x12\xcc2\x84W0\x88\xf5\x0eN\x9e\x7f\xc4\xac\'\xd2(\x96\xf0\n\x06!-}\x96\x83E\xcc\xba!\x9c\x99)\xbc\x82A\x08+\x9f\xedP\x17\xce\x1dS]44\x86W0H\xb6]M9\xb1\xc7M\xb7M\x83Y\xd6\xf0\n\x06\xa1\xec\xa3|\xc7z\'\xc2,sx\x05\x83\xe4\xdb\xd4\xb43\xa3\xc0,\x83x\x05\x83\xd0\xb6Q\xc6\xa3\xf5\xc7,\x8bx\x15\x0b\xba\xed\xdel\xd6\xd5\xd9L\xdbj\xd6}1\xcb$^\xc1 V\xdbU"\xef\x80YG]W\xb3\x8c\xe2\x15\x0c"\xd1hfc\x06\xcc\xda\xea\xb6\x9ae\x15\xaf`\x10\xb3\xcd*\x92x\xc0,w\xdd!\xb2Y\xbc\x82A:T\xbb\xe8]B\xab\xb7\xc6,\xc3x\x05\x83\x14\xdd\xed]&\x1f`\xa9%fY\xc6+\x18\xa4K\x8f\x94\xbdO<\x1e\xb4\xc1,\xd3x\x05\x83\x94\xdd\xec\xddf\xdf\x06\xb3\x8c\xe3\x15\x0c\xd2\xadE\n\xdf\xab9fY\xc7+\x18\xa4\xf0V\xef8\xfd\xa6\x98\x15\xae\x9c\xe8~\xadh\x93\xf9\xe3Jz\x13\x95\xb0\xcd\xbc\x02\x01\xb3\x0e\xdfkD\x89\x8b\xc2\x8a\xdf\xda\xde\xb4\xa40HS\xa5\xb0\xdd\x8c\x02\x11\xb3\x06k\x15\t\x97\x15U\xbf\xb5\xbdi9a\x90\xa6Ja\xbbY\x05\xe2W=.\xd7H\x92\x05^\xe1\x1c\x04M\xdf]\x81\xf0]\xa8\x95\x98\x95\t^\xc1 \xdd\xdb\x03{\xfa\xf0e\xc1\x15\x98\x95\x0b^\xc1 h\xf3>\n\xc4o\xd3.\xc3\xacl\xf0\n\x06\xe9\xd3\x1e\xd8\xd7\xfbe\x98\x15\xf1j\xdd\xd9\x891\xddp\x92n\xac`\xba\xd2\x8d\x985\xff\x85\xc1xS\xfc\xfa\xf5-]3\xa8\xcb\x06\x06\xa9S\x08?_\xa7@\xc4\xac\xd9\xab\x1d\x01\xafj\xaf\x90\x98R\x14\x061U.\x85\xc9\xc6\xaf\x9cO.\x1af\x86W8\x07Q\xd8o\xf6R\n\x98\xf5qI07\xbc\x82A\xecu\xa3\xc6\x8c\x87\xc7c\xcc\xca\x0e\xaf`\x10\x8d\xedf1\xa7\x9b\r\xb7\xff\xbfy\xad^M\xca\x80s\x10\x8b\r\xa9.\xe7\xa7m\xf7Oy\xad^\xc1 \xea\x9a\xcctB\xe1\xbb\xb8\xee?M\xcf`E\xf28\x82\xe4XU\xee9\xc5\xd5\xab\x7f\x0f\x98Uw\x0b<w^\x04\xf1`\x10\x02\x11K\x1fb\xbcz\x150k\xf3!;)`\x90\xecJ\xca>\xa1\xc9\xeaU\\\xcd:\x1f\xb1\x87O\x1b\x10\x06I\xabo\xfe\xa3\xcf^\x1c\x8c\xabYF\xdf\xf5\xbc\xaaP0H\xfe-\x9ct\x86\xf3\x17\x07\x9fvs\xc3,\x18$i\xfbd?\xf8\xe2\xc5\xc1\xe1If\x98\x05\x83d\xdf\xc3\t\'\xb8\xec\xde\xab\xdb\xbc0\x0b\x06I\xd8?\xb9\x0f\xbd\xfc\xde\xab\x97\xac0\x0b\x06\xc9\xbd\x8b\xd3\xcdo\xd5\xbdWYa\x16\x0c\x92\xae\x81\xf2\x1ey\xdd\xad\xed\x01\xb3\xf6^\xf3\x98>\x0c\x92G\x1d\xd9g\xb1\xfe\xd6\xf6\x88Y\xf7\xec9\xa5\x08\x08\x83\xa4P5\xff1\xebnm\x8f\x98u\x96\xc3EC\x18$\xfff\xa6\x9fa\x93\'\x073\xc1,\x18\x84\xbe}\xb2\x1f\xf1\xa1\xd1\x8b\x19\xf2\xc0,\x18$\xfbv\xa6\x9e\xe0(\xdc\xda\xde\xe8\xc5\x0c\xa3\xd3\x0c0\x0b\x06\xa1\xee\x9f\xdc\xc7{k\xf1\xe4\xe0\x9d\xfd\xd5,\x18$\xf7\x86&\x9e_3\xbc\x9a\x04}5\xbf\x9a\x05\x83\x107P\xde\xc35\xc6\xab\x89\x0c\x11\xb3N-\xaff\xc1 yw4\xed\xec\xda\xe0\xd5$r\xc0\xac]\xc3\x17\ra\x10\xda\x16\xcaz\xb4vx5\x83Y\x1bwfu\x81A\xcc\x96\x8e;\xf1\xd6x\x95\x05f\xc1 \xdc}f5^\x17\xbc\xca\x00\xb3`\x10\xab\r\xcb\x9cw7\xbc\x9ab\xd6\x9e3\x8aY0\x08s\xa3\xd9\x0c\xd7\x19\xaf\xa6\x98uft5\x0b\x06\xb1\xd9\xb1\xbcY\xf7\xc1\xabI\xa6\xf7\x9b&W\xb3`\x10\xdeV3\x19\xad\x1f^\xd9\xc6,\x18\xc4d\xcbr&\xdd\x1b\xaff1\xebd\xc8\x99:A,\x18\x84@\xc4\xac\x87\x88xuM4\xc3\x88Y/Dc1\r\x03\x830\tm5L\xc4\xab\'\xb2\xe4_\xc3j\xd6-\xd9h\x1c\x03\xc1 \x1c*\x9b\x8d\x11\xf1\xea\x88\x92\x8aFa5\xcb\x14f\xc1 f\x9b\x97!qJ\xbc\x9a]\xcd2\x84Y0\x08C\x9fY\rA\x8bW\x13\x15\x82\xeb\x0ca\x16\x0cb\xb5{\x93\xe7M\x8eW\xd3\xd5\xac\xc0mf0\x0b\x06I\xdehF\x03\xa4\xc0\xab\x89\x14\xe1\xd0\xb4Kw\xe6\x9fT`\x18$\xa9\xbcv\x07O\x83W\xb3\x98ucB\x9c=g\xe8\x84iVQgB^\xabI&\xc3\xabY\xcc:\xa6\\\x1eK\xa5\xf4\xa1\x1b\xa4\x1a:\xed\xb80HB}S\xe2\xd5\x0cfm\x1b\xc0,\x18$a\x9fY\x1d:-^\xd9\xc2,\x18\xc4j\x17\'\xcb;9^\x99\xc2,\x18$Y\xa3\x19\x1d\x98\x03\xaf&\xd2\x847`k\xc7,\x18\xc4h\x1f\xa7J\x9b\x07\xaf&\xd9\x87\x97\xfcn\xe8^\xcd\x82ARu\x9a\xc9q\xe3\xadR\xa4\xf7^\xd5\xaa\x10^\x13\xafz5\x0b\x06\xa9-aA\x1b\x84\x9bm\xc9nmo*[\xfc\xd0\x88\xe2\xd5,\x18\xa4i!\x0b\xd8.<\xae!\xd0\xab\xf1[\nT\x0f\x9c\xd0\x17\t\x06\xa1\xd7\xd4\xe8\x88\xfcx5\x11*`\x16/\xd7\xb5\xa8\x10\x0c\xd2B\xac\xac7\x95\xc0\xab\x99\xd5,\x81CW\xa3r\xc2 \x8dd\xca\x7f#\x19\xbc\x9aY\xcdR\x8aY0H\xfe\xbd\xdf`\x86rx\xa5\x1d\xb3`\x90\x06\xed\x93\xfd&\x92x5\xc5\xac-\x89\x15\x82\xda\xd2\xc2 \xb5\x12\xe5\xbf\x81,^M1\xebP\xe3j\x16\x0c\x92\x7f\xff\xd7\xccP\x1e\xaf&\t^6\xfc\xf8!g\xc9`\x10N\xb55\xc6\xd2\x80W\x13]\x06\x01\xb3\x94=~\x01\x83hlZ\xc6\x9ct\xe0\xd5,f]2\xce\xbe>\x14\x0cR\xafQ\xc6[\xe8\xc1+\xad\x98\x05\x83d\xdc\xfe\xb5S\xd3\x84WJ1\x0b\x06\xa9\xed\xa2|7\xd0\x85W:1\x0b\x06\xc9\xb7\xff\xcd\xac^-&\xaai5\x0b\x06)\xd5 \x1a\xf1jR\x8b\'=\xabY0H\xa1\x06\xd1\x89W\x93b\x0c\x8f\x9c\xbbPQ\x19\x18DE\x19\xb8\x93\xd0\xb7z\xb5\xa8\xc0\xb5s\xfb\xef\xdc\xb2,\x89\x07\x83((\x02{\n\x9a\xf1j\x06\xb36\x1f\xd9\x95\xf9\x12\x10\x06\x91\xaf\x01{\x06\xba\xf1J\x17f\xc1 \xec\xed)\x1dP?^M\x14\xd2\x80Y0\x88t\xbfr\xc7\x8f_A\xd3\xfb\x08\xf8\xbc\x1aa5K\x1a\xb3`\x10\xee\x06\x15\x8e\x17\xf0J\xfb\xbb\xdaf\x14\x92_\xcd\x82A\x84\x1b\x967|\xc4+\xd5\xaf\xa1\xfa"\xc7\xf5\x86\xecj\x16\x0c\xc2\xdb\xa1\xb2\xd1"^\xe9~\x91\xe1W}\x9e\xb6\xdd\xe6\x83\x9cl0\x88\x9c\xf6\xec\x91m\xe1\xd5t5\xeb\xd8\xb9\xf3\x11\xbbX\x1f\x01a\x10)\xe5\xd9\xe3\xda\xc3\xab\x89D7\x01\xb3\xde\xd8\xf5\x1a\x07\x84A\x84\x84g\x0fk\x11\xaf&"\tb\x16\x0c\xc2\xde\xa92\x01\xef6,\xad^-j4\x14\xc3,\x18D\xa6_\x99\xa3\x8eN\xad\xad^-\n$\x85Y0\x08s\xab\x8a\x84{\xdd\xb5\xb7z\xb5(\x94\x10f\xc1 "\x1d\xcb\x1b\xd46^\xc9\xaef\xc1 \xbc\xbd*\x10\xcd>^MD\xbb\r\xabY\xaf\xcc\n\xc2 \xcc\x82\xb3\x87\xcb\x01\xaf&\xa2\xbd\xec\xba\xcd{^\x05a\x10^\xbd\xd9\xa3\xe5\x81WS\xcc:q\xee\x8c\xf5\xa2!\x0c\xc2\xde\xb2\x9c\x01\xf3\xc1\xab\x19\xcc\xda\xe3\xc4,\x18\x84\xb3_\xb9c\xe5\x84WB\x98\x05\x83p7-c\xbc\xbc\xf0J\x06\xb3`\x10\xc6\x86\xe5\r\x95\x1f^I`\x16\x0c\xc2\xdb\xb5|\xd1r\xc4+\x01\xcc\x82A\xf8Z\x965R\x9ex5\x8bY\xa7,\xabY0\x08k\xdbr\x05\xcb\x17\xaf&\n\x86_\x00\xbb\x1c\xabY0\x08W\xcfr\xc6\xc9\x19\xaf&:\xc69\xde\xa5\x17\x15\x06I\xaf1{\x84\xbc\xf1j"g<J\xa6\xc7,\x18\x84\xbd}S\x07\xcc\x1f\xaf81\x0b\x06I\xdd\xaf\xdc\xe3\x97\x80W\x8c\x98\x05\x83p7p\xe2xe\xe0\x15\x1ff\xc1 \x89\x1b\x96w\xf8r\xf0\x8a\x0b\xb3`\x10\xde\x0eN\x1b\xad$\xbcb\xc2,\x18$m\xcb\xb2\x8e^\x16^\xcdb\xd6\xc90\x95\xd00H*e\xd9\xc7-\x0f\xaf&\x12\x87\x17\xe2\xed\xbe$\xd2\x1b\x06I$,\xfb\xb0%\xe2\xd5\x14\xb3\xc2+Uo\xd3(\x0e\x83\xa4\xd1\x95}\xd42\xf1j\x8aY\xe1\xa5\xdci0\x0b\x06ao\xe5\x14\x01\xcb\xc5\xab\xd4\x98u\xe2\x98\x1f\x82\xa7j\x0fG5P\x0e\xe3\x94\x8cW\x891\xeb\xd41\xdc\xf0\x95\xa2\x07a\x90OU\xcb\xc6\xab\xb4\x98\x05\x83\xa4p/\xeb\x98\xc0\xab\x94\x98\x05\x83\xb06s\x82`\xc0\xabOQ\x13\xbc\xc1\x1e\x06I\xd0\xb3\x9cC\xc6\x07\x87R]\x03\xe0\x9c\x07M,\xfao\xa0\xc0 4\x95\x11\x1a%\xe2U\x9a\xe5M\xa1\t\xf5\x0eK\xfd\x15-\x18\xa4wI\x04\x07\x88x\x95\xe8\x02\x99\xe0\xac\xfa\x85\x0e\x98\xe5\x08?s\r\x83\xf4+\x87\xe8\xde)o\xb1\x10\x9dX\xaf\xe0\x11\xb3\x8e\xc8\xee\xcd\x82Az\x15Cr\xe7\xd8\x08\xc0\xabe\x15\x08\xbf8\xb6\x9e\x88J\x03\x83\x10\t\xc9>L\\\xb1\x01^-\x97\x9d\x10\xb3`\x10\xf6\xce\xa6\tx\x97\xf0\x0eV\x9a\x0c%G\xa1\xc3,\x18D\xb2\x8e\x9dcc\xf5\xaaN\xba\x07"\xcc\x82A\xea\x94\xd6\xf8s\xac^\xd5W\xe5m\x9fd5\x0b\x06\xa9\x97Z\xdd\x16\xb88\xd8\xa4$\xa3s\x8a/\xfb\xc2 M\xb4V\xb5\xcd0|e)\xfd\x0b\xd3TM\xb9c2\x8f\x9b\xfd\xbf\r\x0f\x83t\x14_l\xb7\xf0\x9d>\x8eWn\x8a\xcd\x8f2\xf0\xfb~\xef\xcf_\xc3 \x94\x05a\x18+|\xe9\x95\xe5\xa5\xcd\x0cS\xe1\x08q\xd1\x17\xb3`\x10\x8e2\x91\xc5\x18\x01\xafZj\xf9\xb8\xd5\xef\xa2!\x0c\xd2Rp\xd1\xcd\x99\xdeh.:G\xea\xe0\xef\x87\xbdV\xb3`\x10\xea\x82$\x1c\x8f\xeb\x9b\x18\t\xa7 1\xf4e\xb87\xeb\xbdk`\x18\xa4\xabr\xec\xfb\xf1\xbc\xee\x9f}Z\x0c\x01\x07\x01\xb3\x06\x1d\xe3\xc0 \x1d\x85c\xdf\rx\xd5]\xf2\x88Y\x97\xddv\x87A\xba\xe9\xc6\xbe\x17\xf0\xaa\x97\xe4\x01\xb3\x0e;a\x16\x0c\xd2Kw\xae\x9d\x81W}\x95\xee\x8aY0H_\xe59\xf6\x07^\xf5W\xb9#f\xc1 \xfd\xa5O>\x02\xf0\x8aD\xe2N\x98\x05\x83\x90h\x9fr\x10\xe0\x15\x95\xba]0\x0b\x06\xa1R?\xd58\xc0+:e\xdf\x8fZ\xaff\xc1 t\xf2\'\x19\txE*\xebu\xdb\xd5,\x18\x84T\x7f\xea\xc1pk;\xb5\xa2O-/\x1a\xc2 \xd4\x15\xa0\x1c\x0f\xb7\xb6S\xaa9\x1ek\xd8\x0e\xb3`\x10\xfa\x12\x90\x8d\x88[\xdb\xc9\xa4\x9c\x1d\xa8\x15f\xc1 Ij@1(\xf0\x8aB\xc5ec\xb4\xc1,\x18$U\x15\xfa\x8e\x0b\xbc\xea\xab\xe0\xea\xfd\x87\xc7\x8dW\xb3`\x90te\xe852\xf0\xaa\x97|u;\xdfl\xb8\xfdF\xf7f\xc1 uR\x8a\xfc\x1cx\x95Z\xf6\xa7m\xb7\xf9\xd8 \x08\x0c\xd2@$\xf6M\x80W\xe9%\x8f\x98uQ\x1f\x06\x06\xa9\xd7\x88}\x0b\xe0\x15\x8b\xe4\x11\xb3\xde\xea"\xc1 u\n\xb1\xff\x1cx\xc5%y8Po>\xd4\x04\x83A\xb8\xaa\xd14\x0e\xf0\xaa\xa9R\xfd\xb7\x8b\xbf\x8b\xceGk\xc7\x81A\xfa\xcbL:\x02\xf0\x8aT\xce\xba\xc1\x82\xdc\xfb\xaf\xeb6\x82A\xea$d\xfd9\xf0\x8aU\xee\x10,b\xd6\xfd\x9a\xa00\x08wE\xd6\xc5\x03^\xf1W#\xfeN:[\x8dY0\x08\x7fIVF\x04^\x89\x14c\xad\xec0\x88HM\x96\x05\x05^I\x95b\xdd\x81\x1b\x06\x91\xaa\xcab\xdc:\x18\xd6\x92g\x8ey\xac\xf9\xdd\x04\x83()x8\xce\xef\xad]NQ\x92g\xa6i\xac\xc4,\x18DE\xc5k\xce\x14U\xe4\x98w\x12\xab0\x0b\x06\xd1Pw\xe0\x95|\x15V\xbc<\x06\x06\x91/\x8d\x07^)(\x82\xf7K\xdf\x8f\x01\x83\x88\xd7&~\x14g\xcdB\xbcx~\xe5$\xb0\xec\rK0\x88t\xfdCU\xd6^\xca\x95\xce\xaf\xa4\xf8K0\x0b\x06\x11n\x80p\\\xc7\xea\x95p\rf\xc2\x7f\xc1,\x18D\xb48\xf1W\x16\xf0J\xb4\x04\x0b\xc1_\xf7\xe6?"\x0c\x83HV\x07x%\xa9\xfe\xf2\xd8\xa3\xb3\xb9\xcf\xd0\xc3 \x82%\x02^\t\x8a\xbf:\xf4\xfd\xe6\xcc\x97\xb6a\x10\xb1\x1a\x01\xaf\xc4\xa4\xaf\t<\x8bY0\x88T\x95\x80WR\xca\xd7\xc7\x9d\xc1,\x18\xa4^\xae$[\x04\xbcZ\xff([\x92\xa8\x18\xb4\xa1\x02S\xcc\x82A\x1a*F\xbbY\xc4\xab\x9a\x87\xa1i\x03b\xb4\x96\nL0\x0b\x06i)\x1c\xc9\xe6\x11\xaf\x1eHF\xc2 \xa9\x14\xa80k\xe8a\x90T\x02\xaf\x197\xe2U\xed\x0b\x99\x04\xf2B\xc89\x05"f\xbd\xc0 \xec]\x01\xbcb\x97\xbcc\xc0\x88Y\xff\xdf\xddu\xdc[x7\'\x1c\xbfsx\xe0Ug\xe9\xd8w\x8c\x98\xe5\xfe\x9b=,I@\xab\x06\x01^\x91\x94\x9fk\x90\xfb\r\xf7\xff^\xb8\x82\x91\xc6\xb1i\x10\xe0\x15i\x130\x0c\xf6\x1f\xcem\xdc2\xc4!\x0fa\xd2 \xc0+\xf2>H=\xe0\xa5\xfbW\xe7\x8e\x87\xa9\xc3\xd0\x8fo\xd1 \xc0+\xfa>H=\xe2\xa5\xbb\x0c\xabY\xdbO\xa9\xe3\x90\x8fo\xcf \xc0+\xf2&`\x180\x18\xc4\xc7\xd5\xac\x1b\x86X\xa4!\xcc\x19\x04xEZ\x7f\xae\xc1\xa2A|\\\xcd\xb2\x86Y\xd6\x0c\x02\xbc\xe2ji\xda8\x95A\xbc\xb7\x87Y\xb6\x0c2\xc4\xbdW\xb4}\xcb6\xda\x87A\xeca\x96)\x834\xf9\x94\x11[\xc9\x11\xa8\x8d\x02\x13\x83T\x98udh5\xcb\x92A\xe2WZp\xefU\x9b\xb6\xd4\xb3\xed\xd4 \x15fm\xd9Y\xcd\xb2c\x90\x06\xdf\xf9\xd2\xd3\x0f\xc8dA\x81\x19\x83D\xccr\xd7V\x142c\x10\xe0\x95\x95\x96Z\x9a\xe7\xacALa\x96\x15\x83\x00\xafL\xfb\xc3\xcf\x19\xc4\x12f\xd90\x08\xf0\xca\xb6=\xfc\xa2A\xec`\x96\t\x83\xe0\xad\xed\xd6\xfd\xf1\xc5 f0\xcb\x82An\xf0Z\xd1\xfc\x0c2\xc6\xac\x81\xfa\x89\xe97\xc8\xf0\x18\xaf\x15U\xdfF\xb5\t.\x9c\x83T\xdb\xc7\xd5\xac\xea\xfa\xba\xe6?\xea\r\xf2\xb4\x8d\xb7\xb6kn\xa0\x86\xb9-3\x88\x1f\x9d;w\xf8\xdep\x04\xa1\xcd\xb4\x1b\x04x%\xd4\x18\xc4a\x97\x1a\xc4\xfb\x07\xf5\x98\xa5\xdb \xc0+\xe2>\x15\x1bn\x85A\xfc\xdb\xber\xccRm\x10\xe0\x95XCS\x07^e\x10\xf5\x98\xa5\xd9 \xc0+\xea6\x95\x1bo\xa5A\xb4c\x96^\x83\x00\xaf\xe4\xda\x99>\xf2\x1a\x83\xe8\xc6,\xb5\x06\x01^\xd1w\xa9\xe0\x88\xeb\x0cRa\xd6\xbe\xd2\xd5,\xad\x06\x01^\tvs\x82\xd0k\r\xe2\xfd\xe3\xa6\xdb|L\x10\xb6\xff\x90:\r\x02\xbc\xea_Y]#\xd4\x18\xc4\xbf\x87\xd5\xac\x0b])\x8f\xb3Qi\x10\xe0\x95\xc6V\xe9\x95S\x9dA\xbc\xbf\xd0\x89Y\x1a\r\x02\xbc\xea\xd5\x8b*w\xae7\x88R\xcc\xd2g\x10\xe0\x95\xca\x0e\xef\x99T\x03\x83\xe8\xc4,u\x06\x01^\xf5lE\x9d\xbb71\x88J\xcc\xd2f\x10\xe0\x95\xce\x06\xef\x9bU3\x83(\xc4,]\x06\x01^\xf5mD\xad\xfb74\x88>\xccRe\x10\xe0\x95\xd6\xfe\xee\x9dWS\x83\xa8\xc3,M\x06\x01^\xf5\xeeC\xb5\x0347\x882\xcc\xd2c\x10\xe0\x95\xda\xee&H\xac\x85Ata\x96\x1a\x83\x00\xaf\x08\xdaP\xef\x10m\x0c\xa2\n\xb3\xb4\x18\x04x\xa5\xb7\xb9)2kg\x10E\x98\xa5\xc3 \xc0+\x8a&\xd4<FK\x83\xe8\xc1,\x15\x06\x01^i\xeem\x92\xdc\xda\x1aD\rfi0H\xc0+\xbc\xb5\x9d\xa4\r\xf5\x0e\xd2\xde ~\xb0\xa5\xe1\x16xy\x83D\xbc:\x1f\xe9--2\xa3P\xa0\x83A\xfc\xfb\xa1\x82[\xe0\xc5\r\x12\xf1\xea\x81\xa2\x04\x18C\xb3\x02]\x0c\x12\xdf\xe8+\xfe\xa4\xa1\xb4A\xae\x83\x04\xf8(\x8e\xe6\xd6\xa6\xc9\xad\x9bA\x14`\x96\xacA\x86G\xc0+\x9a\x06\xd4>JG\x83\xf8\xd8!\xa2O\x1a\x8a\x1a\xe4)\x9c\x86\x01\xaf\xb4\xf76I~]\r\xe2}d\x0c\xc1\x17:H\x1a\x04xE\xd2{&\x06\xe9n\x10\x1f\x7f\x8d\xca\xbd\xd0A\xce \xc0+\x13\x9dM\x94d\x0f\x83\xc8b\x96\x98A\x80WD\xadgc\x98>\x06\xf1>^)\x13\xc2,)\x83\x00\xafl46U\x96\xfd\x0c\xe2\xe3\xc5\x00\x19\xcc\x921\x08\xf0\x8a\xaa\xf1\xac\x8c\xd3\xd3 >^N\x16Y\xcd\x121\x08\xf0\xcaJ_\x93\xe5\xd9\xd7 b\x98%a\x10\xe0\x15Y\xdf\x99\x19\xa8\xbfA|\xfc\x94+?f\xf1\x1b\x04xe\xa6\xab\t\x13%0\x88\x17\xf9\x188\xbbA\x80W\x84mgg(\n\x83x\x7f\x1bV\xb3^y\'\xcdm\x10\xe0\x15o}\xb5D\xa31H\x85Y\xf7\xacs\xe25\x08\xf0\x8a\xb5\xb8\x8a\x82\r.i>\x89\x1e1\xeb\x8c\xf3\xe1\x08V\x83\x00\xaf\x14\xb5\xac\xd5T\xee6\xdc.#fq\x1a\x04xe\xb5)U\xe5\xfd\xba\xeb6\xee\xd82\xe23\x08\xf0\x8a\xad\xa8\x99\x07\x1a\x9d:w:d\x9a$\x9bA\x80WL\x15-!L\xc4\xac\x17\x9e\x89r\x19\x04x\xc5S\xcfB\xa2D\xcc\xbae\x99+\x8fA\x80W,\xc5,(H\xc4\xac\x13\x0e\xccb1\x08\xf0\xaa\xa0\xd6\xe5\x9a*\x13fq\x18\x04x\xc5\xd54E\xc5\xe1\xc1\xac\xf4\x06\x01^\x15\xd5\xb6\x8c\x93e\xc1\xac\xe4\x06\x89\xef\xc7{`T\r\xa1\nR\x80\x01\xb3R\x1b$\xbe\xfa\x0b\xef\xbd*\xa8gy\xa7\x9a\x1e\xb3\xd2\x1a$\xbe<\x12\xaf\x15\xe5\xed\x99\xb2\xa2\x8d\xce\x12\xaff%5\x08\xf0\xaa\xacn\x15\x99\xed\xfdf\xd2\x8b\x86)\r\x02\xbc\x12\xe9\x98\xd2\x82\xbe\xee\xa5\xbch\x98\xce \xc0\xab\xd2:Uj\xbe\xa3\xf3\x84\x98\x95\xcc \xc0+\xa9~)0\xeeC:\xccJe\x10\xe0U\x81}*7\xe5\xb7\xfdT\x98\x95\xc6 \xc0+\xb9^)3r2\xccJb\x10\xe0U\x99]*:\xeb\x88YO\xf4\x19\xa40\x08\xf0\x8a\xbeN\x18\xb1V\x81\x88Y7\xb5[\xb5\xdd\x80\xde \xc0\xab\xb65\xc0\xf64\nD\xcc:\xa6\xbe\x05\x9e\xdc \xc0+\x9ajc\x94\x0e\n\x04\xcc\xda&\xc6,j\x83(\xf8\xecb\x07a\xb1K&\nD\xcc\xba&\x9d\x0b\xadA\xc4\xbf(G\xaa\r\x06\xb3\xa7@\xc4\xac#J\xcc"5\x88\xec\xc7\xb2\xecU\x13\x19\'P `\xd6\x16!fQ\x1aD\xf8s\x8b\t\xc4\xc6\x90\x06\x15\x08\x98\xe5\xe80\x8b\xce \xc0+\x83\xcd\x94e\xca\xa3\x8b\x80YT_l#3\x08\xf0*\xcbf\xb39\xa9\xc7\x80Y4\xef\x02\xf6T\x06\x01^\xd9l\xa5L\xb3~\x0f\x98uI27\x1a\x83\x00\xafH\x8a\x81A\xe8\x14\x08\x98uH\x81Y$\x06\x01^\xd1\x15\x16#\x11)@\x84Y\x14\x06\x01^\x11\xd5\x14\xc3P*@\x83Y\xfd\r\x02\xbc\xa2\xac*\xc6"T\x80\x02\xb3z\x1b\x04xEXQ\x0cE\xab\x00\x01f\xf55H\xc0+\x92s!Za0\x1a\x14\xa8\x14\xe8\x8fY\xfd\x0c\x12\xf1\x8af5\r\x05\x85\x02I\x14\xe8{\xd1\xb0\x97A\x02^Q]\x8fI"\x0e\x06\x85\x02\xbe\'f\xf51\x08\xf0\n\xfdg@\x81~\x98\xd5\xdd \xc0+\x03\xcd\x81\x14\xa3\x02}V\xb3:\x1b$<9\x08\xbcB\xff\xd9P 6\xebc\xb7T\xbb\x1a$<9\x88\xd5\xabn\x92c/~\x05\xe2\x8b\x12.:\x85\xedf\x90\x18\x0f\xabW\x9d\x04\xc7N2\nt}\x16\xbc\x93A\x80W2EF\xd4\x1e\n\xc4\xb7\x89t\xc0\xac.\x06\xc1\xeaU\x8f:aW)\x05\xba\xad*\xb57H\xb78R\xaa .\x14\x98*\xd0\xe57{k\x83\xe0\xe2 :\xce\xac\x02\x1d\x9a\xb7\xadA\xba\x98\xd0\xac\x9eH<7\x05\xda\xe3O;\x83\xb4\x1f?7\x851\x1f\xe3\n\xb4\xfd\r\xdf\xca \x1d\x8eP\xc6\xe5D\xfa\xd9)\xd0\xb2\x89\xdb\x18\x04\x17\x07\xb3\xeb\x96\x12\'\xd4\xee\t\xbf\xe6\x06\xc1\xc5\xc1\x12\xbb)\xcb9\xb7yF\xbc\xb1A\x1eq\xefU\x96\xcdR\xe4\xa4\xe2c\xb0\x0f\xcdf\xde\xd4 }n\x88l\x96\t\xb6\x82\x02l\nD\xcc:\x1f5\t\xd7\xcc \xfdn\xa9o\x92\x07\xb6\x81\x02\xac\nD\xcczk\x10\xb1\x91Az>\x94\xd5 \rl\x02\x05\x98\x15x\xdan\x84YM\x0c\x02\xbcb\xae\x1d\xc2q(0<n\x82Y\xf5\x06\x01^qT\x0b1\x04\x14\xb8\xd9\xa8\xc7\xacZ\x83\x00\xaf\x04*\x87\x90<\n<\xed\xd6bV\x9dA\x80W<\xa5B\x14\x11\x05\x86\'u\x98\xb5\xde \xc0+\x91\xb2!(\x9f\x02\xb75\x98\xb5\xd6 \xc0+\xbeB!\x92\x90\x02/\xeb1k\x9dA\x80WB5CXN\x05\xd6c\xd6j\x83\x00\xaf8\xab\x84X\x82\n\xac\xc3\xac\x95\x06\x01^\tV\x0c\xa1y\x15X\x83Y\xab\x0c\xd2\xf7\x9d\xbf\xbc\x13D4(\xd0K\x81\x88YgK\xef\xcdZn\x90\x88Wt\x9f\x9a\xee\x95:v\x86\x02\x1c\n\x04\xcc\xda{]\x12h\xa9A"^=qd\x85\x18P@\x8b\x02\x11\xb3\xee\xbf&\xb3\xcc \x11\xaf\x86Z\xf2F\x1eP\x80G\x81\xe5\x98\xf5\xd5 \xc0+\x9ez \x8a:\x05\x96a\xd6\x17\x83\x00\xaf\xd4\xd5\r\tq)\xf0\xfa\x15\xb3\x16\x0c2:\x07^qU\x03q\xf4)0:]\\\xcd\x9a7\xc8\x1bV\xaf\xf4\x15\r\x19q*p\xb7\xb0\x9a5g\x90\x07\xac^q\xd6\x02\xb14*\xb0\x80Y\xb3\x06\txu\x8c\xd5+\x8dECN\x8c\n\xccc\xd6\xa7A\xb0z\xc5X\x04\x84\xd2\xac\xc0\xfd\xe6\xe7E\xc3\xa9A\xb0z\xa5\xb9d\xc8\x8dU\x81\xd7\xbd\xe9E\xc3\x89Apq\x90\xb5\x02\x08\xa6[\x81\xd1\x99s\xa7\xd5\xbdYc\x83\x00\xaft\xd7\x0b\xd9\xb1+\x100k\xf7eb\x10\xe0\x15\xbb\xfe\x08\xa8]\x81\x80Y\x1b\xb7\xe3#\x08\xf0J{\xb1\x90\x9f\x80\x02\x11\xb3\x8e\x87\x0ex%\xa0=B\x9aP `\xd6\xb6\x1b\xe0\xe2\xa0\x89b!I\x01\x05^\xc3\x9d%\xb8\xf7J@x\x844\xa2\xc0\xe8\xfc\xff\x00\x96G\x86\xd0]J\x0c\xa3\x00\x00\x00\x00IEND\xaeB`\x82'

def load_apng():
	from PIL import Image
	from io import BytesIO
	return Image.open(BytesIO(apng))