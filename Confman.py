import argparse
# import json

directory = {""}
parser = argparse.ArgumentParser(
    prog="Confman",
    usage="%(prog)s [options]",
    epilog="Thanks for using this Python script!",
)
parser.add_argument(
    "-ad",
    "--directory",
    type=str,
    metavar="[PATH] or =[PATH]",
    help="Add a directory for you configuration",
)
args = parser.parse_args()

if args.directory:
    print(f"""Your configuration({args.directory}) is under control now!""")
