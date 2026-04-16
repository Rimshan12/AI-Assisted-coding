###TASK:01
"""
import random
import time

# sample student record as dict
def make_student(i):
    return {
        "name": f"Student{i}",
        "roll": f"R{i:05d}",
        "cgpa": round(random.uniform(5.0, 10.0), 3)
    }

# generate n records
def gen_students(n):
    return [make_student(i) for i in range(1, n + 1)]

# merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["cgpa"] >= right[j]["cgpa"]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

# quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]["cgpa"]
    low = [x for x in arr if x["cgpa"] > pivot]
    equal = [x for x in arr if x["cgpa"] == pivot]
    high = [x for x in arr if x["cgpa"] < pivot]
    return quick_sort(low) + equal + quick_sort(high)

# top 10 display
def show_top(students, k=10):
    print(f"Top {k} students by CGPA:")
    for i, s in enumerate(students[:k], 1):
        print(f"{i:2d}. {s['name']} {s['roll']} {s['cgpa']:.3f}")

if __name__ == "__main__":
    data = gen_students(50000)  # large dataset
    d1 = list(data); d2 = list(data)

    t0 = time.perf_counter()
    r1 = quick_sort(d1)
    q_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    r2 = merge_sort(d2)
    m_time = time.perf_counter() - t0

    print(f"QuickSort: {q_time:.4f}s | MergeSort: {m_time:.4f}s")
    show_top(r1, 10)
"""
##TASK:02
"""
def bubble_sort(arr):
    n = len(arr)
    # Outer loop: each pass moves the next largest element to its final position
    for i in range(n):
        swapped = False
        # Inner loop: compare adjacent items and swap if out of order
        for j in range(0, n - 1 - i):
            # If left > right, swap to enforce ascending order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps happened in this pass, array is sorted; terminate early
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Before:", data)
    print("After :", bubble_sort(data))
"""
###TASK:03
"""
import random
import time

def quick_sort(arr):
 
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr):
     
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

def timeit(func, data):
    t0 = time.perf_counter()
    func(list(data))
    return time.perf_counter() - t0

def test_case(name, data):
    print(f"\n{name} (n={len(data)})")
    print(" Quick Sort :", timeit(quick_sort, data))
    print(" Merge Sort :", timeit(merge_sort, data))

if __name__ == "__main__":
    n = 30000
    random_data = [random.random() for _ in range(n)]
    sorted_data = sorted(random_data, reverse=True)
    reverse_data = list(reversed(sorted_data))

    test_case("Random", random_data)
    test_case("Sorted desc", sorted_data)
    test_case("Reverse sorted asc", reverse_data)

    print("\nComplexity summary:")
    print("Quick  : Best O(n log n), Avg O(n log n), Worst O(n^2)")
    print("Merge  : Best/Avg/Worst O(n log n)")
"""
###TASK:04
"""
products = [
    {"id":"P1","name":"Widget","price":19.99,"qty":120},
    {"id":"P2","name":"Gadget","price":9.99,"qty":350},
    {"id":"P3","name":"Widget","price":18.50,"qty":80},
]

# column-wise table
print(f"{'ID':<5}{'NAME':<10}{'PRICE':<8}{'QTY':<5}")
for p in products:
    print(f"{p['id']:<5}{p['name']:<10}{p['price']:<8.2f}{p['qty']:<5}")

# indexes for fast search
by_id = {p["id"]: p for p in products}
by_name = {}
for p in products:
    by_name.setdefault(p["name"].lower(), []).append(p)

print("\nSearch ID P2:", by_id.get("P2"))
print("Search name widget:", by_name.get("widget"))

# sort examples
sorted_by_price = sorted(products, key=lambda p: p["price"])
sorted_by_qty_desc = sorted(products, key=lambda p: p["qty"], reverse=True)

print("\nSorted by price (asc):")
for p in sorted_by_price:
    print(f"{p['id']} {p['price']:.2f}")

print("\nSorted by qty (desc):")
for p in sorted_by_qty_desc:
    print(f"{p['id']} {p['qty']}")
"""
###TASK:05
import random

stocks = []
for i in range(20):
    sym = f"S{i:03}"
    openp = round(random.uniform(10, 200), 2)
    closep = round(openp * random.uniform(0.9, 1.1), 2)
    change = round((closep - openp) / openp * 100, 2)
    stocks.append({"sym": sym, "open": openp, "close": closep, "change": change})

by_sym = {s["sym"]: s for s in stocks}
top5 = sorted(stocks, key=lambda x: x["change"], reverse=True)[:5]

print("Top 5 gainers:", [(x["sym"], x["change"]) for x in top5])
print("Search S005:", by_sym.get("S005"))