#!/usr/bin/env python3

import sys

offset = 0x100000
bytes_total = int(sys.argv[1])
bytes_left = bytes_total
with open(sys.argv[2], 'w') as fw:
	print('bytes_left: {}'.format(bytes_left))
	fw.write('00' * 0x100000 + '\n');
	bytes_left -= 0x100000
	print('bytes_left: {}'.format(bytes_left))
	fw.write('93 00 00 00\n');
	bytes_left -= 4
	fw.write('93 01 00 00\n');
	bytes_left -= 4
	print('bytes_left: {}'.format(bytes_left))
	fw.write('00' * bytes_left + '\n');
