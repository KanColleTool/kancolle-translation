import json
from binascii import crc32
from util import load

desc = u"Applies a CRC32-keyed patch"

def add_arguments(parser):
	parser.add_argument('lang')
	parser.add_argument('patchfile')

def run(data, args):
	pdata = load(args.patchfile)
	newdata = data
	for i, d in enumerate(data):
		crc = str(crc32(d['orig'].encode('utf-8')) & 0xffffffff)
		if crc in pdata:
			newdata[i][args.lang] = pdata[crc]
		else:
			print(u"Unknown: {0}".format(crc))

	return newdata
