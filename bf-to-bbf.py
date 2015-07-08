import sys

commands = {
  ">": "000",
  "<": "001",
  "+": "010",
  "-": "011",
  ".": "100",
  ",": "101",
  "[": "110",
  "]": "111"
}

# Read args
filename = ""
try:
  filename = sys.argv[1]
except Exception as e:
  print("Usage: python bf-to-bbf.py inputfile")
  sys.exit()

# Read the input file
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

# Code is valid, "compile"
with open("out.bbf", "w") as out:
  for command in code:
    out.write(commands[command])

print("Done writing output to 'out.bbf'")
