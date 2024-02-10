import random
import string

generated_codes = []

def generate_code():
    prefix = "B6"
    while True:
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        code = prefix + suffix
        if code not in generated_codes:
            generated_codes.append(code)
            return code
for i in range(1000):
    print(generate_code())
