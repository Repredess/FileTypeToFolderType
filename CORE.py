import os
import datetime
from watchdog.events import FileSystemEventHandler
import SETTINGS as settings


class Handler(FileSystemEventHandler):

    def __init__(self):
        self.file_extensions = settings.get_extensions()

    def get_path(self) -> tuple:
        if settings.LANGUAGE == 'ru':
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

        elif settings.LANGUAGE == 'en':

            self.folder_track = self.valid_path(txt='Enter the full path to the "dirty" folder:')
            while not self.folder_track:
                self.folder_track = self.valid_path(
                    txt='This path does not exist in the system, enter the correct path to the "dirty" folder:')

            self.folder_dest = self.valid_path(
                txt='Enter the full path to the "clean" folder (to sort into the same folder: press enter):')

            if self.folder_dest == '':
                self.folder_dest = self.folder_track

            elif not self.folder_dest:
                print("This path does not exist")
                while self.folder_dest != '' or self.folder_dest == False:
                    self.folder_dest = self.valid_path(
                        txt='Enter the full path to the "clean" folder (to sort into the "dirty" folder: press enter):')

        return self.folder_track, self.folder_dest

    def get_folder_track(self):
        return self.folder_track

    def get_folder_dest(self):
        return self.folder_dest

    @classmethod
    def valid_path(cls, txt=''):
        path = input(f"{txt}\n").lstrip('\\')
        if os.path.exists(path):
            return path
        elif path == "":
            return ""
        else:
            return False

    def get_live_datetime(self) -> str:
        date = str(datetime.datetime.now()).replace(':', '|').replace('.', ',')
        return date

    def on_any_event(self, event) -> None:
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
                            new_filename = f"{filename.split('.')[0]}({self.get_live_datetime()})"

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

                # Файл с неизвестным расширением, пробуем переместить его в "чистую папку"
                if not flag:
                    try:
                        file = os.path.join(self.folder_track, filename)
                        new_path = os.path.join(self.folder_dest, filename)
                        os.rename(file, new_path)
                    except FileExistsError:
                        continue
    #
    # def on_modified(self, event):
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


def verify_language(txt=""):
    tmp = input(txt)
    while tmp not in ('en', 'ru'):
        tmp = input(f'Invalid language! {txt}')

    return tmp