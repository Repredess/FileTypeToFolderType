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
                extension = filename.split('.')[-1]  # Получаем расширение файла

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
    'Изображения': ['jpg', 'png', 'bmp', 'gif', 'tif', 'jpeg'],
    'Документы': ['doc', 'docx'],
    'Электронные таблицы': ['xls', 'xlsx'],
    'PDF-документы': ['pdf'],
    'Тестовый файл': ['txt'],
    'Архивы': ['zip', 'rar', '7z', 'gzip'],
    'Аудиофайлы': ['mp3', 'wav', 'midi', 'aac'],
    'Видеофайлы': ['mp4', 'avi', 'mkv', 'wmv', 'flv', 'mpeg', 'mow'],
    'Cтраницы из интернета': ['html', 'htm', 'mht'],
    'Презентации': ['ppt', 'pptx'],
    'Базы данных': ['mdb', 'accdb'],
    'Установочные файлы': ['dmg', 'exe', 'pkg'],
    'ISO-файлы': ['iso'],
    'Торрент-файлы': ['torrent'],
    'Сканированные документы(книга, журнал и пр.)': ['djvu'],
    'Электронные книги': ['fb2', 'epub', 'mobi'],
    'Файлы изображений/проектов Photoshop': ['psd']
}

with open('folder_path.json', 'r') as j:
    login_data = json.load(j)
    for key, value in login_data.items():
        if key == "folder_track":
            folder_track = value
        elif key == "folder_dest":
            folder_dest = value

# folder_track = "/Users/pc/Downloads"
# folder_dest = "/Users/pc/Downloads/Отсортированные файлы"

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
