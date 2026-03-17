def solution(products, changes):
    inventory = {}
    res = []

    for prod_id, change in zip(products, changes):
        inventory[prod_id] = inventory.get(prod_id, 0) + change
        max_current_qty = 0

        for qty in inventory.values():
            if qty > max_current_qty:
                max_current_qty = qty

        res.append(max_current_qty)
        
    return res

products = [101, 104, 101, 105]
changes = [4, 2, -4, 3]
result = solution(products, changes)
print(result)
