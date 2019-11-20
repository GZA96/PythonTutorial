import re


def is_email(cad_email):
    if re.fullmatch("[^@]+@[^@]+\\.[^@]+", cad_email) is not None:
        return True
    return False


print(is_email("alguien@somewhere.com"))
