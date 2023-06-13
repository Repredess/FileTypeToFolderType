import time
import os
from watchdog.observers import Observer
import CORE as core
import SETTINGS as settings


def start_app() -> None:
    if settings.FIRST_TIME:
        settings.LANGUAGE = core.verify_language('Choose your language en/ru: ')
        settings.FIRST_TIME = False

    event_handler = core.Handler()
    event_handler.get_path()
    folder_track = event_handler.folder_track
    folder_dest = event_handler.folder_dest
    observer = Observer()
    observer.schedule(event_handler=event_handler, path=folder_track, recursive=True)
    observer.start()
    try:
        test = event_handler.get_live_datetime()
        os.mkdir(os.path.join(folder_track, test))
        os.rmdir(os.path.join(folder_track, test))
    except:
        print('Error !!!!!!!!')
    os.system('clear')
    print(f'Sort is active | {folder_track} -> {folder_dest}')
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
    observer.join()


def main():
    start_app()


if __name__ == "__main__":
    main()

# /Users/pc/Downloads
# pyinstaller -F --name="FileTypeToFolderType" --icon=Custom-Icon.ico main.py
