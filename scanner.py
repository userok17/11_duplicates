import os

class ScannerFiles:
    def __init__(self):
        self.list_duplicates = {}
        
    def search(self, path):
        '''
        Сканирование файлов
        '''
        if not os.path.isdir(path):
            return None
        for item in os.listdir(path):
            filepath = os.path.join(path, item)
            if os.path.isdir(filepath):
                self.search(filepath)
            filesize = os.path.getsize(filepath) # Размер файла
            file_id = '{}{}'.format(item, filesize) # Уникальный идентификатор
            if file_id not in self.list_duplicates: # если нету уникального идентификатора, то создать
                self.list_duplicates[file_id] = {
                    'file_id': file_id,
                    'filename': item,
                    'size': self.__get_format_size(filesize),
                    'filespath': [filepath]
                }
            else:
                self.list_duplicates[file_id]['filespath'].append(filepath)
                
                
    def __get_format_size(self, size):
        '''
        Перевести размер файла в человеческий вид
        '''
        if size < 1024:
            return '{} {}'.format(size, 'bytes')
        elif size < 1048576:
            size_kb = round(size/1024, 2)
            return '{} {}'.format(size_kb, 'KB')
        else:
            size_mb = round(size/1048576, 2)
            return '{} {}'.format(size_mb, 'MB')
        

    def print_duplicates(self):
        '''
        Вывести на экран дубликаты файлов
        '''
        for key, value in self.list_duplicates.items():
            if len(value['filespath']) < 2:
                continue
            
            print('Найдены дубликаты файла: {}'.format(value['filename']))
            print('Размер: {}'.format(value['size']))
            filespath = '\n'.join(value['filespath'])
            print('Пути к директориям:\n{}'.format(filespath))
            print()
