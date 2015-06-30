__author__ = 'other019'


class Square:
    possibilities = [True for i in xrange(10)]
    value = 0

    def __init__(self):
        pass

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value


class Board:
    tab = [[Square() for i in xrange(9)] for j in xrange(9)]

    def __init__(self):
        self.read()

    def read(self):
        for i in xrange(9):
            row = raw_input()
            row = row.split()
            for j in xrange(9):
                self.tab[i][j].set_value(row[j])

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


def main():
    board = Board()
    print board


if __name__ == '__main__':
    main()