import random
import math

# = affectation
foo = 123

# + addition
foo = 123 + 42
foo = foo + 42
# += opérateur d'incrémentation
foo += 42

# - soustraction
foo = 123 - 42
foo = foo - 42

# -= opérateur de décrementation
foo -= 42

# / division
foo = 123 / 42
foo /= 42
print(foo)
print(type(foo))

# // division entière
foo = 123 // 42
foo = foo // 42
foo //= 42
print(foo)
print(type(foo))

# % modulo
foo = 4 % 3
foo = random.randint(1, 100)
print(foo)
print(foo % 2)
foo %= 2


# * multiplication


# ** puissance
foo = 2 ** 2
foo = 2 ** 3
foo = 2 ** 4
foo = 2 ** 5
foo = 2 ** 6
print(foo)
# ^ puissance mais pas en python

# math.sqrt() racine carré
foo = math.sqrt(4)
# ** 0.5 racine carré
foo = 4 ** 0.5
# 0.5 == 1/2
foo = 4 ** (1/2)
# racine cubique
foo = 8 ** (1/3)
print(foo)