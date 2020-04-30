from datetime import datetime
from inputs import *
load('1924')


x, y = map(int, input().split())

print(datetime(2007, x, y).strftime("%A").upper()[:3])


