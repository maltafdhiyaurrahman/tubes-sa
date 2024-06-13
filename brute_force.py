from itertools import combinations

def brute_force_knapsack(items, capacity):
    n = len(items)
    best_value = 0
    best_combination = []
    
    for r in range(1, n + 1):
        for combination in combinations(items, r):
            total_weight = sum(item[1] for item in combination)
            total_value = sum(item[2] for item in combination)
            
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = combination
    
    selected_items = [item[0] for item in best_combination]
    total_weight = sum(item[1] for item in best_combination)
    return selected_items, best_value, total_weight

items = [
    ('A', 10, 60),
    ('B', 20, 100),
    ('C', 30, 120),
    ('D', 25, 80),
    ('E', 15, 50)
]

capacity = 50
selected_items, total_value, total_weight = brute_force_knapsack(items, capacity)

print(f"Barang yang dipilih: {selected_items}")
print(f"Total nilai keuntungan: {total_value}")
print(f"Total berat: {total_weight}")
