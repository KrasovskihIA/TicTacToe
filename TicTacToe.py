#Ячейка поля
class Cell:
    def __init__(self):
        self.value = 0 # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик

    def __bool__(self):
        return self.value == 0

class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = None
        self.computer_win= False
        self.human_win = False
        self.is_draw = False

    def init (self): # Инициализация игрового поля и его очистка
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def __bool__(self): # возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае
        return self.computer_win == False and self.human_win == False

    def show(self): # отображение текущего состояния игрового поля
        for x in self.pole:
            ls = []
            for i in x:
                ls.append(i.value)
            print (ls)

    def __check(self, item): # проверка верности индексов
        if type(item) != tuple or len(item) !=2:
            raise IndexError('некорректно указанные индексы')
        if any(not (0 <= x < 3) for x in item if type(x) != slice):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item): # получение значения из клетки с индексами 
        self.__check(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value): # запись нового значения в клетку с индексами
        self.__check(key)
        r, c = key
        if self.pole[r][c].value != self.FREE_CELL:
            raise ValueError('клетка уже занята')
        self.pole[r][c].value = value

    def human_go(self, key):
        value = self.HUMAN_X

    @property
    def is_human_win(self): # возвращает True, если победил человек, иначе - False
        if self.human_win == True:
            return True
        else:
            return False

    @property
    def is_computer_win(self): # возвращает True, если победил компьютер, иначе - False
        if self.computer_win == True:
            return True
        else:
            return False

    @property
    def is_draw(self): # возвращает True, если ничья, иначе - False
        if self.is_draw == True:
            return True
        else:
            return False