import sys


class Cli_Argv_Parser:
    # Errors
    def BadConfig(Exception):
        pass

    def checkConfig(self, config):
        try:
            if not config['none-value']:
                config['none-value'] = 'None'
        except KeyError:
            config['none-value'] = 'None'

        return config

    def __init__(self, config=None):
        if config is None:
            self.BadConfig()
        else:
            self.config = self.checkConfig(config)

    def getArgv(self, argv=None):
        if self.config['long-keys'] == 'value':
            long_keys = {}
        keys = []
        args = []
        z = 0

        if argv is None:
            argv = sys.argv

        while True:
            z += 1
            try:
                if argv[z][:2] == '--' and self.config['long-keys'] != 'deny':
                    if self.config['long-keys'] == 'value':
                        try:
                            long_keys[argv[z][2:]] = argv[z+1]
                        except IndexError:
                            long_keys[argv[z][2:]] = self.config['none-value']
                        z += 1
                    else:
                        keys.append(argv[z])
                elif argv[z][:1] == '-':
                    temp = list(argv[z][1:])
                    for n in temp:
                        keys.append(n)
                else:
                    args.append(argv[z])
            except IndexError:
                break

        if self.config['long-keys'] != 'deny':
            return args, keys, long_keys
        else:
            return args, keys
