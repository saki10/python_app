## 割合の計算　

print('割合を計算する')

goods = int(input("商品を記入してください")) 
ratio = float(input("割合を記入してください"))

total = goods-(goods*ratio) 

print('値段は',round(total),'円です')