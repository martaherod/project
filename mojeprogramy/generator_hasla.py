import string
import random

def password(n_signs):

    list_upper = string.ascii_uppercase
    list_lower = string.ascii_lowercase
    list_punctuation = string.punctuation
    list_number = string.digits

    password = ""
    for i in range(n_signs//4 +1):
        if len(password) == n_signs:
            continue
        password += random.choice(list_lower)
        if len(password) == n_signs:
            continue
        password += random.choice(list_upper)
        if len(password) == n_signs:
            continue
        password += random.choice(list_punctuation)
        if len(password) == n_signs:
            continue
        password += random.choice(list_number)
        if len(password) == n_signs:
            continue
    return "".join(random.sample(password,len(password)))