import sys

commands = {
  "000": ">",
  "001": "<",
  "010": "+",
  "011": "-",
  "100": ".",
  "101": ",",
  "110": "[",
  "111": "]"
}

# Splits a string every 3 characters
def split(str):
  return [str[start:start + 3] for start in range(0, len(str), 3)]

# Read args
filename = ""
try:
  filename = sys.argv[1]
except Exception as e:
  print("Usage: python bbf-to-bf.py inputfile")
  sys.exit()

# Read code
with open(filename, "r") as inp:
  print("reading...")
  code = ""
  while True:
    c = inp.read(1)
    if not c:
      break
    code = code + c

# Remove spaces from string
code = code.replace(" ", "").replace("\n", "")

# If the code size is not a mod 3, stop
if len(code) % 3 != 0:
  print("Invalid code")
  sys.exit()

# Code is valid, "compile"
with open("out.b", "w") as out:
  split_code = split(code)
  for command in split_code:
    out.write(commands[command])

print("Done writing output to 'out.b'")
