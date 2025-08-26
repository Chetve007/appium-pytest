s = "df122gk123dfgd124dfghjk1sdfg2db99"


def max_int(line: str) -> int:
    if not line:
        return 'Line is empty'
    nums = []
    num = ''
    for symbol in line:
        if symbol.isdigit():
            num += symbol
        else:
            if num:
                nums.append(int(num))
                num = ''
    if num:
        nums.append(int(num))
    print(f'In num: {num}')
    print(f'In nums: {nums}')
    if not nums:
        return "Line don't has digits"
    return max(nums)


assert max_int(s) == 124
assert max_int("") == 'Line is empty'
assert max_int("^$@^%^%#$#%^$&*^&$^JHJDHEJEHJDVbnbnbndgfhergh") == "Line don't has digits"
# print(max_int("73465734657346574365347865734657346573465783465783465783465734865734856734865734657346575673465734654375634756437563478567348657843265734657834657346573465743865734563478564378567348657438"))
assert max_int("73465734657346574365347865734657346573465783465783465783465734865734856734865734657346575673465734654375634756437563478567348657843265734657834657346573465743865734563478564378567348657438") == 73465734657346574365347865734657346573465783465783465783465734865734856734865734657346575673465734654375634756437563478567348657843265734657834657346573465743865734563478564378567348657438
assert max_int("fjghfd45.6hgjrt8999.34rgherh67ghjdf67.6") == 8999
assert max_int("67f89a78c69bfkgjfd7mgfn88f6jfhgjhg") == 89
assert max_int("0x011111111jghrj0x000111thgtrh") == 11111111
