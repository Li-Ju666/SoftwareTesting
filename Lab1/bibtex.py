def extractauthor(str):
    result = str.split(sep = " ", maxsplit = 1)
    if len(result) < 2:
        result.extend(['']*(2-len(result)))
    else:
        result[0], result[1] = result[1], result[0]
    return result