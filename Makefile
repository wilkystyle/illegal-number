.PHONY: clean

main_reversed: main_decimal.txt
	uvx python dec_to_bin.py main_decimal.txt main_reversed
	chmod 700 main_reversed

main_decimal.txt: main
	uvx python bin_to_dec.py main main_decimal.txt

main:
	cc -Os main.c -o main

clean:
	rm -f main main_decimal.txt main_reversed
