"""Main."""
argv_message = ''
import sys
from cpu import *
import sys
if len(sys.argv) != 2:
    print(argv_message)
    sys.exit(1)
else:

    file_name = sys.argv[1]


cpu = CPU()

cpu.load(file_name)
cpu.run()
#to run python3 ls8.py sctest.ls8