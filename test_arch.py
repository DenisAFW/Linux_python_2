# Дополнить проект тестами, проверяющими команды вывода списка файлов (l)
# и разархивирования с путями (x).

import subprocess

folderin = "/home/user/tst"
folderout = "/home/user/out"
folderext = "/home/user/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "2 files"), "test1 FAIL"


def test_step2():
    assert checkout(f"cd {folderout}; 7z x arx2.7z -o{folderext} -y", "Everything is Ok"), "test_2 FAIL"
