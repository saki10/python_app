
import random
kan = random.randint(1,10) ##1~10までランダムに出力する　合っている用
ji = random.randint(1,10)  ##1~10までランダムに出力する　間違い用
print("撒"*kan +"撤"+"撒"*ji, ) ##間違い探し出力

ans =  int(input('間違っている漢字は何番目？')) ##input関数でユーザが答えを入力できる

if ans == kan + 1: ##もしあっていた場合は、
   print("正解です！") ##正解と出力される
else:
    print("不正解。。",kan+1,"番目です") #それ以外は、不正解と答えが出力される