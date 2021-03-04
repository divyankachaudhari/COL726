import numpy as np
def computeSequence(n):
    a = np.empty(n)
    if(n>0):
        a[0] = 1/3
        if(n>1):
            a[1] = 1/12
            if(n>2):
                for i in range(2,n):
                    a[i] = ((2.25*(a[i-1])) - (0.5*(a[i-2])))
    
    return a
