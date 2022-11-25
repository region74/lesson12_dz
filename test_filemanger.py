import my_bank as b
import victory as v
from main import add_folder, copy_folder
import sys
import os
import shutil
import platform
import random
import pytest


def test_check_balance():
    assert b.check_balance(500, 200) == True
    assert b.check_balance(200, 400) == False


def test_get_date():
    assert v.get_date('09.03.1934') == 'девятое марта 1934 года'
    assert v.get_date('01.05.1977') == 'первое мая 1977 года'


# грязные функции
def test_add_folder():
    add_folder('test_folder')
    assert 'test_folder' in os.listdir()


def test_copy_folder():
    copy_folder('test_folder','test_folder_1')
    assert 'test_folder_1' in os.listdir()
