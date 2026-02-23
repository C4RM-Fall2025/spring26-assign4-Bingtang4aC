def getBondPrice_E(face, couponRate, m, yc):
    cf = face * couponRate
    pvcfsum = 0

    for t, y in enumerate(yc, start=1):
        pvm = (1 + y) ** (-t)
        pvcf = pvm * cf
        if t == m:
            pvcf = pvm * cf + pvm *face
        pvcfsum = pvcfsum + pvcf    
    return pvcfsum

face = 2000000
couponRate = .04
m = 5
yc = [.010,.015,.020,.025,.030]
x = getBondPrice_E(face, couponRate, m, yc)
print(x)
