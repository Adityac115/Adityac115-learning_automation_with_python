#!/usr/bin/env python3.10
import os
import subprocess

def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(os.path.join(path, name))
    return files

def convertImageToText(img_file):
    #process = subprocess.Popen(['tesseract', img_file,
    #    ''.join(img_file.rsplit('.png', 1))])
    os.system(f"tesseract {img_file} {''.join(img_file.rsplit('.png', 1))}")


def startOperation():
    list_file = list_files(".")
    print(list_file)
    for img_file in list_file:
        if img_file.lower().split(".")[-1] == "png":
            convertImageToText(img_file)

startOperation()