import argparse
import sys
from tabulate import tabulate
from coffee_report.reader import read_files
from coffee_report.reports.report_registry import REPORTS

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    records = read_files(args.files)

    if args.report not in REPORTS:
        print(f"Error: Unknown report '{args.report}'")
        sys.exit(1)

    report_class = REPORTS[args.report]()
    result = report_class.generate(records)

    print(tabulate(result, headers=["Student", "Median Coffee Spent"], tablefmt="grid"))

if __name__ == "__main__":
    main()