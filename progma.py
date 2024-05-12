import os, shutil

def merge_folders(folder1, folder2):
    folders_in_folder1 = set(os.listdir(folder1))

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
                    new_item = f"{os.path.splitext(item)[0]}_dop{os.path.splitext(item)[1]}"
                    destination = os.path.join(folder1, new_item)
                    shutil.copy(source, destination)
                    print(f"Добавлено '_dop' к файлу: {item}")

    for item in os.listdir(folder2):
        source = os.path.join(folder2, item)

        if os.path.isdir(source) and item not in folders_in_folder1:
            print(f"Удаляем папку {item} из {folder2}")
            shutil.rmtree(source)

folder1 = input('Введите полный путь к первой папке(куда): ')
folder2 = input('Введите полный путь ко второй папке(откуда): ')
merge_folders(folder1, folder2)
