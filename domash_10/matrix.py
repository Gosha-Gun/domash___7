class Matrix:
    def __init__(self, matr_list):
        self.matr_list = matr_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i_2) for i_2 in i]) for i in self.matr_list]))

    def __add__(self, other):
        for i in range(len(self.matr_list)):
            for i_2 in range(len(other.matr_list[i])):
                self.matr_list[i][i_2] = self.matr_list[i][i_2] + other.matr_list[i][i_2]
        return Matrix.__str__(self)

m1 = Matrix([[11,2,3],[4,5,6],[117,8,9]])
m2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
m4 = m1 + m2
print(m4)

