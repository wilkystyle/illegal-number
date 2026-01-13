# illegal-number
A simple repository for exploring the concept of an [illegal number](https://en.wikipedia.org/wiki/Illegal_number), using a simple "Hello, world" program written in C.

## About
The general idea behind this repo is that all executable software programs are a binary, and all binary values have a decimal representation. It should be possible, then, to convert an arbitrary executable binary to a (very large!) decimal number, then convert that decimal number back to a working binary executable.

## Usage

Assuming you have a C compiler and [uvx](https://docs.astral.sh/uv/getting-started/installation/) installed, you should be able to simply run `make` to execute the entire process end-to-end.

Here's what the `Makefile` is doing under the hood:

```bash
# Compile the Hello, World program to a binary named `main`
cc -Os main.c -o main

# Run the Python script to convert `main` to its decimal representation, saved
# in the file `main_decimal.txt`
uvx python bin_to_dec.py main main_decimal.txt

# Run the Python script to read in the decimal number in main_decimal.txt and
# write out a binary file named main_reversed.
uvx python dec_to_bin.py main_decimal.txt main_reversed

# Make the binary file executable
chmod 700 main_reversed
```

Once the above steps have been completed, both `main` and `main_reversed` will run successfully, printing the text "Hello, world!"
