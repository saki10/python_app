import random
num3 = random.randint(51,100)
num4 = random.randint(1,50)

print("問題",num3,"-",num4,"=は?")

ans = int(input('答えを記入してください'))

if num3 - num4 == ans:
   print("正解です！")
else:
    print("不正解。。")
