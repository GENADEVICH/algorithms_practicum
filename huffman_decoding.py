def huffman_decode(symbol_count, encoded_length, codes, encoded_string):

    # Инвертируем словарь кодов для быстрого поиска символа по коду
    reverse_codes = {code: char for char, code in codes.items()}

    # Декодируем строку
    decoded_string = ""
    buffer = ""

    for bit in encoded_string:
        buffer += bit
        if buffer in reverse_codes:
            decoded_string += reverse_codes[buffer]
            buffer = ""

    return decoded_string

# Входные данные
symbol_count = 12
encoded_length = 60
codes = {
    ' ': '1011',
    '.': '1110',
    'D': '1000',
    'c': '000',
    'd': '001',
    'e': '1001',
    'i': '010',
    'm': '1100',
    'n': '1010',
    'o': '1111',
    's': '011',
    'u': '1101'
}
encoded_string = "100011110001001101000111111011001010011000010110011010111110"

# Вызов функции
decoded_string = huffman_decode(symbol_count, encoded_length, codes, encoded_string)
print(decoded_string)
