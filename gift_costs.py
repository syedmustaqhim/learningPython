import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')

gift_costs = np.array(gift_costs).astype(int)  # convert string to int


start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))
#### OUTPUT ####


#  32765421.24
# Duration: 5.4515392780303955 seconds

# #/REFACTORING THE CODE ###drasctically decreases run-time###

# start = time.time()

# total_price =  gift_costs[gift_costs < 25].sum() * 1.08

# print(total_price)
# print('Duration: {} seconds'.format(time.time() - start))

#### OUTPUT ####
#  32765421.24
# Duration: 0.0852658748626709 seconds
