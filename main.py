__author__ = 'other019'


class Square:
    def __init__(self, x, y, val):

        self.possibilities = [i for i in xrange(1, 10)]
        self.x = x
        self.y = y
        self.value = val

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def eliminate_possibilities(self, bd):
        for i in xrange(9):
            self.possibilities.remove(bd.tab[i][self.y].get_value())
        for i in xrange(9):
            self.possibilities.remove(bd.tab[self.x][i].get_value())
        if self.x < 3:
            x_possibilities = [0, 1, 2]
        elif 3 <= self.x < 6:
            x_possibilities = [3, 4, 5]
        else:
            x_possibilities = [6, 7, 8]

        if self.y < 3:
            y_possibilities = [0, 1, 2]
        elif 3 <= self.y < 6:
            y_possibilities = [3, 4, 5]
        else:
            y_possibilities = [6, 7, 8]

        for i in x_possibilities:
            for j in y_possibilities:
                self.possibilities.remove(bd.tab[i][j].get_value())

    def try_to_set_value(self):
        if self.value == 0:
            if len(self.possibilities) == 1:
                self.value = self.possibilities[0]


class Board:
    def __init__(self):
        self.tab = [[None for i in xrange(9)] for j in xrange(9)]
        self.read()

    def __str__(self):
        res = '[\n'
        for i in xrange(9):
            res += '['
            for j in xrange(9):
                res += self.tab[i][j].get_value()
                res += ', '
            res += ']\n'
        res += ']'
        return res

    def read(self):
        for i in xrange(9):
            row = raw_input()
            row = row.split()
            for j in xrange(9):
                self.tab[i][j] = Square(i, j, row[j])

    def eliminate_possibilities(self):
        for i in xrange(9):
            for j in xrange(9):
                self.tab[i][j].eliminate_possibilities()

    def try_to_set_value(self):
        for i in xrange(9):
            for j in xrange(9):
                self.tab[i][j].try_to_set_value()


def main():
    board = Board()
    print board


if __name__ == '__main__':
    main()