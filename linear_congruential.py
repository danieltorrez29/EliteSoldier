import time


class LinearCongruential:
    def __init__(self):
        # Multiplier for the congruential formula
        self.multiplier = 1664525
        # Increment for the congruential formula
        self.increment = 1013904223
        # Modulus for the congruential formula
        self.modulus = 2**32
        # Generate initial seed based on current time
        self.seed = int(time.time()) % self.modulus

    def generate_number(self, minimum, maximum):
        # Update seed using congruential formula
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulus
        # Calculate the range of values based on the given minimum and maximum
        pseudo_random_number = minimum + (self.seed % (maximum - minimum + 1))
        return pseudo_random_number
