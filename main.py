__author__ = 'other019'


class Square:
    def __init__(self, x, y, val):

        self.possibilities = [i for i in xrange(1, 10)]
        self.x = x
        self.y = y
        self.value = int(val)

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def get_len_pos(self):
        return len(self.possibilities)

    def eliminate_possibilities(self, bd):
        for i in xrange(9):
            if bd.tab[i][self.y].get_value() in self.possibilities:
                self.possibilities.remove(bd.tab[i][self.y].get_value())
        for i in xrange(9):
            if bd.tab[self.x][i].get_value() in self.possibilities:
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
                if bd.tab[i][j].get_value() in self.possibilities:
                    self.possibilities.remove(bd.tab[i][j].get_value())

    def try_to_set_value(self):
        if self.value == 0:
            if len(self.possibilities) == 1:
                self.value = self.possibilities[0]
                self.possibilities = []


class Board:
    def __init__(self):
        self.tab = [[None for i in xrange(9)] for j in xrange(9)]

    def __str__(self):
        res = '[\n'
        for i in xrange(9):
            res += '['
            for j in xrange(9):
                res += str(self.tab[i][j].get_value())
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
                self.tab[i][j].eliminate_possibilities(self)

    def try_to_set_value(self):
        for i in xrange(9):
            for j in xrange(9):
                self.tab[i][j].try_to_set_value()

    def assign_min_len_possibilities(self):
        min_pos = 9
        for i in xrange(9):
            for j in xrange(9):
                if self.tab[i][j].get_len_pos() < min_pos and self.tab[i][j].get_len_pos() != 0 and self.tab[i][
                    j].get_value() == 0:
                    min_pos = self.tab[i][j].get_len_pos()
        return min_pos

    def assign_min_len_possibilities_pos(self):
        min_pos = 9
        x = 0
        y = 0
        for i in xrange(9):
            for j in xrange(9):
                if self.tab[i][j].get_len_pos() < min_pos and self.tab[i][j].get_len_pos() != 0 and self.tab[i][
                    j].get_value() == 0:
                    min_pos = self.tab[i][j].get_len_pos()
                    x = i
                    y = j
        return x, y

    def how_many_without_values(self):
        without_values = 0
        for i in xrange(9):
            for j in xrange(9):
                if self.tab[i][j].get_value() == 0:
                    without_values += 1
        return without_values

    def is_everything_ok(self):
        for i in xrange(9):
            row = []
            for j in xrange(9):
                if self.tab[i][j].get_value() in row and self.tab[j][i].get_value() != 0:
                    return False
                else:
                    row.append(self.tab[i][j].get_value())
        for i in xrange(9):
            col = []
            for j in xrange(9):
                if self.tab[j][i].get_value() in col and self.tab[j][i].get_value() != 0:
                    return False
                else:
                    col.append(self.tab[j][i].get_value())
        sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for ii in sets:
            for jj in sets:
                box = []
                for i in ii:
                    for j in jj:
                        if self.tab[j][i].get_value() in box and self.tab[j][i].get_value() != 0:
                            return False
                        else:
                            box.append(self.tab[j][i].get_value())
        return True


def solve(bd):
    while bd.how_many_without_values() != 0:
        if not bd.is_everything_ok():
            return 1
        bd.eliminate_possibilities()
        bd.try_to_set_value()
        if bd.how_many_without_values() > 1:
            bd.eliminate_possibilities()
            bd.try_to_set_value()
            if bd.how_many_without_values() > 1:
                x, y = bd.assign_min_len_possibilities_pos()
                for i in bd.tab[x][y].possibilities:
                    bd2 = bd
                    bd2.tab[x][y].set_value(i)
                    solve(bd2)
    print bd
    return 0


def main():
    board = Board()
    board.read()


if __name__ == '__main__':
    main()