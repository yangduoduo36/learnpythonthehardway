def scan(args_str):
	"""Scan the input for words, search in buckets and return the bucket name and the word if present as a tuple. If word doesn't belong to any bucket, return a tuple stating error and the word."""
	args_list = args_str.split()
	args_lower_list = [word.lower() for word in args_list]
	result = []
	for pos,word in enumerate(args_lower_list):
		if word in ['north','south','east']:
			result.append(('direction',word))
		elif word in['go', 'kill', 'eat']:
			result.append(('verb',word))
		elif word in ['the','in','of']:
			result.append(('stop',word))
		elif word in ['bear','princess']:
			result.append(('noun',word))
		elif word.isdigit():
			result.append(('number',int(word)))
		else:
			result.append(('error',args_list[pos]))
	return result
