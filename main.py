import sys
from stats import get_report

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
    report = get_report(sys.argv[1])
main()
