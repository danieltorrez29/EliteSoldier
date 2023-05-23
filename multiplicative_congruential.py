import time


class MultiplicativeCongruential:
    def __init__(self):
        # Initialize the seed based on the current time
        self.seed = int(time.time())

    def generate_number(self, min_value, max_value):
        # Define the constants for the generator
        multiplier = 1664525
        increment = 1013904223
        modulus = 2**32

        # Calculate the next seed using the congruential formula
        self.seed = (multiplier * self.seed + increment) % modulus

        # Scale the seed to the desired range
        scaled_value = self.seed % (max_value - min_value + 1)
        integer = scaled_value + min_value

        return integer
