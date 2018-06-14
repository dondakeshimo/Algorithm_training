L_n_m = [int(i) for i in input().split()]
lines = []
position = 1
next_position = 1
height = L_n_m[0]

for l in range(L_n_m[2]):
    lines.append([int(i) for i in input().split()])

while not (height==0):
    for a, b, c in lines:
        if (position == a and height == b):
            next_position = a + 1
            next_height = c - 1
        elif (position == a+1 and height == b):
            next_position = a
            next_height = c -1 
    if (position == next_position):
        height -= 1
    else:
        position = next_position
        height = next_height

print(position)

