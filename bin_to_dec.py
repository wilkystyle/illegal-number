import sys

sys.set_int_max_str_digits(0)

if len(sys.argv) != 3:
    print(
        f"usage: {sys.argv[0]} INPUT_BINARY_FILE OUTPUT_DECIMAL_FILE",
        file=sys.stderr,
    )
    sys.exit(1)

input_binary = sys.argv[1]
output_decimal = sys.argv[2]

with open(input_binary, "rb") as f:
    data = f.read()

n = int.from_bytes(data, byteorder="big")

with open(output_decimal, "w") as f:
    f.write(f"{len(data)}\n")
    f.write(str(n))
