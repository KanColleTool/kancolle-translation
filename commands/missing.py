import sys
import json

desc = u"Dumps missing lines"

def add_arguments(parser):
	parser.add_argument('lang')
	parser.add_argument('outfile')

def run(data, args):
	untld = []
	for d in data:
		if not args.lang in d:
			untld.append(d)
	
	s = json.dumps(untld, indent=4, separators=(',', ': '), ensure_ascii=False, sort_keys=True)
	if args.outfile == '-':
		print(s)
	else:
		with open(args.outfile if args.outfile != '-' else sys.stdout, 'w') as f:
			f.write(s.encode('utf-8'))
