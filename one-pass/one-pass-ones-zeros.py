# Question:
# Given an array of 1s and 0s arrange the 1s together and 0s together in a 
# single scan of the array. Optimize the boundary conditions.

def onepass(l):
    """Strategy: use two counters, c_one and c_zero, one at front and one at end.
    1) Stop when they meet. 
    2) If c_one meets a one go forward, if c_zero meets zero go foward
    3) if c_one sees zero stop,
    4) Swap when both are in wrong position
    """
    ret = [ False for i in xrange(len(l)) ]

    if l[0] == 1:
        c_one, c_zero = 0, len(l) - 1
        direction = True                # c_one going to right
    else:
        c_one, c_zero = len(l) - 1, 0
        direction = False               # c_one going to left
    #c_one MUST point to one, c_zero might not point to appropriate value

    c_one_fail, c_zero_fail = False, l[c_zero] != 0

    while True:
        #Manual Break
        if direction:
            if c_one >= c_zero:
                break
        else:
            if c_one <= c_zero:
                break

        if c_one_fail and c_zero_fail: 
            ret[c_one] = l[c_zero]
            ret[c_zero] = l[c_one]
            if direction:
                c_one += 1
                c_zero -= 1
            else: 
                c_one -= 1
                c_zero += 1

            #New conditions
            c_one_fail = l[c_one] != 1
            c_zero_fail = l[c_zero] != 0

        if not c_one_fail:
            ret[c_one] = 1
            if direction:
                c_one += 1
            else:
                c_one -= 1
            c_one_fail = l[c_one] != 1

        if not c_zero_fail:
            ret[c_zero] = 0
            if direction:
                c_zero -= 1
            else:
                c_zero += 1
            c_zero_fail = l[c_zero] != 0

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
        






