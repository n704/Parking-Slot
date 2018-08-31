import unittest
from lib.parking_lot import ParkingLot

class TestingParkingSlot(unittest.TestCase):
    """
    Testing Parking Lot
    """

    def test_creation(self):
        """
        Can create parking lot with n number.
        Raise Exception
            * size is not a number.
        """
        parking_lot = ParkingLot(5)
        self.assertEqual(parking_lot.size, 5)
        for slot in parking_lot.slots:
            self.assertIsNone(slot)
        try:
            ParkingLot("ABC")
        except Exception as e:
            self.assertEqual("Size need to be Integer: ABC", e.message)

    def test_park_a_car(self):
        """
        Test parking.
        """
        parking_lot = ParkingLot(0)
        try:
            parking_lot.park_a_car("123", "123")
        except Exception as e:
            self.assertEqual(e.message, "Sorry, parking lot is full")
        parking_lot = ParkingLot(1)
        try:
            parking_lot.park_a_car("", "")
        except Exception as e:
            self.assertEqual(e.message, "vehicale information cannot be empty.\n")

    def test_leave_a_car(self):
        """
        Test car leaving.
        """
        parking_lot = ParkingLot(3)
        message = parking_lot.car_is_leaving(2)
        self.assertEqual("Slot number 2 is free.\n", message)
        try:
            parking_lot.car_is_leaving(-1)
        except Exception as e:
            self.assertEqual("Slot number should be greater than zero.\n", e.message)
        try:
            parking_lot.car_is_leaving(4)
        except Exception as e:
            self.assertEqual("Slot number does not exist in parking lot.\n", e.message)
        parking_lot.park_a_car("123", "123")
        parking_lot.park_a_car("123", "123")
        parking_lot.park_a_car("123", "123")
        message = parking_lot.car_is_leaving(3)
        self.assertEqual("Slot number 3 is free.\n", message)

    def test_registration_numbers_for_cars_with_colour(self):
        """
        Test car with reg number color
        """
        parking_lot = ParkingLot(5)
        parking_lot.park_a_car("KA-01-HH-1234", "White")
        parking_lot.park_a_car("KA-01-BB-0001", "Black")
        parking_lot.park_a_car("KA-01-HH-9999", "White")
        parking_lot.park_a_car("KA-01-HH-2701", "Blue")
        parking_lot.park_a_car("KA-01-HH-3141", "Black")
        registration_numbers = parking_lot.registration_numbers_for_cars_with_colour("WHITE")
        self.assertEqual(registration_numbers, "KA-01-HH-1234, KA-01-HH-9999")
        registration_numbers = parking_lot.registration_numbers_for_cars_with_colour("RED")
        self.assertEqual(registration_numbers, "")

    def test_slot_numbers_for_cars_with_colour(self):
        """
        Return slot number of the registerd vehicale
        """
        parking_lot = ParkingLot(5)
        parking_lot.park_a_car("KA-01-HH-1234", "White")
        parking_lot.park_a_car("KA-01-BB-0001", "Black")
        parking_lot.park_a_car("KA-01-HH-9999", "White")
        parking_lot.park_a_car("KA-01-HH-2701", "Blue")
        parking_lot.park_a_car("KA-01-HH-3141", "Black")
        slots = parking_lot.slot_numbers_for_cars_with_colour("BLACK")
        self.assertEqual("2, 5", slots)
        slots = parking_lot.slot_numbers_for_cars_with_colour("YELLOW")
        self.assertEqual("", slots)

    def test_slot_number_for_registration_number(self):
        """
        Test slot_number_for_registration_number.
        """
        parking_lot = ParkingLot(5)
        parking_lot.park_a_car("KA-01-HH-1234", "White")
        parking_lot.park_a_car("KA-01-BB-0001", "Black")
        parking_lot.park_a_car("KA-01-HH-9999", "White")
        parking_lot.park_a_car("KA-01-HH-2701", "Blue")
        parking_lot.park_a_car("KA-01-HH-3141", "Black")
        slot = parking_lot.slot_number_for_registration_number("KA-01-HH-1234")
        self.assertEqual(slot, "1")
        slot = parking_lot.slot_number_for_registration_number("KA-01-Hd-1234")
        self.assertEqual(slot, "")

    def test_status(self):
        """
        Test test_status
        """
        parking_lot = ParkingLot(6)
        parking_lot.park_a_car("KA-01-HH-1234", "White")
        parking_lot.park_a_car("KA-01-HH-9999", "White")
        parking_lot.park_a_car("KA-01-BB-0001", "Black")
        parking_lot.park_a_car("KA-01-HH-7777", "Red")
        parking_lot.park_a_car("KA-01-HH-2701", "Blue")
        parking_lot.park_a_car("KA-01-HH-3141", "Black")
        parking_lot.car_is_leaving(4)
        import sys
        from StringIO import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            parking_lot.status_of_parking_lot()
            output = out.getvalue().strip()
            expected = """Slot No.    Registration No    Colour
1           KA-01-HH-1234      White
2           KA-01-HH-9999      White
3           KA-01-BB-0001      Black
5           KA-01-HH-2701      Blue
6           KA-01-HH-3141      Black"""
            self.assertEqual(len(expected), len(output))
            self.assertEqual(expected, output)

        finally:
            sys.stdout = saved_stdout




if __name__ == '__main__':
    unittest.main()
