def compress(chars):
	if chars[-1]=='$':
	    chars.append('#')
	else:
	    chars.append('$')
	count = 1
	k = 0
	i = 1
	j = 0
	while i < len(chars):
	    if chars[i] == chars[j]:
	        count += 1
	        i += 1
	    else:
	        if count != 1:
	            a = [digit for digit in str(count)]
	            # print(a)
	            for x in a:
	                k += 1
	                chars[k] = x
	                # print(chars)
	        k += 1
	        chars[k] = chars[i]
	        j = i
	        count = 1
	        i += 1
	while len(chars)>k:
		chars.pop()
	print(chars)
	return len(chars)


chars = ["a","a","b","b","b","b","b","b","b","b","b","b","b","c","c","b","b","b","b","c",'c','c']

print(compress(chars))

print(chars)