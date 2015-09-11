import json
from binascii import crc32
from util import dump

desc = u"Compiles a TL database"

def add_arguments(parser):
	parser.add_argument('lang')
	parser.add_argument('patchfile')

def run(data, args):
	compiled = {}
	for item in data:
		if not args.lang in item:
			continue
		crc = str(crc32(item['orig'].encode('utf-8')) & 0xffffffff)
		compiled[crc] = item[args.lang]
	
	dump(compiled, args.patchfile, pretty=False)
