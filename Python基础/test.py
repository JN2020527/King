import math

number = 0
while True:
    number += 1
    if math.isqrt(number + 100)**2 == number + 100 and math.isqrt(number + 268)**2 == number + 268:
        print(number)
        break
