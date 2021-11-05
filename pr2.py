#! /usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    tpl = lambda a, b: (a, b)
    p1 = tpl(1, 2)
    print(f'{p1} \n ')
    p2 = tpl(p1, 3)
    print(f'{p2} \n')
    p3 = tpl(p1, p2)
    print(f'{p3} ')
