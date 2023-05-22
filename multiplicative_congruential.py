import time


class MultiplicativeCongruential:
    def __init__(self):
        # Initialize the seed based on the current time
        self.seed = int(time.time())

    def generate_number(self):
        # Define the constants for the generator
        multiplier = 1664525
        increment = 1013904223
        modulus = 2**32

        # Calculate the next seed using the congruential formula
        self.seed = (multiplier * self.seed + increment) % modulus

        # Convert the seed to a decimal between 0 and 1
        decimal = self.seed / modulus

        return decimal
