# fh = open('bank.py') # relative path
fh = open('/Users/mehul.chopra/Documents/personal/training/curtly-python/bank.py') # absolute path

for line in fh:
  print(line.rstrip()) # it reads the line with the \n

fh.seek(0)

print('Reading again...')
for line in fh:
  print(line.rstrip())

fh.seek(0)
print('Reading again..')

print(fh.read()) # reads the entire file
# be careful. Reads the entire file in a str

fh.seek(0)
print('Reading again..')

lines = fh.readlines()
print(lines)
# be careful. Reads the entire file in a list