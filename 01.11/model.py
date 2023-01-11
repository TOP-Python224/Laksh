"""Модель MVC."""

from pathlib import Path
import re


class Email:
    """Описывает модель взаимодействия и хранения email адресов."""
    file_path: str | Path = 'emails.txt'
    
    def __init__(self, email: str):
        self.email = email

    @property
    def email(self) -> str:
        """Возвращает значение поля __email."""
        return self.__email

    @email.setter
    def email(self, value: str):
        """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        pattern = r'\b[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self) -> None:
        """Добавляет значение поля __email в файл."""
        with open(self.file_path, 'a', encoding='utf-8') as fileout:
            fileout.write(self.email + '\n')

