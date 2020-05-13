def toRoman(number):
    number = number
    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = ''

    factors = []

    for letter in romans.keys():
        while romans[letter] <= number:
            result += letter
            number -= romans[letter]
    
    return result
