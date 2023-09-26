# Парадигма ООП для запоминания состояния доски
# Также структурная и процедурная парадигмы

class Board:
    def __init__(self, size):
        self.size = size
        self.field = [['' for i in range(size)] for j in range(size)]

    def print_field(self):
        for row in range(self.size):
            for col in range(self.size):
                print('___' if self.field[row][col] == '' else f'_{self.field[row][col]}_', end='')
                print('|' if col < self.size -1 else '', end='')
            print()
        print()

    def do_step(self, row, col, fig):
        if 1 <= row <= self.size and 1 <= col <= self.size:
            if self.field[row - 1][col - 1] == '':
                self.field[row - 1][col - 1] = fig
                return True
            else:
                return False
        else:
            return False

    def win(self):
        fig = ''

        # Ряды
        for row in range(self.size):
            fig = self.field[row][0] if self.field[row].count(self.field[row][0]) == self.size else ''
            if fig != '':
                return True, fig

        # Колонки
        for col in range(self.size):
            row_set = set()
            for row in range(self.size):
                fig = self.field[row][col]
                row_set.add(fig)
            if len(row_set) == 1 and fig != '':
                return True, fig

        # Диагональ 1
        row_set = set()
        for index in range(self.size):
            fig = self.field[index][index]
            row_set.add(fig)
        if len(row_set) == 1 and fig != '':
            return True, fig

        # Диагональ 2
        row_set = set()
        for index in range(self.size):
            fig = self.field[index][self.size - index - 1]
            row_set.add(fig)
        if len(row_set) == 1 and fig != '':
            return True, fig

        # Нет выигрыша
        return False, ''


def tic_tac_game():
    board_size = 3
    board = Board(board_size)

    step_count = board_size ** 2
    tic_step = True
    i = 0
    win = False
    while i < step_count:
        board.print_field()

        fig = 'X' if tic_step else '0'
        input_step = input(f'Ход {i + 1}. Фигура {fig}. Укажите строку (1 - 3) и колонку (1 - 3) через пробел: ')

        try:
            step = list(map(int, input_step.split()))
            step_result = board.do_step(step[0], step[1], fig)
            if not step_result:
                print('Ход неправильный. Повторите ввод: ')
                continue
        except:
            print('Ход неправильный. Повторите ввод: ')
            continue

        win = board.win()[0]
        if win:
            board.print_field()
            print(f'Выиграл {fig}!!!')
            break

        tic_step = not tic_step
        i += 1

    if not win:
        print('Ничья!')


tic_tac_game()

