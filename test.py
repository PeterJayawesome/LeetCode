a=['abc','abcde','abcde']
print(zip(a))
print(a)
shortest = min(a,key=len)
for i,letter_group in enumerate(shortest):
	for other in a:
		if other[i] != letter_group:
			print(shortest[:i])
			break
print(shortest)