FIRST_TIME = False
LANGUAGE = 'en'

file_extensions_ru = {
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
    'JSON-файлы': ['json'],
    'Програмные файлы': ['js', 'py'],
    'VUE-файлы': ['vue']
}

file_extensions_en = {
    'Images': ['jpg', 'png', 'bmp', 'gif', 'tif', 'jpeg', 'ico'],
    'Documents and spreadsheets': ['xml', 'xlsx', 'xltx', 'xlt', 'tbl', 'docm', 'docx', 'xls', 'xsl',
                                   'xltm', 'doc'],
    'PDF-docs': ['pdf'],
    'Text files': ['txt', 'text', 'tex', 'ttf', 'log', 'sub', 'apt', 'err', 'pwi'],
    'Archives': ['zip', 'rar', '7z', 'gzip', 'bin', 'jar', 'tar'],
    'Audio files': ['mp3', 'wav', 'midi', 'aac', 'flac', 'alac', 'aac', 'wav'],
    'Video files': ['mp4', 'avi', 'mkv', 'wmv', 'flv', 'mpeg', 'mow'],
    'Internet pages': ['html', 'htm', 'mht'],
    'Presentations': ['ppt', 'pptx'],
    'Files and databases': ['sql', 'dat', 'sav', 'mpp', 'csv', 'css', 'db', 'gbr', 'mdb', 'sqlite3', 'accdb',
                            'nbp',
                            'db3'],
    'Setup files': ['dmg', 'exe', 'pkg', 'msi'],
    'ISO files, disk image files': ['iso', 'gho', 'ghs'],
    'Torrent files': ['torrent'],
    'Scanned documents (book, magazine, etc.)': ['djvu'],
    'E-books': ['fb2', 'epub', 'mobi'],
    'Photoshop Image/Project Files': ['psd'],
    'Fonts': ['fnt', 'fon', 'otf', 'ttf'],
    'Project and backup files': ['prj', 'v2i', 'sis', 'sav', 'bak', 'dmp'],
    'JSON-files': ['json'],
    'Program Files': ['js', 'py'],
    'VUE-files': ['vue']
}


def get_extensions() -> dict:
    if LANGUAGE == 'ru':
        return file_extensions_ru
    elif LANGUAGE == 'en':
        return file_extensions_en
