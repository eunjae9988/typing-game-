import random
import time

w=['cat','dog','fox','monkey','panda','frog','snake','wolf','java']
n=1
print('[already for game]Enter!')
start=time.time()
q=random.choice(w)
while n<=5:
    print("*question",n)
    print(q)
    x=input()
    if q==x:
        print("correct")
        n=n+1
        q=random.choice(w)
    else:
        print("try again")