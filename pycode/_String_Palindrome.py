

anagram = [x for x in input()]
print anagram
count_alphabets = [ anagram.count(x) for x in set(anagram) ]
print count_alphabets
middle_element = [x for x in count_alphabets if x % 2 == 1]
print middle_element

if len(middle_element) == 0 or len(middle_element) == 1:
    print("YES")
else:
    print("NO")