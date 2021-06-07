def bear(berries):
    n = len(berries)
    if berries[0:n:2] > berries[1:n:2]:
        return berries[0:n:2]
    else:
        return berries[1:n:2]
# a -is from input.txt every string in array format
a = [4, 2, 5, 7]
print(bear(a))
# The bear function is ready,
point = sum(bear(a))
print(point)
# the point write to output.txt
