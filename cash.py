## 貯金計画アプリ

print('貯金計画アプリ')

money = int(input("目標金額を記入してください")) 
year = int(input("何年後までに達成したいか")) 
total =  int(money /(year*365) )
print('1日に約',total,'円貯金しよう！！')