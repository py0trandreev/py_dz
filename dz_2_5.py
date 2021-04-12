prices = [57.8, 46.51, 97, 31.78, 700.5, 45.9, 123.10, 300, 32.35, 78.78]

# 5.A-5.B
for list_item in sorted(prices):
    rubles = int(list_item)
    kopecks = int(round(100 * (list_item % 1), 2))

    if sorted(prices).index(list_item) != len(prices) - 1:
        print(f"{rubles} руб {kopecks:02} коп", end=", ")
    else:
        print(f"{rubles} руб {kopecks:02} коп")

print(prices)

# 5.C
prices_desc_sorted = sorted(prices, reverse=True)
print(prices_desc_sorted)

# 5.D
print(sorted(prices_desc_sorted[:5]))
