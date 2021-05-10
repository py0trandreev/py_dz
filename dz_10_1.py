class Matrix:
    def __init__(self, matrix_ls):
        self.matrix = matrix_ls

    def __str__(self):
        result_str = ""
        for el_ls in self.matrix:
            result_str += str("│ ")
            for el in el_ls:
                result_str += (str(el) + " ")
            result_str += str("│\n")
        return result_str

    def __add__(self, other):
        result_ls = []
        for self_ls, other_ls in zip(self.matrix, other.matrix):
            result_ls.append(list(map(lambda x, y: x + y, self_ls, other_ls)))

        return Matrix(result_ls)





mx = [
    [1,3,4],
    [3,7,8],
    [6,4,7],
]

mx2 = [
    [7,9,3],
    [7,4,5],
    [9,4,1],
]
mx1 = Matrix(mx)
print(mx1)
mx2 = Matrix(mx2)
mx3 = mx1 + mx2
print(mx3)




