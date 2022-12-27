from itertools import combinations

essential_items_data = {
    "TOI": [3, 5, 6],
    "Hindu": [2.5, 4, 4],
    "ET": [4, 4, 10],
    "BM": [1.5, 1.5, 1.5],
    "HT": [2, 4, 4],
}

cost = { newspaper:(prices[0]*5 + prices[1] + prices[2]) for newspaper, prices in essential_items_data.items() }

budget = int(input())

result =[]
for newspapers in combinations(cost.keys(), 2):
    if (cost[newspapers[0]] + cost[newspapers[1]] <= budget):
        result += [set(newspapers)]

print(*result, sep=', ')
