import json

def dump(data, filename, pretty=True):
	s = json.dumps(data, indent=4, separators=(',', ': '), ensure_ascii=False, sort_keys=True)
	if filename == '-':
		print(s)
	else:
		with open(filename, 'w') as f:
			f.write(s.encode('utf-8'))

def load(filename):
	with open(filename, 'rU') as f:
		return json.load(f)
