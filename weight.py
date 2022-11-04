## BMI測定

print('BMIを計算する')
heiget = int(input("身長を記入してください")) /100.0
weiget = int(input("体重を記入してください"))

bmi = weiget / (heiget*heiget)
print('BMIは',round(bmi),'です')