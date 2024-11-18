import math

def vector_magnitude(vector):
    return math.sqrt(sum(comp ** 2 for comp in vector))

# Example usage:
v = [3, 4, 5]
magnitude = vector_magnitude(v)
print("Magnitude of the vector is:", magnitude)