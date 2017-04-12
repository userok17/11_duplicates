from argparse import ArgumentParser
from scanner import ScannerFiles

def main():
    parser = ArgumentParser(description='Поиск дубликатов')
    parser.add_argument('-f', '--filepath', required=True, dest='filepath', help='Укажите директорию для поиска дупликатов')
    args = parser.parse_args()
    
    scanner = ScannerFiles()
    scanner.search(args.filepath)
    scanner.print_duplicates()
    
if __name__ == '__main__':
    main()
