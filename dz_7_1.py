import os

ROOT = os.path.dirname(__file__)
DIR_NAME = "my_project"
DIR_PATH = os.path.join(ROOT, DIR_NAME)
SUBDIRS_TUP = ("settings", "mainapp", "adminapp", "authapp")

print("ROOT {}".format(ROOT))
print("DIR_PATH {}".format(DIR_PATH))
print("DIR_NAME {}".format(DIR_NAME))

# check if the main project dir exists
if not os.path.exists(DIR_PATH):
    os.makedirs(DIR_PATH)

for el in SUBDIRS_TUP:
    try:
        os.makedirs(os.path.join(DIR_PATH, el))
    except OSError as ex:
        print("Ошибка. Папка {} уже существует.".format(os.path.join(DIR_PATH, el)))
    except Exception as ex:
        print("Неизвестная ошибка {}".format(ex))
