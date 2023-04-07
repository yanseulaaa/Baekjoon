nums = []
for i in range(0,10): nums.append(int(input()))
mod = [val%42 for val in nums]
unique = set(mod)
print(len(unique))