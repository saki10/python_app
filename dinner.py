import random
tekion = ["ハンバーグ","ムニエル","オムライス","酢豚","チャーシュー丼","納豆ご飯"]
winnter = ["鍋","ラーメン","チゲ","焼肉","お好み焼き","チュクミ","豚汁","クリームシチュー"]
summer = ["冷麺","蕎麦","カレー","冷やし担々麵","うどん","冷や汁","冷やし中華","サンドウィッチ"]




answer = int(input("今日の気温は？"))

if answer <= 15: 
    taberu = random.choice(winnter)
    print(taberu,"とかはいかがでしょうか？")
elif answer >= 28:
    taberu = random.choice(summer)
    print(taberu,"とかはいかがでしょうか？")
else:
    taberu = random.choice(tekion)
    print(taberu,"とかはいかがでしょうか？")



##import random
##tekion = ["ハンバーグ","ムニエル","オムライス","酢豚","チャーシュー丼","納豆ご飯"]
##winnter = ["鍋","ラーメン","チゲ","焼肉","お好み焼き","チュクミ","豚汁","クリームシチュー"]
##summer = ["冷麺","蕎麦","カレー","冷やし担々麵","うどん","冷や汁","冷やし中華","サンドウィッチ"]


#taberu = random.choice(tekion)
#win = random.choice(winnter)
#su = random.choice(summer)

#answer = int(input("今日の気温は？"))

#if answer <= 15: 
#     print(taberu)
#elif answer >= 28:
#    print(win)
#else:
#    print(su)



