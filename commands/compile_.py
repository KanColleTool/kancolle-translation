import json
from binascii import crc32

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
	
	encoded = json.dumps(compiled, separators=(',', ':'), ensure_ascii=False, sort_keys=True)
	
	with open(args.patchfile, 'w') as f:
		f.write(encoded.encode('utf-8'))
