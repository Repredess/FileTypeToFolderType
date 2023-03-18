from watchdog.observers import Observer
import os
import time
from datetime import datetime
from watchdog.events import FileSystemEventHandler


# import simplejson as json


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        # Проходимся по данным в папке:
        for filename in os.listdir(folder_track):
            flag = False
            new_filename = None
            extension = filename.split('.')[-1].lower()  # Получаем расширение файла

            # Если является файлом:
            if os.path.isfile(os.path.join(folder_track, filename)) and not filename.startswith(
                    '.') and not extension in ['lnk', 'url']:

                # Ищем наше расширение:
                for key, value in file_extensions.items():

                    # Если нашли его:
                    if extension in value:

                        # Если нет папки для расширения, то создаем ее:
                        if not os.path.exists(os.path.join(folder_dest, key)):
                            os.mkdir(os.path.join(folder_dest, key))

                        elif os.path.exists(os.path.join(folder_dest, key, filename)):
                            new_filename = str(datetime.now()).replace('.', '-')
                            os.rename(os.path.join(folder_track, filename),
                                      (os.path.join(folder_track, f"{new_filename}.{extension}")))

                        if new_filename:
                            file = os.path.join(folder_track, f"{new_filename}.{extension}")
                            new_path = os.path.join(folder_dest, key, f"{new_filename}.{extension}")
                        else:
                            file = os.path.join(folder_track, filename)
                            new_path = os.path.join(folder_dest, key, filename)

                        os.rename(file, new_path)
                        flag = True
                        break

                if not flag:
                    try:
                        file = os.path.join(folder_track, filename)
                        new_path = os.path.join(folder_dest, filename)
                        os.rename(file, new_path)
                    except FileExistsError:
                        continue


file_extensions = {
    'Изображения': ['jpg', 'png', 'bmp', 'gif', 'tif', 'jpeg', 'ico'],
    'Документы и электронные таблицы': ['xml', 'xlsx', 'xltx', 'xlt', 'tbl', 'docm', 'docx', 'xls', 'xsl', 'xltm',
                                        'doc'],
    'PDF-документы': ['pdf'],
    'Текстовые файлы': ['txt', 'text', 'tex', 'ttf', 'log', 'sub', 'apt', 'err', 'pwi'],
    'Архивы': ['zip', 'rar', '7z', 'gzip', 'bin', 'jar', 'tar'],
    'Аудиофайлы': ['mp3', 'wav', 'midi', 'aac', 'flac', 'alac', 'aac', 'wav'],
    'Видеофайлы': ['mp4', 'avi', 'mkv', 'wmv', 'flv', 'mpeg', 'mow'],
    'Cтраницы из интернета': ['html', 'htm', 'mht'],
    'Презентации': ['ppt', 'pptx'],
    'Файлы и базы данных': ['sql', 'dat', 'sav', 'mpp', 'csv', 'css', 'db', 'gbr', 'mdb', 'sqlite3', 'accdb', 'nbp',
                            'db3'],
    'Установочные файлы': ['dmg', 'exe', 'pkg', 'msi'],
    'ISO-файлы, файлы образа диска': ['iso', 'gho', 'ghs'],
    'Торрент-файлы': ['torrent'],
    'Сканированные документы(книга, журнал и пр.)': ['djvu'],
    'Электронные книги': ['fb2', 'epub', 'mobi'],
    'Файлы изображений/проектов Photoshop': ['psd'],
    'Шрифты': ['fnt', 'fon', 'otf', 'ttf'],
    'Файлы проектов и резервных копий': ['prj', 'v2i', 'sis', 'sav', 'bak', 'dmp'],
    'JSON-файлы': ['json']
}


##################################
# Чтение нужных путей из json-файла:

# with open('dist/folder_path.json', 'r+', encoding="utf-8") as j:
#     login_data = json.load(j)
#     for key, value in login_data.items():
#         if key == "folder_track":
#             folder_track = value
#         elif key == "folder_dest":
#             folder_dest = value

###############################
# Ручная настройка brootforce:

# folder_track = "/Users/pc/Downloads"
# folder_dest = "/Users/pc/Downloads/Отсортированные файлы"

#################
# Ручная настройка в терминале:
def valid_path(txt=''):
    path = input(f"{txt}\n").lstrip('\\')
    if os.path.exists(path):
        return path
    elif path == "":
        return ""
    else:
        return False


folder_track = valid_path(txt='Введите полный путь до "грязной" папки:')
while not folder_track:
    folder_track = valid_path(txt='Данный путь не существует в системе, введите корректный путь до "грязной" папки:')

folder_dest = valid_path(txt='Введите полный путь до "чистой" папки(чтобы отсортировать в эту же папку: нажмите enter):')
if folder_dest == '':
    folder_dest = folder_track
elif not folder_dest:
    print("Данного пути не существует")
    while folder_dest != '' or folder_dest == False:
        folder_dest = valid_path(
            txt='Введите полный путь до "чистой" папки(для сортировки в "грязную" папку: нажмите enter):')

#################
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()
print('|sort is active|если сортировка не прошла добавьте любой файл в отслеживаемую папку')

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Закрытие программы")
    observer.stop()

observer.join()

# pyinstaller -F --name="FileTypeToFolderType" --icon=Custom-Icon.ico main.py
