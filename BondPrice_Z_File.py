def getBondPrice_Z(face, couponRate, times, yc):
    cf = face * couponRate
    pvcfsum = 0
    last_t = times[-1]

    for t, y in zip(times, yc):
        pvm = (1 + y) ** (-t)
        pvcf = pvm * cf
        if t == last_t:
            pvcf = pvm * cf + pvm *face
        pvcfsum = pvcfsum + pvcf    
    return pvcfsum

face = 2000000
couponRate = .04
times=[1,1.5,3,4,7]
yc = [.010,.015,.020,.025,.030]
x = getBondPrice_Z(face, couponRate, times, yc)
print (x)
