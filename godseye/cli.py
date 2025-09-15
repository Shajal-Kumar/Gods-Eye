import argparse
import sys
from .banner import show_banner

class CustomHelpFormatter(argparse.RawTextHelpFormatter):
    def add_subparsers(self, action):
        # Override to show subcommand arguments automatically
        for name, subparser in action.choices.items():
            # add a blank line for spacing
            self._add_item(lambda x: "\n", [])
            self._add_item(self._format_subparser, [subparser])
        return super().add_subparsers(action)

    def _format_subparser(self, parser):
        help_text = parser.format_help()
        # indent each line by 2 spaces
        indented = "\n".join("  " + line for line in help_text.splitlines())
        return indented + "\n"

def search(args):
    print(f"[+] Starting new search for: {args.name}")
    if args.username:
        print(f"    Username Hint: {args.username}")
    if args.location:
        print(f"    Location Hint: {args.location}")
    if args.employer:
        print(f"    Employer Hint: {args.employer}")
    if args.email:
        print(f"    Email Hint: {args.email}")
    # TODO: Call search orchestrator here
    print("[!] Search Functionality Not Yet Implemented")

def view(args):
    print(f"[+] Viewing runs (filtered by run_id={args.run_id})")
    # TODO: Fetch and display runs from database
    print("[!] View Functionality Not Yet Implemented")

def export(args):
    print(f"[+] Exporting run data for run {args.run_id} to {args.format.upper()}")
    # TODO: Render Dossier
    print("[!] Export Functionality Not Yet Implemented")

def delete(args):
    print(f"[+] Deleting run {args.run_id}")
    # TODO: Delete run from database
    print("[!] Delete Functionality Not Yet Implemented")

def main():
    show_banner("GOD\'S EYE")
    parser = argparse.ArgumentParser(
        prog="godseye",
        description="Look up anyone, anywhere, anytime.",
        epilog=(
            "Examples:\n"
            "  godseye search -n \"John Doe\" -l \"New York\" -e \"Google\"\n"
            "  godseye view -r 12345\n"
            "  godseye export -r 12345 -f pdf\n"
            "  godseye delete -r 12345"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(title="commands", dest="command")

    search_parser = subparsers.add_parser(
        "search",
        help="Start a new investigation",
    )
    search_parser.add_argument("-n", "--name", required=True, help="Target's full name")
    search_parser.add_argument("-u", "--username", help="Known username/handle")
    search_parser.add_argument("-l", "--location", help="Known location/city/region")
    search_parser.add_argument("-e", "--employer", help="Known employer/workplace")
    search_parser.add_argument("-m", "--email", help="Known email address")
    search_parser.add_argument("-nc", "--no-cache", action="store_true", help="Ignore cached results")
    search_parser.set_defaults(func=search)

    view_parser = subparsers.add_parser(
        "view",
        help="View past investigations"
    )
    view_parser.add_argument("-r", "--run-id", type=int, help="Run idetifier to filter results")
    view_parser.set_defaults(func=view)

    export_parser = subparsers.add_parser(
        "export",
        help="Export a dossier"
    )
    export_parser.add_argument("-r", "--run-id", required=True, help="Run identifier to export")
    export_parser.add_argument("-f", "--format", choices=["pdf", "html"], default="html", help="Export format")
    export_parser.set_defaults(func=export)

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a run and its data"
    )
    delete_parser.add_argument("-r", "--run-id", required=True, help="Run identifier to delete")
    delete_parser.set_defaults(func=delete)

    args = parser.parse_args()
    if not vars(args).get("func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)

if __name__ == "__main__":
    main()

