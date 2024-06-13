def greedy_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    
    total_value = 0
    total_weight = 0
    selected_items = []
    
    for item in items:
        if total_weight + item[1] <= capacity:
            selected_items.append(item[0])
            total_value += item[2]
            total_weight += item[1]
    
    return selected_items, total_value, total_weight

items = [
    ('A', 10, 60),
    ('B', 20, 100),
    ('C', 30, 120),
    ('D', 25, 80),
    ('E', 15, 50)
]

capacity = 50
selected_items, total_value, total_weight = greedy_knapsack(items, capacity)

print(f"Barang yang dipilih: {selected_items}")
print(f"Total nilai keuntungan: {total_value}")
print(f"Total berat: {total_weight}")
