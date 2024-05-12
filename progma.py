import os, shutil
import tempfile


def merge_folders(folder1, folder2):
    for item in os.listdir(folder2):
        source = os.path.join(folder2, item)
        destination = os.path.join(folder1, item)

        if os.path.isdir(source):
            if not os.path.exists(destination):
                os.makedirs(destination)
            merge_folders(destination, source)
        else:
            if not os.path.exists(destination):
                shutil.copy(source, folder1)
            else:
                print(f"Файл {item} уже существует в {folder1}. Пропускаем...")


folder1 = input('введите полный путь к первой папке: ')
folder2 = input('введите полный путь ко второй папке: ')
merge_folders(folder1, folder2)
