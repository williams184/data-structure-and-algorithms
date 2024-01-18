def convert_to_roman(num):
    roman_numerals = [
        {"symbol": 'M', "value": 1000},
        {"symbol": 'CM', "value": 900},
        {"symbol": 'D', "value": 500},
        {"symbol": 'CD', "value": 400},
        {"symbol": 'C', "value": 100},
        {"symbol": 'XC', "value": 90},
        {"symbol": 'L', "value": 50},
        {"symbol": 'XL', "value": 40},
        {"symbol": 'X', "value": 10},
        {"symbol": 'IX', "value": 9},
        {"symbol": 'V', "value": 5},
        {"symbol": 'IV', "value": 4},
        {"symbol": 'I', "value": 1},
    ]

    result = ''
    for key in roman_numerals:
        while num >= key["value"]:
            result += key["symbol"]
            num -= key["value"]

    return result

result = convert_to_roman(36)
print(result)
