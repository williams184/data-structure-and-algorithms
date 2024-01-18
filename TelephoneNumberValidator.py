import re

def telephone_check(s):
    pattern = re.compile(r'^1?[-\s]?(\d{3}|\(\d{3}\))[-\s]?\d{3}[-\s]?\d{4}$')
    return pattern.match(s) is not None

result = telephone_check('555-555-5555')
print(result)
