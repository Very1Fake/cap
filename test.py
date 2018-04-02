import cli_argv_parser


config = {
    'long-keys': 'value',
}

Parser = cli_argv_parser.Cli_Argv_Parser(config)

print(Parser.getArgv())
x, y, z = Parser.getArgv()

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
