# TODO: gotta check syntax
def formatUsernamesFromArray(arr):
    str = ''
    for username in arr:
        str += username + ', '
    str = str[0, -2]
    return str