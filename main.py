from watchdog.observers import Observer
import os
import time
from datetime import datetime
from watchdog.events import FileSystemEventHandler
import simplejson as json


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        # Проходимся по данным в папке:
        for filename in os.listdir(folder_track):
            flag = False
            new_filename = None

            # Если является файлом:
            if os.path.isfile(os.path.join(folder_track, filename)) and not filename.startswith('.'):
                extension = filename.split('.')[-1].lower()  # Получаем расширение файла

                # Ищем наше расширение:
                for key, value in file_extensions.items():

                    # Если нашли его:
                    if extension in value:

                        # Если нет папки для расширения, то создаем ее:
                        if not os.path.exists(os.path.join(folder_dest, key)):
                            os.mkdir(os.path.join(folder_dest, key))

                        elif os.path.exists(os.path.join(folder_dest, key, filename)):
                            new_filename = str(datetime.now())
                            os.rename(os.path.join(folder_track, filename), (os.path.join(folder_track, f"{new_filename}.{extension}")))

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
                    file = os.path.join(folder_track, filename)
                    new_path = os.path.join(folder_dest, filename)
                    os.rename(file, new_path)


file_extensions = {
    'Изображения': ['jpg', 'png', 'bmp', 'gif', 'tif', 'jpeg', 'ico'],
    'Документы и электронные таблицы': ['xml', 'xlsx', 'xltx', 'xlt', 'tbl', 'docm', 'docx', 'xls', 'xsl', 'xltm', 'doc'],
    'PDF-документы': ['pdf'],
    'Текстовые файлы': ['txt', 'text', 'tex', 'ttf', 'log', 'sub', 'apt', 'err', 'pwi'],
    'Архивы': ['zip', 'rar', '7z', 'gzip', 'bin', 'jar'],
    'Аудиофайлы': ['mp3', 'wav', 'midi', 'aac', 'flac', 'alac', 'aac', 'wav'],
    'Видеофайлы': ['mp4', 'avi', 'mkv', 'wmv', 'flv', 'mpeg', 'mow'],
    'Cтраницы из интернета': ['html', 'htm', 'mht'],
    'Презентации': ['ppt', 'pptx'],
    'Файлы и базы данных': ['sql', 'dat', 'sav', 'mpp', 'csv', 'css', 'db', 'gbr', 'mdb', 'sqlite3', 'accdb', 'nbp', 'db3'],
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
# Чтение нужных библиотек из файла json

# with open('folder_path.json', 'r+', encoding="utf-8") as j:
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

folder_track = input("Введите полный путь отслеживаемой папки: \n")
folder_dest = input("Введите полный путь к папке для отсортированных файлов: \n")
time.sleep(1)
#################
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()
print('sort is active')

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Закрытие программы")
    observer.stop()

observer.join()

# pyinstaller -F --icon=Custom-Icon.ico main.py
