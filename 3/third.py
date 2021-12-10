from binaries import binary_list

""" binary_list = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
] """

ox_gen_rating = 0
co_scrub_rating = 0


# oxygen
# co2


def iterate_binaries(list, rating):
    for i in range(12):
        print(list)
        ones = 0
        zeros = 0

        # count which ones are more, 1's or 0's
        for binary in list:

            bit = int(binary[i])

            if bit == 0:
                zeros += 1
            else:
                ones += 1

        print("zeros: " + str(zeros)+", ones: " + str(ones))
        the_one_to_remove = ""

        # if calculating oxygen rating bullshit...
        if rating == "oxygen":
            if zeros == ones:
                the_one_to_remove = "0"
            else:
                the_one_to_remove = "1" if zeros > ones else "0"

        # if calculating co2 fuckshit...
        else:  # co2
            if zeros == ones:
                the_one_to_remove = "1"
            else:
                the_one_to_remove = "1" if zeros < ones else "0"

        # remove every binary with the lesser bit in current index...
        binaries_to_remove = []
        for binary in list:
            if the_one_to_remove == "":
                print("homo lol")
            if len(list) == 1:
                break
            bit = str(binary[i])
            if bit == the_one_to_remove:
                print("remove-->" + str(binary))
                binaries_to_remove.append(binary)

        for binary in binaries_to_remove:
            list.remove(binary)


remaining_binaries = binary_list.copy()

print("-----------------------")
print("---Oxygen gen rating---")
print("-----------------------")
while len(remaining_binaries) > 1:
    iterate_binaries(remaining_binaries, "oxygen")


ox_gen_rating = remaining_binaries[0]

remaining_binaries = binary_list.copy()

print("-----------------------")
print("--co2 scrubber rating--")
print("-----------------------")
while len(remaining_binaries) > 1:
    iterate_binaries(remaining_binaries, "co2")

co_scrub_rating = remaining_binaries[0]

result = int(co_scrub_rating, 2) * int(ox_gen_rating, 2)

print(result)
