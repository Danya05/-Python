import random
from string import ascii_letters, digits
from re import fullmatch, search


class EmailValidator:
    @classmethod
    def get_random_email(cls):
        length = random.randint(3, 50)
        email = ''
        for i in range(length):
            email += random.choice(ascii_letters + digits)
        return email + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        return cls.__is_email_str(email) and len(email) <= 100 and len(email.split('@')[0]) <= 50 and \
               search('[.]', email.split('@')[1]) is not None and search('[.]{2}', email) is None and \
               fullmatch(r'.+@.+', email) is not None

    @classmethod
    def __is_email_str(cls, email):
        return type(email) == str

    def __new__(cls, *args, **kwargs):
        return None
