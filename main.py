#create list of pizza toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#create list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

#find length of toppings list
num_pizzas = len(toppings)

print('We sell ' + str(num_pizzas) + ' kinds of pizza!')

#combine list of prices with list of toppings
pizzas = list(zip(prices, toppings))
print(pizzas)

#sort combined list
pizzas.sort()

#create lists grouping pizza type by price
cheapest_pizza = pizzas[1]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
num_two_dollar_slices = prices.count(2)
print(three_cheapest)
print(num_two_dollar_slices)
