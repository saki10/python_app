## 0.1mmの紙を折ると高さが分かるアプリ

print('紙を折るとどんな高さになるかアプリ')

profound = 0.1
fold = float(input("折る回数を記入してください")) 
total = 2**fold*0.1
print('高さは',total,'mmです')