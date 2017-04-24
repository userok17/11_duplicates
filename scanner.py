import os

class ScannerFiles:
    def __init__(self):
        self.list_files = {}
        
    def search(self, path):
        if not os.path.isdir(path):
            return None
        for item in os.listdir(path):
            filepath = os.path.join(path, item)
            if os.path.isdir(filepath):
                self.search(filepath)
                continue
            self.__add_file(filepath)
            
    def print_duplicates(self):
        if not self.list_files:
            return None
        for key, value in self.list_files.items():
            if not self.__has_duplicates(value['filespath']):
                continue
            print('Найдены дубликаты файла: {}'.format(value['filename']))
            print('Размер: {}'.format(value['size']))
            filespath = '\n'.join(value['filespath'])
            print('Пути к директориям:\n{}'.format(filespath))
            print()
        self.list_files = []

    def __add_file(self, filepath):
        filename = os.path.split(filepath)[1]
        filesize = os.path.getsize(filepath) 
        file_id = '{}{}'.format(filename, filesize) 
        if file_id not in self.list_files: 
            self.list_files[file_id] = {
                'file_id': file_id,
                'filename': filename,
                'size': self.__get_format_size(filesize),
                'filespath': [filepath]
            }
        else:
            self.list_files[file_id]['filespath'].append(filepath)
                
    def __get_format_size(self, size):
        if size < 1024:
            return '{} {}'.format(size, 'bytes')
        elif size < 1048576:
            size_kb = round(size/1024, 2)
            return '{} {}'.format(size_kb, 'KB')
        else:
            size_mb = round(size/1048576, 2)
            return '{} {}'.format(size_mb, 'MB')

    def __has_duplicates(self, files):
        return len(files) > 1

