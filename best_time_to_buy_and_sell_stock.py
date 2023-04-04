prices = [7,1,5,3,6,4]

def profit(prices):
    profits = []

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[i] - prices[j]
            profits.append(profit)

    return max(profits)

print(profit(prices = prices))
# yukarıdaki çöümün list comprehension ile yapılmış şekli
prices = [7,1,5,3,6,4]
uzunluk = len(prices)
def p():
    liste = [prices[j]-prices[i] for i in range(uzunluk) for j in range(i+1,uzunluk)] # list comprehension
    liste.append(0)
    return max(liste)
print(p())

# yukarıdaki çözüm aslında çalışıyor ancak zaman hatasına takılıyor bu yüzden şöyle bir çözüm daha var
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf") # bunun amacı min_price değişkenine listenin ilk elemanını atayabilmek çünkü kendisi her zaman herhangi bir sayıdan büyük.
        max_profit = 0

        for price in prices:
            if price < min_price: # burada işlem True oluyor ve min_price Price'a eşitleniyor yani verilen listenin ilk elemanına.
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
