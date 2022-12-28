from typing import Optional

from dataclasses import dataclass
from enum import Enum
from string import ascii_lowercase as a_lc

import re


class SquareColor(int, Enum):
    """Цвет поля на доске."""
    LIGHT = 0
    DARK = 1

class PieceColor(Enum):
    """Цвет фигуры."""
    WHITE = 0
    BLACK = 1

class PieceKind(Enum):
    """Вид фигуры."""
    KING = 0
    QUEEN = 1
    ROOK = 2
    BISHOP = 3
    KNIGHT = 4
    PAWN = 5


@dataclass
class Piece:
    """Описывает сущность фигуры."""
    color: PieceColor
    kind: PieceKind
    square: Optional['Square']
    
    def __post_init__(self):
        self.removed: bool = False
    
    def __del__(self):
        """Удаляет фигуру с поля."""
        self.square.piece = None
        self.square = None
        self.removed = True
    
    def __repr__(self):
        return f'{self.color.name.title()} {self.kind.name.title()}'
    
    def __str__(self):
        return self.color.name[0] + self.kind.name[0]
    
    def move(self, end_square: 'Square') -> None:
        """Осуществляет проверку, ход фигуры и взятие фигуры противника."""
        if end_square.piece is not None:
            if end_square.piece.color is self.color:
                raise Exception
            else:
                del end_square.piece
        self.square.piece = None
        self.square = end_square
        end_square.piece = self


@dataclass
class Square:
    """Описывает сущность поля."""
    color: SquareColor
    file: str
    rank: str
    piece: Optional[Piece] = None
    
    def __repr__(self):
        return f'<{self.file + self.rank}: {self.piece!r}>'
    
    def __str__(self):
        return self.file + self.rank


class Chessboard(dict):
    """Описывает сущность игровой доски."""
    
    class File(dict):
        """Вертикаль игровой доски."""
        def __init__(self, file: str, start_color: SquareColor):
            super().__init__()
            for i in range(4):
                for j in range(2):
                    rank = i*2 + j + 1
                    self[rank] = Square(
                        list(SquareColor)[start_color-j],
                        file,
                        str(rank)
                    )
    
    def __init__(self):
        """Создаёт и нумерует игровою доску и заполняет её пустыми полями соответствующих цветов."""
        super().__init__()
        for i in range(8):
            for _ in range(4):
                for j in range(2):
                    self[a_lc[i]] = self.__class__.File(a_lc[i], list(SquareColor)[j-i%2])
        self.__post_init__()
    
    def __post_init__(self):
        """Расставляет фигуры на игровой доске в начальную позицию."""
        self['a1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['a1'])
        self['b1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['b1'])
        self['c1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['c1'])
        self['d1'].piece = Piece(PieceColor.WHITE, PieceKind.QUEEN, self['d1'])
        self['e1'].piece = Piece(PieceColor.WHITE, PieceKind.KING, self['e1'])
        self['f1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['f1'])
        self['g1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['g1'])
        self['h1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['h1'])
        for rank in a_lc[:8]:
            self[rank][2].piece = Piece(PieceColor.WHITE, PieceKind.PAWN, self[rank][2])
        self['a8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['a8'])
        self['b8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['b8'])
        self['c8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['c8'])
        self['d8'].piece = Piece(PieceColor.BLACK, PieceKind.QUEEN, self['d8'])
        self['e8'].piece = Piece(PieceColor.BLACK, PieceKind.KING, self['e8'])
        self['f8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['f8'])
        self['g8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['g8'])
        self['h8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['h8'])
        for rank in a_lc[:8]:
            self[rank][7].piece = Piece(PieceColor.BLACK, PieceKind.PAWN, self[rank][7])
    
    def __rank(self, number) -> list[Square]:
        """Возвращает горизонталь игровой доски."""
        return [file[number] for file in self.values()]
    
    def __getitem__(self, key: str | int):
        """Обеспечивает вариативный доступ к полям игровой доски."""
        if re.match(r'^[a-h][1-8]$', key := str(key).lower()):
            return super().__getitem__(key[0])[int(key[1])]
        elif re.match(r'^[a-h]$', key):
            return super().__getitem__(key)
        elif re.match(r'^[1-8]$', key):
            return self.__rank(int(key))
        else:
            raise KeyError
