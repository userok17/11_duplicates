from argparse import ArgumentParser
from scanner import ScannerFiles

def main():
    parser = ArgumentParser(description='Поиск дубликатов')
    parser.add_argument('-p', '--path', required=True, dest='path', help='Укажите директорию для поиска дупликатов')
    args = parser.parse_args()
    
    scanner = ScannerFiles()
    scanner.search(args.path)
    scanner.print_duplicates()
    
if __name__ == '__main__':
    main()
