import sys

sys.set_int_max_str_digits(0)

if len(sys.argv) != 3:
    print(f"usage: {sys.argv[0]} INPUT_DECIMAL_FILE OUTPUT_BINARY_FILE")
    sys.exit(1)

input_decimal = sys.argv[1]
output_binary = sys.argv[2]

with open(input_decimal) as f:
    length = int(f.readline().strip())
    n = int(f.readline().strip())

data = n.to_bytes(length, byteorder="big")

with open(output_binary, "wb") as f:
    f.write(data)
