import sys

print int(bin(int(sys.stdin.readline()))[::-1][:-2], 2)
