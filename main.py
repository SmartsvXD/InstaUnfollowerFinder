import argparse

parser = argparse.ArgumentParser("main")
parser.add_argument(
    "-t", "--terminal", help="Launches the app in terminal mode.", type=bool
)

args = parser.parse_args()

if args.terminal:
    import src.cli as cli

    cli.main()
else:
    import src.gui as gui

    gui.main()