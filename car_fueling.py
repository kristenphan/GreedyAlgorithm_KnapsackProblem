# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # calculate number of gas stations available
    n = len(stops)
    # clone the array that stores the location of all available gas stations
    # and subsequently add the location for the starting point and destination
    stops_copy = stops[:]
    stops_copy.insert(0, 0)
    stops_copy.append(d)
    # initialize the number of refills
    # and index of the gas station in the array where we last refilled
    numRefills = 0
    lastRefill = 0

    # iterate through all gas stations
    for i in range(1,n+1):
        # if the gas station at position i is beyond the distance allowance from the last refill position
        if m < (stops_copy[i]-stops_copy[lastRefill]):
            if (i-1) == lastRefill: # return -1 if it's impossible to reach gas station i
                return -1
            else: # return to the last gas station i-1 and refill
                lastRefill = i-1
                numRefills += 1
                if m < (stops_copy[i]-stops_copy[lastRefill]): # double check that after refill at the previous gas station, we're still able to reach the current gas station
                    return -1
        # if the gas station i is right at the border where we will be running out of gas, get gas here
        elif m == (stops_copy[i] - stops_copy[lastRefill]):
            lastRefill=i
            numRefills += 1
        # the stop is with distance allowance. no need to get gas
        # and try to advance to the next gas station
        else:
            continue

    # check if we're able to reach the destination from last refill
    if m < (stops_copy[-1]-stops_copy[lastRefill]):
        if n == lastRefill:
            return -1
        else: # if not, go back to the last station to get gas
            lastRefill = n
            numRefills += 1

    # check again if we're still able to reach the destination after the last refill
    # if not, return -1 because we've tried to get gas at the last gas station n
    if m < (stops_copy[-1]-stops_copy[lastRefill]):
        return -1

    return numRefills



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
