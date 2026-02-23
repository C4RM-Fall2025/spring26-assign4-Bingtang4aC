def PriceBond(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = face * couponRate / ppy  
    
    for i in range(1, (m * ppy)+1):
        pvm = (1 + y / ppy) ** (-i)
        pvcf = pvm * cf
        pvcfsum = pvcfsum + pvcf

        if i == m * ppy: 
            pvcfsum = pvcfsum + face * pvm

    return pvcfsum

y = 0.03
face = 2_000_000
couponRate = 0.04
m = 10


ppy = 1
price_1 = PriceBond(y, face, couponRate, m, ppy)
print(price_1)


ppy = 2
price_2 = PriceBond(y, face, couponRate, m, ppy)
print(price_2)
