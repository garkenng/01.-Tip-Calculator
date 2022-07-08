# Asks the user for the price of the meal and amount in percentage of tip they wish to add
# Tax is fixed at 15%

# set tax as a constant variable
tax = 0.15

# takes cost of meal
def total_cost_of_meal(cost, tip):
    percentage_tip = int(tip) / 100
    cost = int(cost) * percentage_tip
    cost *= tax + cost
    return cost 


cost_of_meal = input('Cost of meal: ')
tip_amount = input('Tip percentage: ')

print(total_cost_of_meal(cost_of_meal, tip_amount))