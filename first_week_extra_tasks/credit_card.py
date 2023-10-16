def maskify(cc):
    if len(cc) < 4:
        return cc
    else:
        result = ''
        count = 0
        while count != len(cc) - 4:
            result += '#'
            count += 1
    return result + cc[-4:]

print(maskify('123'))
