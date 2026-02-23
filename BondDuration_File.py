def getBondDuration(y, face, couponRate, m, ppy=1):
    cf = face * couponRate
    pvcfsum = 0
    wsum = 0

    for i in range(1, (m * ppy) + 1):
        pvm = (1 + y / ppy) ** (-i)

        cf_t = cf
        if i == m * ppy:
            cf_t = cf + face

        pvcf = pvm * cf_t
        pvcfsum = pvcfsum + pvcf
        w = i * pvcf
        wsum = wsum + w

    d = wsum / pvcfsum
    return d

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

x = getBondDuration(y, face, couponRate, m, ppy)
print (x)
