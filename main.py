import os
import datetime
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    def __init__(self):
        self.file_extensions = {
            'Изображения': ['jpg', 'png', 'bmp', 'gif', 'tif', 'jpeg', 'ico'],
            'Документы и электронные таблицы': ['xml', 'xlsx', 'xltx', 'xlt', 'tbl', 'docm', 'docx', 'xls', 'xsl',
                                                'xltm', 'doc'],
            'PDF-документы': ['pdf'],
            'Текстовые файлы': ['txt', 'text', 'tex', 'ttf', 'log', 'sub', 'apt', 'err', 'pwi'],
            'Архивы': ['zip', 'rar', '7z', 'gzip', 'bin', 'jar', 'tar'],
            'Аудиофайлы': ['mp3', 'wav', 'midi', 'aac', 'flac', 'alac', 'aac', 'wav'],
            'Видеофайлы': ['mp4', 'avi', 'mkv', 'wmv', 'flv', 'mpeg', 'mow'],
            'Cтраницы из интернета': ['html', 'htm', 'mht'],
            'Презентации': ['ppt', 'pptx'],
            'Файлы и базы данных': ['sql', 'dat', 'sav', 'mpp', 'csv', 'css', 'db', 'gbr', 'mdb', 'sqlite3', 'accdb',
                                    'nbp',
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

    def get_folders(self):
        self.folder_track = self.valid_path(txt='Введите полный путь до "грязной" папки:')
        while not self.folder_track:
            self.folder_track = self.valid_path(
                txt='Данный путь не существует в системе, введите корректный путь до "грязной" папки:')

        self.folder_dest = self.valid_path(
            txt='Введите полный путь до "чистой" папки(чтобы отсортировать в эту же папку: нажмите enter):')

        if self.folder_dest == '':
            self.folder_dest = self.folder_track

        elif not self.folder_dest:
            print("Данного пути не существует")
            while self.folder_dest != '' or self.folder_dest == False:
                self.folder_dest = self.valid_path(
                    txt='Введите полный путь до "чистой" папки(для сортировки в "грязную" папку: нажмите enter):')

    @classmethod
    def valid_path(cls, txt=''):
        path = input(f"{txt}\n").lstrip('\\')
        if os.path.exists(path):
            return path
        elif path == "":
            return ""
        else:
            return False

    def on_modified(self, event):
        # Проходимся по данным в папке:
        for filename in os.listdir(self.folder_track):
            flag = False
            new_filename = None
            extension = filename.split('.')[-1].lower()  # Получаем расширение файла

            # Если является файлом:
            if os.path.isfile(os.path.join(self.folder_track, filename)) and not filename.startswith(
                    '.') and not extension in ['lnk', 'url']:

                # Ищем наше расширение:
                for key, value in self.file_extensions.items():

                    # Если нашли его:
                    if extension in value:

                        # Если нет папки для расширения, то создаем ее:
                        if not os.path.exists(os.path.join(self.folder_dest, key)):
                            os.mkdir(os.path.join(self.folder_dest, key))

                        # Если папка есть и в ней уже есть файл с этим именем:
                        elif os.path.exists(os.path.join(self.folder_dest, key, filename)):
                            new_filename = f"{filename.split('.')[0]}({str(datetime.datetime.now()).replace('.', '-')})"

                            os.rename(os.path.join(self.folder_track, filename),
                                      (os.path.join(self.folder_track, f"{new_filename}.{extension}")))

                        if new_filename:
                            file = os.path.join(self.folder_track, f"{new_filename}.{extension}")
                            new_path = os.path.join(self.folder_dest, key, f"{new_filename}.{extension}")
                        else:
                            file = os.path.join(self.folder_track, filename)
                            new_path = os.path.join(self.folder_dest, key, filename)

                        os.rename(file, new_path)
                        flag = True
                        break

                if not flag:
                    try:
                        file = os.path.join(self.folder_track, filename)
                        new_path = os.path.join(self.folder_dest, filename)
                        os.rename(file, new_path)
                    except FileExistsError:
                        continue
    #
    # def on_any_event(self, event):
    #     print(event.event_type, event.src_path)
    #
    # def on_moved(self, event):
    #     print("on_moved", event.src_path)
    #
    # def on_opened(self, event):
    #     print("on_opened", event.src_path)
    #
    # def on_created(self, event):
    #     print("on_created", event.src_path)
    #
    # def on_deleted(self, event):
    #     print("on_deleted", event.src_path)


def main():
    event_handler = Handler()
    event_handler.get_folders()
    folder_track = event_handler.folder_track
    observer = Observer()
    observer.schedule(event_handler=event_handler, path=folder_track, recursive=True)
    observer.start()
    try:
        test = str(datetime.datetime.now()).replace('.', '-')
        os.mkdir(os.path.join(folder_track, test))
        os.rmdir(os.path.join(folder_track, test))
    except:
        print('Error !!!!!!!!')
    print('Sort is active')
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
    observer.join()


if __name__ == "__main__":
    main()

# /Users/pc/Downloads
# pyinstaller -F --name="FileTypeToFolderType" --icon=Custom-Icon.ico main.py
