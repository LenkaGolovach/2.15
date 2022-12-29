#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать новый текстовый файл, затем требуется узнать число ядер процессора,а потом
записать их в созданный файл, изменить имя файла на myproccesor.txt если его еще не существует,
если он существует, то выдать соответствующее сообщение.
"""

import os


if __name__ == "__main__":
    with open("newfile.txt", "w") as data:
        data.write(os.environ["NUMBER_OF_PROCESSORS"])
    check = os.path.exists("myproccesor.txt")
    if not check:
        os.rename("newfile.txt", "myproccesor.txt")
    else:
        print("Файл уже существует")