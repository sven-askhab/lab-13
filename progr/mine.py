#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def book_info(**kwargs):
    """
    Собирает информацию о книге в словарь
    """
    book_details = {}

    for key, value in kwargs.items():
        book_details[key] = value

    return book_details


def main():
    """
    Главная функция программы
    """
    book_details = book_info(
        title="Дюна",
        author="Фрэнк Герберт",
        year=1965,
        genre="Фантастика",
        pages=704
    )

    print(book_details)

if __name__ == "__main__":
    main()