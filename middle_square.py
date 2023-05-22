import time


class MiddleSquare:
    def __init__(self):
        # Generate the initial seed based on the current time
        self.seed = int(time.time()) % 10000
        # Convert the seed to a string representation and pad it with leading zeros if necessary
        self.seed_str = str(self.seed).zfill(4)
        # Set the cycle size to represent the full range of possible seed values
        self.cycle_size = 10000

    def generate_number(self):
        # Generate the square of the seed and convert it to a string
        square = str(int(self.seed_str) ** 2)

        # Fill the square with leading zeros to ensure it has 8 digits
        square = square.zfill(8)

        # Extract the middle 4 digits from the square
        middle = square[2:6]
        self.seed_str = middle

        # Calculate the decimal value by dividing the middle digits by 10 raised to the power of the length of the middle digits
        decimal = int(middle) / (10 ** len(middle))

        # Update the seed for the next iteration
        self.seed = (self.seed + 1) % self.cycle_size
        self.seed_str = str(self.seed).zfill(4)

        return decimal
