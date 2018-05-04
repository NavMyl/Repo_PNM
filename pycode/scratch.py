#s = "ABC"

def permutations(string, step = 0):
    print " Function has been called", step
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print "".join(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):
        #print "i value:",i

        # copy the string (store as array)
        string_copy = [character for character in string]
        #print string_copy
        #print "Before Swap", string_copy[step], step, string_copy[i], i

        #string_copy = ['A','B','C']

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        #print "Swap", string_copy[step],step, string_copy[i],i
        #print "after swap",string_copy

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        #print "pass",string_copy, step, i
        #print "call"
        #step+=1
        permutations(string_copy, step+1 )
    #return string_copy

string = "AB"
n = len(string)
a = list(string)
print permutations('ABCD',0)
