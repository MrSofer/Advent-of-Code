with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

rotations = content.split()


def parse_rotation(rotation: str) -> int:
    assert rotation[0] in ["L", "R"] and str.isnumeric(rotation[1:])
    return (-1) ** (int(rotation[0] == "L")) * int(rotation[1:])

rotations = [parse_rotation(rotation) for rotation in rotations]

dial = 50

def Part1(dial):

    ret = 0

    for i in range(len(rotations)):
        dial = (dial + rotations[i]) % 100
        ret += int(dial == 0)

    print("For day 1, the password is", ret)

def Part2(dial:int) -> None:

    ret = 0

    for i in range(len(rotations)):
        #dial is a number between 0 and 99
        ret -= int(dial==0 and rotations[i] <= 0)
        dial += rotations[i]
        ret += abs(dial) // 100 + int(dial <= 0) #above or equal to 100 : add abs(dial) // 100, below or equal to 0 : add abs(dial)//100 + 1 (unless we were at 0)
        dial %= 100
    print("For day 2, the password is", ret)

Part1(dial)
Part2(dial)