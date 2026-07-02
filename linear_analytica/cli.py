"""Linear Analytica — CLI entry point."""

import argparse
from .navigator import lookup, list_signs, analyse_tablet


def main():
    parser = argparse.ArgumentParser(description='Linear Analytica — structural cipher decoder')
    sub = parser.add_subparsers(dest='command')

    p_lookup = sub.add_parser('lookup', help='Look up a Linear A sign')
    p_lookup.add_argument('code', help='Sign code (e.g. AB001)')

    p_list = sub.add_parser('list', help='List signs')
    p_list.add_argument('--category', '-c', help='Filter by semantic category')

    p_tablet = sub.add_parser('tablet', help='Analyse a tablet transcription')
    p_tablet.add_argument('transcription', help='Space-separated sign codes')

    args = parser.parse_args()

    if args.command == 'lookup':
        result = lookup(args.code)
        print(f"Sign {result['sign_code']}: {result['semantic']}")
        print(f"  Tuple: {''.join(result['tuple'])}")
        print(f"  Accounting role: {result['accounting_role'] or 'none'}")

    elif args.command == 'list':
        signs = list_signs(args.category)
        for s in signs:
            role = f" [{s['accounting_role']}]" if s['accounting_role'] else ''
            print(f"{s['sign_code']}: {s['semantic']:20s}{role}  {''.join(s['tuple'])}")

    elif args.command == 'tablet':
        result = analyse_tablet(args.transcription)
        print(f"Transcription: {result['transcription']}")
        print(f"Signs: {result['sign_count']}")
        print(f"Aggregators: {result['aggregators']}")
        print(f"Deficits: {result['deficits']}")
        print(f"Surpluses: {result['surpluses']}")
        print(f"Is accounting: {result['is_accounting']}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
