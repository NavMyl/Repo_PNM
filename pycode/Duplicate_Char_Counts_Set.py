l1 = ['a','b','a','c','c']

for i in set(l1):
    if l1.count(i) > 1:
        letter = i
        count = l1.count(i)
        print ('{} count is {}'.format(letter,count))
