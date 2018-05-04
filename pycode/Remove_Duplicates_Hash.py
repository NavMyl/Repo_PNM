NO_OF_CHARS = 256
bin_hash = [0] * NO_OF_CHARS
print bin_hash
ip_ind = 0
res_ind = 0
list1 = ['a','a','b','b','c']
temp =''
while ip_ind != len(list1):
    temp = list1[ip_ind]
    if bin_hash[ord(temp)] == 0:
        bin_hash[ord(temp)] = 1
        #print list1
        list1[res_ind] = list1[ip_ind]
        #print list1
        res_ind += 1
    ip_ind += 1

#new_list = list1[0:res_ind]



print ''.join(list1[0:res_ind])
