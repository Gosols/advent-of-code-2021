from measurements import measurements

# 1.1

total = 0

for i in range(len(measurements)):
    if i == 0:
        continue
    previous = measurements[i - 1]
    current = measurements[i]

    if (current > previous):
        total += 1


print(total)

# 1.2

lul = 0

for i in range(len(measurements)):
    # start at the fourth measurement
    if i < 3:
        continue
    a1 = measurements[i - 3]
    a2 = measurements[i - 2]
    a3 = measurements[i-1]

    sum_of_a = a1+a2+a3

    b1 = measurements[i - 2]
    b2 = measurements[i - 1]
    b3 = measurements[i]

    sum_of_b = b1+b2+b3

    if sum_of_b > sum_of_a:
        lul += 1

print(lul)
