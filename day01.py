with open("DataDay01.txt", "r") as f:
    data = f.readlines()

increased1: int = 0
increased2: int = 0
decreased: int = 0
previous = None

# first part of the challenge
for i in data:
    i = int(i)
    try:
        if previous < i:
            increased1 += 1
            print(f"{i} (increased)")
        if previous > i:
            decreased += 1
            print(f"{i} (decreased)")
    except TypeError:
        print(f"{i} (N/A)")
    previous = i

# second part of the challenge
for i in range(len(data)):
    try:
        if (int(data[i + 1]) + int(data[i + 2]) + int(data[i + 3])) > (
            int(data[i]) + int(data[i + 1]) + int(data[i + 2])
        ):
            increased2 += 1
    except IndexError:
        pass


print(increased1, increased2)
