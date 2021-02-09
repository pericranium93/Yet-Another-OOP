import random
import re


class Card:
    _num_in_card = 15
    _row_in_card = 3

    def __init__(self, name):
        self.name = name
        self.rows = []
        self.num_in_rows = []

    def __str__(self):
        if self.name == 'игрок':
            return f'{"Ваша карточка".center(36, "-")}\n{"".join(self.rows[0])}\n{"".join(self.rows[1])}\n' \
                   f'{"".join(self.rows[2])}\n{"-" * 36} '
        if self.name == 'компьютер':
            return f'{"Карточка компьютера".center(36, "-")}\n{"".join(self.rows[0])}\n{"".join(self.rows[1])}\n' \
                   f'{"".join(self.rows[2])}\n{"-" * 36}'

    def row_creator(self):
        self.get_num(self._num_in_card)
        for i in range(self._row_in_card):
            a = '  ,' * 8
            space = re.split(',', a)
            nums = [' ' + str(i) + ' ' for i in self.num_in_rows[i * 5: i * 5 + 5]]  #
            row = space + nums
            random.shuffle(row)
            self.rows.append(row)

    def get_num(self, num_required):
        self.num_in_rows += random.sample(range(0, 91), num_required)

    def cross_out_num(self, num):
        self.num_in_rows.remove(num)
        for lst in self.rows:
            for index, elem in enumerate(lst):
                if elem == str(f' {num} '):
                    lst[index] = ' - '


class Game:
    nums_required = 90
    numbers = []

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def generator(self, num_required):  # намного удобнее вынести его в отдельную функцию.
        numbers = [i for i in range(num_required + 1)]
        return numbers

    def start_game(self):
        self.numbers = self.generator(self.nums_required)
        self.player1.row_creator()
        self.player2.row_creator()
        while True:
            random.shuffle(self.numbers)  # иммитируем лототрон, перемешивая последовательность каждый ход
            keg = self.numbers.pop()
            print(f'Новый бочонок: {keg} (осталось {len(self.numbers)})')
            print(self.player1)
            print(self.player2)
            answer = input('Зачеркнуть цифру? (y/n)').lower()

            if answer == 'y' and keg not in self.player1.num_in_rows:
                print(f'Вы проиграли! В вашей карточки нет числа {keg}')
                break
            elif answer != 'y' and keg in self.player1.num_in_rows:
                print(f'Вы проиграли! В вашей карточки есть число {keg}')
                break

            if keg in self.player1.num_in_rows:
                self.player1.cross_out_num(keg)
                if not self.player1.num_in_rows:
                    print(self.player1)
                    print(self.player2)
                    print('Вы победили!!!')
                    break
            if keg in self.player2.num_in_rows:
                self.player2.cross_out_num(keg)
                if not self.player2.num_in_rows:
                    print(self.player1)
                    print(self.player2)
                    print('Компьютер победил')
                    break


a = Card('игрок')
b = Card('компьютер')
c = Game(a, b)
c.start_game()

