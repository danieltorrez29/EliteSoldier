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

    def generate_number(self):
        # Update seed using congruential formula
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulus
        # Scale the generated number to the range of 0 to 1
        decimal = self.seed / self.modulus
        # Return the pseudo-random number as a decimal between 0 and 1
        return decimal
