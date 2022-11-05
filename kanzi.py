import random
kan = random.randint(1,10)
ji = random.randint(1,10)
print("撒"*kan +"撤"+"撒"*ji, )

ans =  int(input('間違っている漢字は何番目？'))

if ans == kan + 1:
   print("正解です！")
else:
    print("不正解。。",kan+1,"番目です")