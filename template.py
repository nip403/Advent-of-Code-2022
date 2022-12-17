import os

def getinput():
    with open(os.path.split(__file__)[0] + "\\input.txt", "r") as f:
        data = f.read().rstrip().split("\n")

    return data

def part1():
    data = getinput()
    return

def part2():
    data = getinput()
    return
    
if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())