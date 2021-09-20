#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    line = list(input('Введите строку: '))
    count = 0
    for i, gl in enumerate(line):
        if gl in vowels:
            count += 1
    print(count)