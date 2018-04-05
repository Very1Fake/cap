import cap
import time


config = {
    'long-keys': 'allow',
    'none-value': 'N',
    'delay': 0,
    'keys-limit': 1
}

Parser = cap.cap(config)
temp = time.time()
x, y, z = Parser.getArgs()
time = (time.time() - temp) * 1000.0

args = 'Arguments:\n'
keys = 'Keys:\n'
long_keys = 'Long Keys:\n'

for i in x:
    args += i + '\n'

for i in y:
    keys += i + '\n'

for i in z:
    long_keys += i + ': ' + z[i] + '\n'

print('\n' + args + '\n' + keys + '\n' + long_keys)
print('\n\n' + 'Total time: ' + str(float(time)))
