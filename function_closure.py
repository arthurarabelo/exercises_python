"""
Create functions that double, triple, and quadruple
the number received as a parameter.
"""

def create_multiplier(multiplier):
    def multiplicate(number):
        return number * multiplier
    return multiplicate

duplicate = create_multiplier(2)
triplicate = create_multiplier(3)
quadruplicate = create_multiplier(4)

print(duplicate(2), triplicate(2), quadruplicate(2))
