#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z')+1):
  if ord(alpha_letters) ==101  or ord(alpha_letters) == 113:
    continue
    print("{:c}".format(alpha_letters), end="")
