import json

desc = u"Filters out blacklisted lines"

def add_arguments(parser):
	parser.add_argument('blfile')

def run(data, args):
	bldata = {'*': []}
	with open(args.blfile, 'rU') as f:
		for item in json.load(f):
			src = item['src']
			ctx = item['ctx']
			if not src in bldata:
				bldata[src] = []
			bldata[src].append(ctx)
			print(u"Blacklisted: {0} -> {1}".format(src, ctx))
	
	retval = []
	for item in data:
		src = item['src']
		ctx = item['ctx']
		if src in bldata and ctx in bldata[src] or ctx in bldata['*']:
			print(u"Skip: {0} -> {1}".format(src, ctx))
			continue
		retval.append(item)
	print(len(retval))
	
	return retval
