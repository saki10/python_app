import random 
num1 = random.randint(1,50)
num2 = random.randint(50,100)
print ("問題",num1,"+",num2,"=は？")

ans = int(input("答えは？"))

if num1+num2 == ans:
    print("正解!!")
else :
     print("不正解。。。")