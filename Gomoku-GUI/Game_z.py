import random

class Frogsweeper:

    def __init__(self, diff):
        if diff == 'e':
            self.area = sum([[sum([[' '] for a in range(8)], [])] for b in range(8)], [])
            self.n = 8

    def __str__(self):
        re = ''
        for row in self.area:
            for point in row:
                re = re + point + ' '
            re += '\n'
        return re

    def find_neighbors(self, a, b):
        result = [(a - 1, b - 1), (a - 1, b), (a - 1, b + 1), (a, b - 1),
                  (a, b + 1), (a + 1, b - 1), (a + 1, b), (a + 1, b + 1)]
        for point in result:
            if point[0] < 0 or point[0] > self.n - 1 or point[1] < 0 or point[1] > self.n - 1:
                result.remove(point)
        return result


    def initial(self):
        li = []   # list of coordinate tuples containing mines
        for i in range(self.n + 2):
            coor = (random.randint(0, self.n - 1), random.randint(0, self.n - 1))
            while coor in li:
                coor = (random.randint(0, self.n - 1), random.randint(0, self.n - 1))
            li.append(coor)
            self.area[coor[0]][coor[1]] = '*'  # '*' represents a mine.
        a = 0
        b = 0
        while a < self.n:
            while b < self.n:
                count = 0
                if self.area[a][b] != '*':
                    for point in self.find_neighbors(a, b):
                        if self.area[point[0]][point[1]] == '*':
                            count += 1
                self.area[a][b] = str(count)
                b += 1
            a += 1


if __name__ == '__main__':
    game = Frogsweeper('e')
    game.initial()
    print(game)
