# Mapping dictionary for encoding and decoding
mapping = {
    'aa': 'A',
    'ab': 'B',
    'ac': 'C',
    'ad': 'D',
    'ba': 'E',
    'bb': 'F',
    'bc': 'G',
    'bd': 'H',
    'ca': 'I',
    'cb': 'J',
    'cc': 'K',
    'cd': 'M',
    'da': 'L',
    'db': 'N',
    'dc': 'O',
    'dd': 'P'
}


# Function to reduce a 40-character string to a 20-character string
def reduce_to_20_characters(input_string):
    if len(input_string) != 40:
        raise ValueError("Input string must be 40 characters long")

    result = ""
    for i in range(0, 40, 2):
        pair = input_string[i:i + 2]
        if pair in mapping:
            result += mapping[pair]
        else:
            raise ValueError(f"Invalid pair: {pair}")

    return result


# Function to convert a 20-character string back to the original 40-character string
def convert_to_40_characters(input_string):
    if len(input_string) != 20:
        raise ValueError("Input string must be 20 characters long")

    result = ""
    for char in input_string:
        found = False
        for pair, replacement in mapping.items():
            if replacement == char:
                result += pair
                found = True
                break
        if not found:
            raise ValueError(f"Invalid character: {char}")

    return result


# Example usage:
original_string = "abbbdbacbcbbcdbacbbbbcdbbbbacbbbdaacdadb"
encoded_string = reduce_to_20_characters(original_string)
decoded_string = convert_to_40_characters(encoded_string)

print("Original String:", original_string)
print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
