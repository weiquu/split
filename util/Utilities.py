def formatUsernamesFromArray(arr):
    str = ''
    for username in arr:
        str += username + ', '
    str = str[:-2]
    return str