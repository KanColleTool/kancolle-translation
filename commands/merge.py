import sys
import json
from util import load

desc = u"Imports translated lines"

def add_arguments(parser):
	parser.add_argument('lang')
	parser.add_argument('infile')

def run(data, args):
	pd = load(args.infile)
	d = {}
	for item in data:
		if not item['ctx'] in d:
			d[item['ctx']] = {}
		d[item['ctx']][item['orig']] = item

	for item in pd:
		if item[args.lang]:
			d[item['ctx']][item['orig']][args.lang] = item[args.lang]
	return data
