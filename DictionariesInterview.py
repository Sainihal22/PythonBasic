# Write the code.
# Take 3 items and prices from user.
# Store in dictionary.
# Print the most expensive item.
# Enter item 1 : apple
# Enter price 1: 50
# Enter item 2 : mango
# Enter price 2: 80
# Enter item 3 : banana
# Enter price 3: 30

# Most expensive : mango at 80


# prices = {}

# for i in range(3):
#     item = input(f"Enter an item {i+1} : ")
#     price = int(input(f"Enter the price of above item {i+1} : "))
#     prices[item] = price

# print(prices)
prices = {'Apple': 40, 'Mango': 90, 'Kiwi': 120}
# keys_list = list(prices.keys())
# print(keys_list)
# max_price = prices[keys_list[0]]
# print(max_price)
# max_item = keys_list[0]
# print(max_item)

# for key, value in prices.items():
#     if value > max_price:
#         max_price = value
#         max_item = key

# print(f"The most expensive fruit {max_item} is {max_price}")

# max_price = 0
# max_item = None

# for key, value in prices.items():
#     if value > max_price:
#         max_price = value
#         max_item = key

# print(f"The most expensive fruit {max_item} is {max_price}")
