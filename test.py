import cap
import time


config = {
    'long-keys': 'allow',
    'none-value': 'N',
    'delay': 0
}

Parser = cap.cap(config)
print(Parser.getArgs())

temp = time.time()
x, y, z = Parser.getArgs()
time = time.time() - temp

args = 'Arguments:\n'
keys = 'Keys:\n'
long_keys = 'Long Keys:\n'

for i in x:
    args += i + '\n'

for i in y:
    keys += i + '\n'

for i in z:
    long_keys += i + '\n'

print('\n' + args + '\n' + keys + '\n' + long_keys)
print('\n\n' + 'Total time: ' + str(long(time)))
