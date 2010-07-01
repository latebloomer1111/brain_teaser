# Question:
# Given an array of 1s and 0s arrange the 1s together and 0s together in a 
# single scan of the array. Optimize the boundry conditions.

def onepass(l):
    """remember, l[:boundry] are all zeros
    iterator checks for zeros and swap with boundry
    """
    ret = [False] * len(l)      #python list are immutable in iteration?
    boundry = 0
    for i in xrange(len(l)):
        if l[i]:
            ret[i] = 1          #careful, you should assign here, try base case = [1, 1, 1, 1]
        else:
            ret[boundry] = 0
            boundry += 1
            ret[i] = 1
    return ret


if __name__ == "__main__":

    l = [1, 0, 0, 1, 0, 1, 0, 1]
    print "original", l
    print onepass(l)

    l = [0, 0, 0, 1, 0, 1, 0, 1]
    print "original", l
    print onepass(l)
 
    l = [1, 1, 1, 1, 1, 1, 1, 1]
    print "original", l
    print onepass(l)
        

