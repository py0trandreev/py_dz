class Cell:
    def __init__(self, cell_item_count):
        self.cell_item_count = cell_item_count

    def __add__(self, other):
        return Cell(self.cell_item_count + other.cell_item_count)

    def __sub__(self, other):
        if self.cell_item_count - other.cell_item_count <= 0:
            print("Разность должна быть больше 0")
        else:
            return Cell(self.cell_item_count - other.cell_item_count)

    def __mul__(self, other):
        return Cell(self.cell_item_count * other.cell_item_count)

    def __floordiv__(self, other):
        return Cell(self.cell_item_count // other.cell_item_count)

    def __truediv__(self, other):
        return Cell(self.cell_item_count // other.cell_item_count)

    def make_order(self, cell_items_in_a_row):
        result = ''
        row_number = self.cell_item_count // cell_items_in_a_row
        for i in range(row_number):
            result += "*" * cell_items_in_a_row + "\n"
        row_remainder = self.cell_item_count % cell_items_in_a_row
        result += "*" * row_remainder

        return result


cl1 = Cell(5)
cl2 = Cell(8)
cl3 = cl1 + cl2
print(cl3.cell_item_count)
print(cl3.make_order(4))
