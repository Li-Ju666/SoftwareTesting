def extractauthor(str):
    if str.find(",") == -1:
        result = str.split(sep = " ")
        if len(result) > 1:
            first_name = ''
            for i in range(len(result)-1):
                first_name = first_name + result[i] + " "
            first_name = first_name[:-1]
            surname = result[-1]
            result = [surname, first_name]
        if len(result) < 2:
            result.extend(['']*(2-len(result)))
    else:
        result = str.split(sep = ", ")
    return result

def extractauthors(str):
    result = str.split(" and ")
    for i in range(len(result)):
        result[i] = tuple(extractauthor(result[i]))
    return result
