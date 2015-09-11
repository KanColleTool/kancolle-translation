#!/usr/bin/env python
from __future__ import print_function
import os
import json
import argparse
import commands

BASE = os.path.abspath(os.path.dirname(__file__))

parser = argparse.ArgumentParser(description=u"Tool for working with KanColle translation files")
subparsers = parser.add_subparsers(metavar=u"command", dest='cmd')

subcommands = {}
for name, mod in commands.commands:
	subp = subparsers.add_parser(name, help=mod.desc)
	if 'add_arguments' in mod.__dict__:
		mod.add_arguments(subp)
	subcommands[name] = mod

if __name__ == '__main__':
	json_path = os.path.join(BASE, u'translation.json')
	with open(json_path, 'rU') as f:
		data = json.load(f)
	
	args = parser.parse_args()
	retval = subcommands[args.cmd].run(data, args)
	if retval is not None:
		if not isinstance(retval, basestring):
			print(u"Encoding...")
			retval = json.dumps(retval, indent=4, separators=(',', ': '), ensure_ascii=False, sort_keys=True)
		with open(json_path, 'w') as f:
			print(u"Writing...")
			f.write(retval.encode('utf-8'))
