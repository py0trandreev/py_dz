import os
import shutil

ROOT = os.path.dirname(__file__)
DIR_NAME = "my_project"
DIR_PATH = os.path.join(ROOT, DIR_NAME)
TEMPLATE_DIR = "templates"
FULL_PATH_TO_TEMLATE = os.path.join(DIR_PATH, TEMPLATE_DIR)


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


for root, dirs, files in os.walk(DIR_PATH):
    for dir in dirs:
        full_path_to_dir = os.path.join(root, dir)
        if dir == "templates" and FULL_PATH_TO_TEMLATE != full_path_to_dir:
            print("dir {}".format(dir))
            full_path_to_dir = os.path.join(root, dir)
            print("___ {}".format(full_path_to_dir))
            try:
                copytree(full_path_to_dir, FULL_PATH_TO_TEMLATE)
            except FileExistsError as ex:
                print("Файл уже существует")

try:
    os.makedirs(os.path.join(DIR_PATH, TEMPLATE_DIR))
except OSError as ex:
    print("Ошибка. Папка {} уже существует.".format(os.path.join(DIR_PATH, TEMPLATE_DIR)))
except Exception as ex:
    print("Неизвестная ошибка {}".format(ex))
