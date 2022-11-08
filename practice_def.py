#3の3乗は？

def root(wo):
    print(str(wo),"の10乗は",wo**3,"です")
root(3)


#例
def say_hello(greeting) :
    print(greeting)

hello = say_hello
hello("Good Morning")

#==> Good Morning

def split_bills(people,total):
    price = total /people
    print(str(people),'人の場合',str(price),'円です')
split_bills(10,68900)


def split_bills(people,total):
    price = total // people
    print(str(people),'人の場合',str(price),'円です')
split_bills(10,68900)


def get_bills(water,gas,power,rent=8000):
    total = rent + water +gas + power
    print (total)

    if total >= 110000 :
        print('高め')
    elif total >= 100000 and total < 110000:
        print('まぁまぁ')
    else:
        print('低め')
get_bills(water=500,gas=500,power=10000)

#実引数に数字を競っているすることができる
# 未満 <