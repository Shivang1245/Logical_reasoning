'''Question:- You are given an array [prices] where prices[i] is the price of a given stock on the Ith day.
You want t maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.
'''
priceList= [1,2,3,4,5,67,86,8,65,545,766]

def find_max_profit(pricelist):
    min_price = float('inf')
    max_profit = 0

    for price in pricelist:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

print(find_max_profit(priceList))

# we are taking a record of the minimum price of the stock value and then checking if it will generate a max profit on the given day