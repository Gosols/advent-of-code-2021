from input import input

horizontal = 0
depth = 0
aim = 0

for i in input:
    split_instruction = i.split(" ")

    instruction = split_instruction[0]
    amount = int(split_instruction[1])

    if instruction == "forward":
        # increases your horizontal position by X units.
        # increases your depth by your aim multiplied by X
        horizontal += amount
        if aim > 0:
            depth += (aim * amount)
    if instruction == "up":
        aim -= amount
    if instruction == "down":
        aim += amount

print(horizontal * depth)
