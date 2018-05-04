def reverse(string):

    result = ''

    for i in xrange(len(string),0,-1):
        print i
        result += string[i-1]

    return result



print (reverse('text'))