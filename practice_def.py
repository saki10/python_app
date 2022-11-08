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