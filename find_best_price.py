def findInShop(prices,items,shop):
	itemset = set(items)
	l = set(e for s in prices[shop] for e in s['items'])
	print('set: ',l)
	if not itemset.issubset(l):
		# print('Hey!')
		return 0xffffffff
	covered = [{'items':[],'price':0}]
	res = 0
	for price in prices[shop]:
		print(price)
		temp = [{'items': c['items']+price['items'],'price': c['price']+price['price']} for c in covered]
		covered += temp
	res = 0xffffffff
	for c in covered:
		if isSublist(items,c['items']) and c['price'] < res:
			res = c['price']
	return res

def isSublist(a,b):
    for item in a:
        if a.count(item) > b.count(item):
            return False
    return True


def find_best_price(items,prices):
	# print(items)
	res = {'shop':'','price': 0xffffffff}
	p = {}
	for price in prices:
		for item in price[2:]:
			if item in items:
				# print(item)
				p[price[0]] = p.get(price[0],[]) + [{'price':price[1],'items':price[2:]}]
	print(p)
	for shop in p:
		a = findInShop(p,items,shop)
		if a < res['price']:
			res['shop'] = shop
			res['price'] = a
	return res if res['price'] < 0xffffffff else 'No result found'





prices = [
	['shop_1',3.00,'latte'],
	['shop_1',1.50,'cookie'],
	['shop_1',2.00,'brownie'],
	['shop_1',4.50,'latte','brownie'],
	['shop_2',2.50,'latte'],
	['shop_2',2.50,'cookie'],
	['shop_2',4.75,'latte','brownie','water'],
]

print(find_best_price(['latte','cookie','brownie'],prices))