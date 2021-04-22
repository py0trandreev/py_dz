src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[el_index] for el_index in range(1, len(src)) if src[el_index] > src[el_index-1]]
print(result)