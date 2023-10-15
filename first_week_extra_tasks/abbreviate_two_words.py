def abbrev_name(name):
    names = name.split(' ');
    return f"{names[0][0]}.{names[1][0]}".upper()
