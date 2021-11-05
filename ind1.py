#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def f1():
    def f2(p):
        result = p + 3
        return result
    return f2


if __name__ == '__main__':
    cnt = f1()
    k = int(input('Введите число \n'))
    print(f'Результат вычислений: {cnt(k)}')
