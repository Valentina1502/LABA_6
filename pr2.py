#! /usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    tpl = lambda a, b: (a, b)
    p1 = tpl(1, 2)
    p2 = tpl(p1, 3)
    p3 = tpl(p1, p2)
    print(f'{p1} \n{p2} \n{p3}')
