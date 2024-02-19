# Expansion table
expansion_table = [32, 1, 2, 3, 4, 5, 4, 5,
                   6, 7, 8, 9, 8, 9, 10, 11,
                   12, 13, 12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21, 20, 21,
                   22, 23, 24, 25, 24, 25, 26, 27,
                   28, 29, 28, 29, 30, 31, 32, 1]


# XOR operation
def xor(bitset1, bitset2):
    return [bit1 ^ bit2 for bit1, bit2 in zip(bitset1, bitset2)]


# Example keys K1 to K16
keys = [
    "101000001001001010100010100010011011011000010011",
    "101100001001001001000010101110010001001111111001",
    "101100000001101001010010111111110110011000100100",
    "001001000111001001010000001110000100101111001110",
    "000001100101010101010100100101001111000010010111",
    "010011100100000101010001111001110010011011100001",
    "000011111100000100101001101110101010101101001011",
    "100010110000000110001011001101101101011100010110",
    "001110010000101010001001010111010010010111100010",
    "001110010001100010001000010001001111001111110101",
    "000100000010100011001100011100111000110011101001",
    "000100000110110000010100110010101001110100011011",
    "010001000010110100100100000011110111011100111100",
    "110000101010010000100101011110010101100111100000",
    "110010011000011000100010110000001100100000111111",
    "111000001001001010101010110001110011111010011100"
]

# Example input R0
input_r0 = [0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 1,
            1, 1, 1, 0, 0, 0, 1, 1,
            1, 1, 1, 0, 0, 0, 1, 1]

# Start with R0 value
input_ri_minus_1 = input_r0

# Perform DES encryption for 16 rounds
for round_num in range(16):
    # Perform expansion E(Ri-1)
    expanded_ri_minus_1 = [input_ri_minus_1[i - 1] for i in expansion_table]

    # XOR with current key
    current_key = [int(bit) for bit in keys[round_num]]
    a1 = xor(expanded_ri_minus_1, current_key)

    print(f"Round {round_num + 1}:")
    print("Expanded E(Ri-1):", ''.join(map(str, expanded_ri_minus_1)))
    print("Key K{}: {}".format(round_num + 1, format(int(keys[round_num], 2), '048b')))
    print("A{}: {}\n".format(round_num + 1, ''.join(map(str, a1))))

    # Update Ri-1 for the next round
    input_ri_minus_1 = a1

