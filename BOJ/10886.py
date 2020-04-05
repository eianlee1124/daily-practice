from inputs import *
load('10886')

NO, YES = range(2)
NOTCUTE = 'Junhee is not cute!'
CUTE = 'Junhee is cute!'

ret = {NO: 0, YES: 0}
test = int(input())
for _ in range(test):
    vote = int(input())
    ret[vote] += 1
    
print(NOTCUTE if ret[0] > ret[1] else CUTE)