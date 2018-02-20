def strSubsets(str):
	if not str:
		return [""]
	#store the result for str[1:]
	arr = strSubsets(str[:-1])
	#for elem in arr, add str[0]+elem as a subset
	return [s+str[-1] for s in arr] + arr

s = "abc"
print strSubsets(s)#return ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']


prices = [7, 1, 5, 3, 6, 4]
arr = [prices[i]-prices[i+1] for i in xrange(len(prices)-1)]
arr = reduce(lambda x,y: (x+y if x*y>0 else x,y),arr)
print arr