import unittest

def time_difference(start_time: int, end_time: int) -> int:
    """
    Calculate the time difference between start_time and end_time in a 24-hour cyclic format.
    This handles cases where end_time may be on the next day (e.g., from 23:00 to 01:00).

    Parameters:
    - start_time (int): Starting hour in 24-hour format (0-23).
    - end_time (int): Ending hour in 24-hour format (0-23).

    Returns:
    - int: The time difference in hours.
    """
    return (end_time - start_time + 24) % 24

# test
class TestTimeDifference(unittest.TestCase):
    def test_same_time(self):
        self.assertEqual(time_difference(5, 5), 0)

    def test_within_day(self):
        self.assertEqual(time_difference(10, 15), 5)

    def test_cross_midnight(self):
        self.assertEqual(time_difference(23, 1), 2)
        self.assertEqual(time_difference(22, 3), 5)

    def test_full_day(self):
        self.assertEqual(time_difference(0, 0), 0)

    def test_one_hour_to_midnight(self):
        self.assertEqual(time_difference(23, 0), 1)

if __name__ == '__main__':
    unittest.main()
