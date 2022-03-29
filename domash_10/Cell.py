class Cell:
    def __init__(self, cellule):
        self.cellule = int(cellule)

    def __add__(self, other):
        return self.cellule + other.cellule

    def __sub__(self, other):
        sub = self.cellule - other.cellule
        if sub < 0:
            return 'Клетка исчезла'
        else:
            return sub


    def __truediv__(self, other):
        return self.cellule // other.cellule

    def __mul__(self, other):
        return self.cellule * other.cellule

    def make_order(self, row):
        result = ''
        for i in range(int(self.cellule / row)):
            result += '*' * row + '\n'
        result += '*' * (self.cellule % row) + '\n'
        return result


cell = Cell(31)
cell_2 = Cell(3)
cell_3 = Cell(12)
cell_4 = Cell(15)
cell_5 = Cell(24)
cell_6 = Cell(18)
print(cell + cell_2)
print(cell_6 - cell_3)
print(cell_5 / cell_2)
print(cell_2 * cell_3)
print(cell_2 - cell_4)
print(cell.make_order(7))