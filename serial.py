"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Initialize a serial number generator"""
        self.start = self.next = start

    def __repr__(self):
        """Show serial generator representation"""
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        """Generate the next serial number incremented by 1"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset the serial number to the number it started with"""
        self.next = self.start
