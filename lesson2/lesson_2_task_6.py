lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
result = []
for nomb in lst:
    if nomb < 30 and nomb % 3 == 0:
        result.append(nomb)
print(result)
