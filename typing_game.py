import random
import time

def processing():
    global user_num, n
    # Fixed the isdigit syntax error
    if user_num.isdigit() == True and (int(user_num) >= 1 and int(user_num) <= 10):
        start = time.time()
        q = random.choice(w)  
        
        while n <= int(user_num):
            print("*question", n)
            print(q)
            x = input("Input: ")  
            
            if q == x:
                print("correct")
                n = n + 1
                q = random.choice(w)
            else:
                print("wrong! try again!")
                
        end = time.time()
        et = end - start
        et = format(et, ".2f")
        print("typing time:", et, "seconds")
    else:
        print("Entered answer is not 1 ~ 10 numbers. Try again please.")
        user_num = input()
        processing()

w = ['cat', 'dog', 'fox', 'monkey', 'panda', 'frog', 'snake', 'wolf', 'java']
n = 1

print('[already for game]Enter!')
input()
print("Choose number of questions:1~10")
user_num = input()

if user_num.isdigit() == True and (int(user_num) >= 1 and int(user_num) <= 10):
    print("Answer is number")
    processing()
else:
    print("Answer is not 1~10, please try again")
    user_num = input()
    processing()
