print(range(3))
##==> range(0,3)
print(list(range(3)))  ##<==リストに変換して表示

## range (開始位置,終了位置)
print(list(range(2,6))) ##<==2から始まって6の直後で終わる整数をリストに変換して表示

## [2,3,4,5]

for i in range(3): ##<==取り出し変数iにrangeで生成した整数をいれる
    print(i)
## ==> 0

##     1

##     2