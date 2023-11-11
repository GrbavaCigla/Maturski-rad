import argparse
from .commands import record, plot, clean


COMMANDS = {"record": record, "plot": plot, "clean": clean}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    for name, module in COMMANDS.items():
        command = subparsers.add_parser(name)
        module.setup(command)

    args = parser.parse_args()

    if args.command in COMMANDS:
        COMMANDS[args.command].run(args)
    else:
        parser.print_usage()
