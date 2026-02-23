def getBondPrice_E(face, couponRate, yc):
    cf = face * couponRate
    pvcfsum = 0

    for t, y in enumerate(yc, start=1):
        pvm = (1 + y) ** (-t)
        pvcf = pvm * cf
        if t == len(yc):
            pvcf = pvm * cf + pvm *face
        pvcfsum = pvcfsum + pvcf    
    return pvcfsum

face = 2000000
couponRate = .04
yc = [.010,.015,.020,.025,.030]
x = getBondPrice_E(face, couponRate, yc)
print(x)
