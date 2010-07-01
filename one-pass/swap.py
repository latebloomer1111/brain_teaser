# Question:
# Given an array of 1s and 0s arrange the 1s together and 0s together in a 
# single scan of the array. Optimize the boundary conditions.


def swap(l):
    zero,one = 0, len(l) -1 
    while (zero < one):
        if not l[zero]:
            zero += 1
        else:               #Adding else here prevents both pointers moving at the same time
            if l[one]:
                one -= 1
            if l[zero] and (not l[one]):
                temp = l[zero]
                l[zero] = l[one]
                l[one] = temp
        print l, zero, one
    return l


l = [1, 0, 0, 1, 0, 1, 0, 1]
print "original", l
print swap(l)

l = [0, 0, 0, 1, 0, 1, 0, 1]
print "original", l
print swap(l)

l = [1, 1, 1, 1, 1, 1, 1, 1]
print "original", l
print swap(l)
    














