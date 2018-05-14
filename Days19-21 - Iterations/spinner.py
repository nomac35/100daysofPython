import itertools
import time
import sys

symbol = itertools.cycle('-\|/')

while True:
    sys.stdout.write('\r' + next(symbol))
    sys.stdout.flush()
    time.sleep(0.5)

