# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    # create a new list to store unit price for each item
    # and fill in unit price values
    unit_prices = [0 for i in range(len(weights))]
    for i in range(len(weights)):
        unit_prices[i] = float(prices[i]/weights[i])

    # sort the unit prices and store it in a new list sorted_unit_prices
    sorted_unit_prices = sorted(unit_prices, reverse=True)

    # create a new list to store weights in accordance with unit prices
    # i.e. the weight of the most valued item will appear first in the list
    # weight of the least valued item will appear last in the list
    sorted_weights = [0 for i in range(len(sorted_unit_prices))]
    for i in range(len(weights)):
        index = unit_prices.index(sorted_unit_prices[i])
        sorted_weights[i] = weights[index]

    # iterate through the sorted_unit_prices
    # and add as much item as possible, starting with the most valued ones
    value = 0
    for i in range(len(sorted_unit_prices)):
        if capacity >= sorted_weights[i]:
            value += sorted_unit_prices[i]*sorted_weights[i]
            capacity -= sorted_weights[i]
        else:
            value += sorted_unit_prices[i]*capacity
            capacity = 0
        if capacity>0:
            continue
        else:
            break

    return value





if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
