#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_between_positive(*args):
    """
    Рассчет суммы аргументов между первым и вторым положи тельными аргументами
    """
    if args:
        values = [float(arg) for arg in args]

        first_pos = None
        second_pos = None

        for i, value in enumerate(values):
            if value > 0:
                if first_pos is None:
                    first_pos = i
                elif second_pos is None:
                    second_pos = i
                    break  

        if first_pos is None or second_pos is None:
            return None

        return(sum(values[first_pos + 1:second_pos]))
    
    else:
        return None


def main():
    '''
    Главная функция программы.
    '''
    print(sum_between_positive(3, -2, -4, 5, -7, 1))
    print(sum_between_positive(-1, -2, -3, -4, -5))
    print(sum_between_positive(8, 6, -1, -3, -4, 5))
    print(sum_between_positive())

if __name__ == "__main__":
    main()