#연습문제7
import random
random.randint(1, 45)
i = 0
res = []
while i < 6 :
    i = i + 1
    a = random.randint(1, 45)
    if a in res :
        print('값이 기존에 있습니다. 새롭게 추가하지 않습니다.')
    else :

    res.append(a)
print(res)