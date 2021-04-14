hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

#number of purchases per hairstyle last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for i in prices:
  total_price += i

average_price = total_price / len(prices)
print("Average Haircut Price Last Week: $" + str(average_price))
print()

#too expensive! let's reduce the prices by $5 this week
new_prices = [i - 5 for i in prices]
print(new_prices)

#what's the new average?
new_total_price = 0
for i in new_prices:
  new_total_price += i

new_price_average = new_total_price / len(new_prices)
print("Average Haircut Price This Week: $" + str(new_price_average))
print()
#better! also i just realized it's literally last week's average minus 5 lol

#how much revenue was made last week?
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue Last Week: $" + str(total_revenue))

#average daily revenue last week
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue Last Week: $" + str(average_daily_revenue))
print()

#haircuts under 30 dollars using new price list
print("On a budget? Get your hair cut in selected styles for under $30!")
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)
