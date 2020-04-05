from inputs import *
load('2839')
sugars = [int(input()) for _ in range(5)]
for sugar in sugars:
    cnt = 0
    while sugar > 0:
        if sugar % 5 != 0:
            sugar -= 3
            if sugar < 0:
                cnt = -1
                break
            cnt += 1
        elif sugar % 5 == 0:
            cnt += 1
            sugar -= 5
        elif sugar % 5 != sugar % 3 != 0:
            cnt = -1
    print(cnt)