class Complex_number:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.imaginary_part < 0:
            result = "{} - {}*i".format(self.real_part, (-1) * self.imaginary_part)
        else:
            result = "{} + {}*i".format(self.real_part, self.imaginary_part)
        return result

    def __add__(self, other):
        return Complex_number(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        result_real = self.real_part * other.real_part + (-1) * self.imaginary_part * other.imaginary_part
        result_imaginary = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return Complex_number(result_real, result_imaginary)


cn1 = Complex_number(2, 1)
cn2 = Complex_number(3, -3)
print(cn1)
print(cn2)
print(cn1 + cn2)
print(cn1 * cn2)
