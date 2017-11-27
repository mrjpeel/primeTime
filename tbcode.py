import time
start = time.time()

currentprimes = []
for number in range(1,100000):
    divided = False
    root = number**0.5
    root = root/2
    root = int(root+1)
    for check in range(root):
        if number%((check+2)*2) == 0:
            divided = True
    if divided == False:
        currentprimes.append(number)

print (time.time() - start)