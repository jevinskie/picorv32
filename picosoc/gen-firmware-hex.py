#!/usr/bin/env python3

import sys

bytes_total = 16*1024*1024
bytes_left = bytes_total
with open(sys.argv[1], 'w') as fw:
	for i in range(0x100000//4):
		fw.write('00 00 00 00\n');
		bytes_left -= 4
	fw.write('93 00 00 00\n');
	fw.write('93 01 00 00\n');
	bytes_left -= 8
	for i in range(bytes_left//4):
		fw.write('00 00 00 00\n');
