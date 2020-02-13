import random

lineNums = [num for num in range(1,33)]
random.shuffle(lineNums)
for num in lineNums:
    print(num)
    