import re


def is_url(cad):
    if re.fullmatch("((http|https)://)?[a-zA-Z0-9\.\/\?\:@\\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", cad) is not None:
        return True
    return False


print(is_url("http://exampleweb.com"))
