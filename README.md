# Anti-Duplicator

Cкрипт, который принимает на вход папку, просматривает все файлы в ней (и всех подпапках и под-под-...папках) и сообщает, если находит дубликаты.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash
python3 duplicates.py -p <path>

Найдены дубликаты файла: 1.mp4
Размер: 2.37 MB
Пути к директориям:
/home/user/devman/11_duplicates/video/bla/dsf/1.mp4
/home/user/devman/11_duplicates/video/bla/1.mp4
/home/user/devman/11_duplicates/video/1.mp4

Найдены дубликаты файла: femida.mp4
Размер: 8.99 MB
Пути к директориям:
/home/user/devman/11_duplicates/video/bla/dsf/aa/femida.mp4
/home/user/devman/11_duplicates/video/bla/dsf/aa/33/femida.mp4

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

