"""
Напишите скрипт который получает системный ввод от пользователя и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""

import sys

input_ = sys.stdin

if sys.argv[1] == 'sys.in':
    print('команда принята')
