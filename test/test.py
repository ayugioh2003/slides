# 第三週作業：該怎麼找錢（進階版）
# consumer_money 1~1000 286
# coin = [500, 100, 50, 10, 5, 1]
# change = 1000 - comsumer_money
# change_num = 500, 1; 100, 2; 10, 1; 1,4


print('歡迎來到結帳系統')
consumer_money = int(input("請輸入您購買商品的價格: "))
change = 1000 - consumer_money

coin = [500, 100, 50, 10, 5, 1]
# 空白的 list https://goo.gl/6Mdai6
coin_num = [0]*6


# 計算每個硬幣需要的數量
for i in range(len(coin)):
  while change >= coin[i]:
    change = change - coin[i]
    coin_num[i] = coin_num[i] + 1

# 抓出數量超過零的硬幣，新增到 result
# https://goo.gl/zRn8Go
result = []
for j in range(len(coin)):
  if coin_num[j] > 0:
    result.append( str(coin[j]) + ", " + str(coin_num[j]) )

# 加入分號分隔 https://goo.gl/HikSdi
print('即將印出要找的零錢種類與數量')
print("; ".join(result))

result
