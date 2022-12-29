#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла и выводит на экран сначала
вопросительные, а затем восклицательные предложения.
"""

if __name__ == "__main__":
    with open("ind1.txt", "r") as txt:
        content = txt.readlines()
        content.reverse()
        count = 0
        for vop in content:
            if '?' in vop:
                print(vop)
        for vosk in content:
            if '!' in vosk:
                print(vosk)