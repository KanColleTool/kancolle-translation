import sys
import json
from util import dump

desc = u"Dumps missing lines"

def add_arguments(parser):
	parser.add_argument('lang')
	parser.add_argument('outfile')

def run(data, args):
	untld = []
	for d in data:
		if not args.lang in d:
			d[args.lang] = ""
			untld.append(d)

	dump(untld, args.outfile)
