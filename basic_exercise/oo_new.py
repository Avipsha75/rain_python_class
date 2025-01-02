class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, *others):
        sum_vector = Vector(self.x, self.y)
        for other in others:
            sum_vector = Vector(sum_vector.x + other.x, sum_vector.y + other.y)

        return sum_vector
    
    def __sub__(self, *others):
        sub_vector = Vector(self.x, self.y)
        for other in others:
            sub_vector = Vector(sub_vector.x - other.x, sub_vector.y - other.y)

        return sub_vector
    
    def __mul__(self, *others):
        mul_vector = Vector(self.x, self.y)
        for other in others:
            mul_vector = Vector(mul_vector.x * other, mul_vector.y * other)

        return mul_vector
    
    def __str__(self):
        return f"Vector: ({self.x}, {self.y})"
    
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(3, 4)
v4 = Vector(3, 4)
result_vector = v1 + v2 + v3 + v4
print(result_vector)