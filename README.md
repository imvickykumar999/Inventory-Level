# Inventory Management

## Problem Statement

You are given two integer arrays:

* `products`, where `products[i]` represents the product ID being updated at step `i`
* `changes`, where `changes[i]` represents the stock change for that product:

  * positive value → stock added
  * negative value → stock removed

Return an integer array `inventory_status` of length `n`, where:

* `inventory_status[i]` is the **highest stock quantity among all products after the i-th update**
* If the inventory becomes empty, then `inventory_status[i] = 0`

---

## Function Signature

```python
def inventoryManagement(products: List[int], changes: List[int]) -> List[int]:
```

---

## Input

* `products`: integer array of length `n`
* `changes`: integer array of length `n`

---

## Output

* Return an integer array `inventory_status` of length `n`

---

## Example 1

### Input

```python
products = [101, 104, 101, 105]
changes = [4, 2, -4, 3]
```

### Output

```python
[4, 4, 2, 3]
```

### Explanation

* After update 0: Product `101` has `4` units → max stock = `4`
* After update 1: Product `101` has `4`, product `104` has `2` → max stock = `4`
* After update 2: Product `101` removed completely, product `104` has `2` → max stock = `2`
* After update 3: Product `105` has `3`, product `104` has `2` → max stock = `3`

---

## Example 2

### Input

```python
products = [150, 150, 120]
changes = [5, -5, 2]
```

### Output

```python
[5, 0, 2]
```

### Explanation

* After update 0: Product `150` has `5` units → max stock = `5`
* After update 1: Product `150` removed completely → inventory empty → `0`
* After update 2: Product `120` has `2` units → max stock = `2`

---

## Constraints

* The stock level of any product will never become negative.

---

## Efficient Approach Hint 🚀

Because `n` can be as large as **100,000**, an efficient solution should use:

* **HashMap / Dictionary** → track stock of each product
* **Max Heap / Counter optimization** → quickly find current maximum stock

Target complexity:

* **O(n log n)** preferred
* **O(n²)** will timeout
