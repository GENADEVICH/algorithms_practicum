import heapq
from collections import defaultdict, Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node.char is not None:
        code_map[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", code_map)
        build_codes(node.right, prefix + "1", code_map)

    return code_map


def huffman_encode(string):
    frequencies = Counter(string)
    tree = build_huffman_tree(frequencies)
    codes = build_codes(tree)

    encoded_string = ''.join(codes[char] for char in string)
    unique_chars = len(codes)
    encoded_length = len(encoded_string)

    print(f"{unique_chars} {encoded_length}")
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")

    print(encoded_string)
    return codes, encoded_string


def huffman_decode(encoded_length, codes, encoded_string):
    reverse_codes = {code: char for char, code in codes.items()}

    current_code = ""
    decoded_string = ""
    for bit in encoded_string:
        current_code += bit
        if current_code in reverse_codes:
            decoded_string += reverse_codes[current_code]
            current_code = ""

    print(decoded_string)
    return decoded_string



string = "Errare humanum est."
codes, encoded_string = huffman_encode(string)

encoded_length = len(encoded_string)
decoded_string = huffman_decode(encoded_length, codes, encoded_string)
