import random
kanji = random.randint (1,15)
matigai = random.randint (1,15)

print("離"*kanji+"難"+"離"*matigai,)

an = int(input("何番目が間違っているでしょうか?"))

if kanji+1 == an :
    input('正解です！！')
else:
    input('不正解です！！',kanji+1,'番目です')