import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

files = []

def list_all_files(path=Path('.')):
    for entry in path.iterdir():
        if entry.is_file():
            files.append(entry)
        elif entry.is_dir():
            list_all_files(entry)


def sorting_files(file):
    dict_path = Path('dict')
    dict_path.mkdir(exist_ok=True)
    for file in files:
        file_extension = file.suffix[1:]
        folder_path = dict_path / file_extension
        folder_path.mkdir(exist_ok=True)
        shutil.copy(str(file), str(folder_path / file.name))

def multi_thread(files):
    with ThreadPoolExecutor() as executor:
        executor.map(sorting_files, files)

if __name__ == '__main__':
    directory_path = Path('./picture')
    list_all_files(directory_path)
    multi_thread(files)


