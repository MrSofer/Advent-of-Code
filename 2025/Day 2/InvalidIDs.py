
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()

IDs = content.split(",")

for i in range(len(IDs)):
    IDs[i] = IDs[i].split("-")

def sum_parts(lo, hi ,p,skip_repdigits = True):
    total = 0
    k = len(str(lo))
    while 10**(k-1) <= hi:
        a, b = max(lo, 10**(k-1)), min(hi, 10**k - 1)
        if a <= b:
            s = sum([10**(k*i) for i in range(p)])
            total += (a + b) * (b - a + 1) // 2 * s

            #taking into account d repeated numbers
            if skip_repdigits:
                q = ((10**k) - 1) // 9
                total -= sum(range((a-1)//q + 1,b//q + 1)) * (((10**(p*k))-1)//9)

        k += 1
    return total


PRIMES = {2,3,5,7,11} #assuming numbers are < 12 digits long and being extra safe


def sum_range(left:str,right:str,p : int) -> int:

    assert left.isnumeric() and right.isnumeric() and p in PRIMES

    total = 0
    left_digits, right_digits = len(left), len(right)

    if left_digits % p == 0:
        left_first = int(left[:left_digits // p])
        left_first += int(str(left_first) * p < left)
    else: left_first = 10**(left_digits // p)

    if right_digits % p == 0:
        right_first = int(right[:right_digits // p])
        right_first -= int(str(right_first) * p > right)
    else: right_first = 10**(right_digits//p) - 1 #int((right_digits // p) * "9")

    total += sum_parts(left_first,right_first,p)

    return total

def sum_d_repeating(lo:str,hi:str) -> int:

    assert lo.isnumeric() and hi.isnumeric()

    lo,hi = int(lo),int(hi)

    total = 0
    d = max(2,len(str(lo)))

    while 10**(d-1) <= hi:
        a, b = max(lo, 10 ** (d - 1)), min(hi, (10 ** d) - 1)
        q = ((10**d) - 1) // 9
        total += sum(range((a-1)//q + 1,b//q + 1)) * q

        d+=1

    return total



def part_one():

    ret = 0

    for left,right in IDs:

        if int(right) < 10:
            continue

        left_digits,right_digits = len(left),len(right)

        if left_digits % 2 == 0:
            left_first = int(left[:left_digits//2])
            left_second = int(left[left_digits//2:])
        else:
            left_first = 10**(left_digits//2)
            left_second = 0

        if right_digits % 2 == 0:
            right_first = int(right[:right_digits//2])
            right_second = int(right[right_digits//2:])
        else:
            right_first = int((right_digits//2) * "9")
            right_second = int((right_digits//2) * "9")

        left_first += int(left_first < left_second)
        right_first -= int(right_first > right_second)

        ret += sum_parts(left_first, right_first, 2,False)


    print(int(ret))

def part_two():
    ret = 0
    for l,r in IDs:
        for p in PRIMES:
            ret += sum_range(l,r,p)
        ret += sum_d_repeating(l,r)

    print(ret)
            



part_one()
part_two()

#print(IDs)