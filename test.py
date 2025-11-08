misc = [1, 2, 4.2, 98.349, 'Hello', 'World']

strings = []
numerics = []

# 1. List splitting
for elem in misc:
#     if elem.isalpha()    -> won't work!
    if type(elem) == str:
        strings.append(elem)
    else:
        numerics.append(elem)
        
# 2. Sorting
numerics.sort()
strings.sort()

# 3. Recombining
out = numerics + strings

print(out)