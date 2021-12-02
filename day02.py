with open("Day02Data.txt", "r") as f:
    data = f.readlines()

horizontal: int = 0
vertical: int = 0
aim: int = 0

for line in data:
    direction, length = line.split(" ", maxsplit=2)
    length = int(length)
    if direction == "forward":
        horizontal += length
        vertical += aim * length
    if direction == "down":
        # vertical += length
        aim += length
    if direction == "up":
        # vertical -= length
        aim -= length

print(horizontal*vertical)
