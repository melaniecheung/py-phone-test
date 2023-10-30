"""
test_phoneclass

Author: Melanie Cheung
Email: mcccheun@uwaterloo.ca
Student ID: 20989817
these are the unit tests for phoneclass
"""

import unittest
from phone.Phone import Phone

class TestPhone(unittest.TestCase):
    """
    TestPhone class representing unit tests for the 'Phone' class
    """

    # constructor tests
    def test_constructor_typical1(self):
        """
        Input: Pink iPhone 13 with price of 1099, 
        battery mAh of 2000 and power consumption of 100, pin of 2234
        Expected output: instance of a Phone with all variables above
        """
        # create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # check post conditions
        self.assertEqual(apple.get_name(), "iPhone 13")
        self.assertEqual(apple.get_colour(), "Pink")
        self.assertEqual(apple.get_price(), 1099)
        self.assertEqual(apple.get_battery_mah(), 2000)
        self.assertEqual(apple.get_power_consumption_mw(), 100)
        self.assertEqual(apple.get_pin(), "2234")

    def test_constructor_typical2(self):
        """
        Input: Samsung Galaxy S21, purple colour, 
        999 price, 1000 battery mAh, 200 power consumption, 1234 pin
        Expected output: instance of a Phone with all variables above
        """
        # create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # check post conditions
        self.assertEqual(samsung.get_name(), "Samsung Galaxy S21")
        self.assertEqual(samsung.get_colour(), "Purple")
        self.assertEqual(samsung.get_price(), 999)
        self.assertEqual(samsung.get_battery_mah(), 1000)
        self.assertEqual(samsung.get_power_consumption_mw(), 200)
        self.assertEqual(samsung.get_pin(), "1234")

    def test_constructor_unusual1(self):
        """
        Input: Pink iPhone 13 with price of 0, 
        battery mAh of 20000 and power consumption of 0, pin of 1234
        Expected output: instance of a Phone store with "iPhone 13", 
        "Pink", with the variables above
        """
        # create Phone instance
        unusual_apple = Phone("iPhone 13", "Pink", 0, 0, 0, "1234")

        # check post conditions
        self.assertEqual(unusual_apple.get_name(), "iPhone 13")
        self.assertEqual(unusual_apple.get_colour(), "Pink")
        self.assertEqual(unusual_apple.get_price(), 0)
        self.assertEqual(unusual_apple.get_battery_mah(), 0)
        self.assertEqual(unusual_apple.get_power_consumption_mw(), 0)
        self.assertEqual(unusual_apple.get_pin(), "1234")

    def test_constructor_unusual2(self):
        """
        Input: Pink apple iPhone 13 with Blue colour, 
        9999999 price, 1 battery capacity, 2 power consumption and 5555 pin
        Expected output: An instance of a Phone should be created with the specified attributes
        """
        # create Phone instance
        unusual_apple = Phone("iPhone 13", "Blue", 9999999, 1, 2, "5555")

        # check post conditions
        self.assertEqual(unusual_apple.get_name(), "iPhone 13")
        self.assertEqual(unusual_apple.get_colour(), "Blue")
        self.assertEqual(unusual_apple.get_price(), 9999999)
        self.assertEqual(unusual_apple.get_battery_mah(), 1)
        self.assertEqual(unusual_apple.get_power_consumption_mw(), 2)
        self.assertEqual(unusual_apple.get_pin(), "5555")

    def test_constructor_error1(self):
        """
        Input: empty name, empty colour, empty pin
        Expected output: An error should occur when trying to create the Phone
        """
        # Attempt to create Phone with empty values
        with self.assertRaises(ValueError):
            Phone(" ", " ", 1099, 2000, 1000, " ")

    def test_constructor_error2(self):
        """
        Input: Invalid product price (negative)
        Expected output: An error should occur when trying to create the Phone
        """
        # Attempt to create Phone with negative product price
        with self.assertRaises(ValueError):
            Phone("iPhone 13", "Pink", -1099, 2000, 100, "2234")

# accessor
    def test_calculate_battery_life_typical1(self):
        """
        Input: create Phone "Apple" and calculate the battery life with typical values
        Expected output: calculates battery life of the Apple phone
        """
        # create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
        battery_mah = 3000
        power_consumption_mw = 500
        expected_battery_life_hours = 6.0
        self.assertEqual(apple.calculate_battery_life(
            battery_mah, power_consumption_mw),
            expected_battery_life_hours)

    def test_calculate_battery_life_typical2(self):
        """
        Input: create Phone "Samsung" and calculate the battery life with typical values
        Expected output: calculates battery life of the Samsung phone
        """
        # create Phone instance
        samsung = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
        battery_mah = 6000
        power_consumption_mw = 500
        expected_battery_life_hours = 12.0
        self.assertEqual(samsung.calculate_battery_life(
                battery_mah, power_consumption_mw),
                expected_battery_life_hours)

    def test_calculate_battery_life_error1(self):
        """
        Input: create Phone "Apple" and attempts 
        to calculate the battery life with negative power consumption
        Expected output: raises value error
        """
        # create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
        battery_mah = 3000
        power_consumption_mw = -500

        # negative power consumption, raise value error
        with self.assertRaises(ValueError):
            apple.calculate_battery_life(battery_mah, power_consumption_mw)

    def test_calculate_battery_life_error2(self):
        """
        Input: create phone "Samsung" and calculates the battery life 
        and attempts to calculate the battery life with 0 power consumption
        Expected output: raises value error
        """
        # create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")
        battery_mah = 3000
        power_consumption_mw = 0

        # 0 power consumption, raise value error
        with self.assertRaises(ValueError):
            samsung.calculate_battery_life(battery_mah, power_consumption_mw)

    def test_calculate_battery_life_error3(self):
        """
        Input: create phone "Samsung" and calculates the battery life 
        and attempts to calculate the battery life with a string
        Expected output: raises type error
        """
        # create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")
        battery_mah = "3000"
        power_consumption_mw = 200

        # 0 power consumption, raise value error
        with self.assertRaises(TypeError):
            samsung.calculate_battery_life(battery_mah, power_consumption_mw)

    def test_calculate_battery_life_unusual2(self):
        """
        Input: create phone "Apple" and calculates the battery life with 
        extremely small battery capacity and typical power consumption
        Expected output: calculate battery life with the given values
        """
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
        battery_mah = 0.001
        power_consumption_mw = 500
        expected_battery_life_hours = 0.000002
        self.assertAlmostEqual(apple.calculate_battery_life(battery_mah,
                                                            power_consumption_mw),
                                                            expected_battery_life_hours,
                                                            places=6)

    def test_set_battery_mah_typical1(self):
        """
        Input: Create Phone "Apple" and set the battery capacity to 4000 mAh
        Expected output: The battery capacity of the phone should be updated to 4000 mAh
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 3000, 100, "2234")

        # Set battery capacity to 3000 mAh
        updated = apple.set_battery_mah(4000)

        # Check if the battery capacity is updated
        self.assertEqual(apple.get_battery_mah(), 4000)
        self.assertTrue(updated)

    def test_set_battery_mah_typical2(self):
        """
        Input: Create Phone "Samsung" and set the battery capacity to 1599 mAh
        Expected output: The battery capacity of the phone should be updated to 1599 mAh
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Set battery capacity to 3000 mAh
        updated = samsung.set_battery_mah(1599)

        # Check if the battery capacity is updated
        self.assertEqual(samsung.get_battery_mah(), 1599)
        self.assertTrue(updated)

    def test_set_battery_mah_unusual1(self):
        """
        Input: create phone "Apple" and set battery capacity to a very large value
        Expected output: sets the battery capacity to very large value
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 3000, 100, "2234")

        # set battery capacity to a very large value
        updated = apple.set_battery_mah(10**13)

        # check postconditions
        self.assertEqual(apple.get_battery_mah(), 10**13)
        self.assertTrue(updated)

    def test_set_battery_mah_unusual2(self):
        """
        Input: create phone "Apple" and set battery capacity to a small value
        Expected output: sets the battery capacity to small value
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 3000, 100, "2234")

        # set battery capacity to a very large value
        updated = apple.set_battery_mah(2)

        # check postconditions
        self.assertEqual(apple.get_battery_mah(), 2)
        self.assertTrue(updated)

    def test_set_battery_mah_error1(self):
        """
        Input: Create Phone "Samsung" and attempt to set the battery capacity to a negative value
        Expected output: Raise value error, and the battery capacity should not be updated
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Attempt to set battery capacity to a negative value
        with self.assertRaises(ValueError):
            samsung.set_battery_mah(-2000)

        # Check postconditions
        self.assertEqual(samsung.get_battery_mah(), 1000)

    def test_set_battery_mah_error2(self):
        """
        Input: Create Phone "Apple" and attempt to set the battery capacity to a non-integer value
        Expected output: Type Error, and the battery capacity should not be updated
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Attempt to set battery capacity to a non-integer value (e.g., a string)
        with self.assertRaises(TypeError):
            samsung.set_battery_mah("3000")

        # Check postconditions
        self.assertEqual(samsung.get_battery_mah(), 1000)

    def test_set_power_consumption_typical1(self):
        """
        Input: Create Phone "Apple" and  set the power consumption to 500mW
        Expected output: sets power consumption with the updated typical values
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # Set power consumption to 500 mW
        apple.set_power_consumption_mw(500)

        # Check if the power consumption is updated
        self.assertEqual(apple.get_power_consumption_mw(), 500)

    def test_set_power_consumption_typical2(self):
        """
        Input: Create Phone "Samsung" and  set the power consumption to 100mW
        Expected output: sets power consumption with the updated typical values
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Set power consumption to 500 mW
        samsung.set_power_consumption_mw(100)

        # Check if the power consumption is updated
        self.assertEqual(samsung.get_power_consumption_mw(), 100)

    def test_set_power_consumption_unusual1(self):
        """
        Input: create phone "Apple" and set power consumption to a very large value
        Expected output: sets the power consumption to very large value
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 3000, 100, "2234")

        # set power consumption to a very large value
        apple.set_power_consumption_mw(10**13)

        # check postconditions
        self.assertEqual(apple.get_power_consumption_mw(), 10**13)

    def test_set_power_consumption_unusual2(self):
        """
        Input: create phone "Apple" and set power consumption to a small value
        Expected output: sets the power consumption to small value
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 3000, 100, "2234")

        # set power consumption to a small value
        apple.set_power_consumption_mw(2)

        # check postconditions
        self.assertEqual(apple.get_power_consumption_mw(), 2)

    def test_set_power_consumption_error1(self):
        """
        Input: Create Phone "Apple" and attempt to set the power consumption to a non-integer value
        Expected output: An error should occur, and the power consumption should not be updated
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # Attempt to set power consumption to a non-integer value (string)
        with self.assertRaises(TypeError):
            apple.set_power_consumption_mw("500")

        # Check postconditions
        self.assertNotEqual(apple.get_power_consumption_mw(), "500")

    def test_set_power_consumption_error2(self):
        """
        Input: Create Phone "Apple" and attempt to set the power consumption to 0
        Expected output: An error should occur, and the power consumption should not be updated
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # attempt to set the power consumption to 0
        with self.assertRaises(ValueError):
            apple.set_power_consumption_mw(0)

        # Check postconditions
        self.assertNotEqual(apple.get_power_consumption_mw(), 0)

    def test_set_power_consumption_error3(self):
        """
        Input: Create Phone "Samsung" and attempt to set the power consumption to a negative value
        Expected output: An error should occur, and the power consumption should not be updated
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Attempt to set power consumption to a negative value
        with self.assertRaises(TypeError):
            samsung.set_power_consumption_mw("-200")

        # Check postconditions
        self.assertNotEqual(samsung.get_power_consumption_mw(), -200)

    def test_unlock_typical1(self):
        """
        Input: unlock the apple with a valid 4-digit pin
        Expected output: phone should be unlocked
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # unlock the phone with a valid 4-digit pin
        unlocked = apple.unlock('2234')

        # Check if the phone is successfully unlocked
        self.assertTrue(unlocked)

    def test_unlock_typical2(self):
        """
        Input: unlock the samsung with a valid 4-digit pin
        Expected output: phone should be unlocked
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # unlock the phone with a valid 4-digit pin
        unlocked = samsung.unlock('1234')

        # Check if the phone is successfully unlocked
        self.assertTrue(unlocked)

    def test_unlock_unusual1(self):
        """
        Input: unlock the phone with the wrong 4-digit pin
        Expected output: phone should not be unlocked, and should return false
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # unlock the phone with the wrong PIN
        unlocked = apple.unlock('1111')

        # Check if the phone is unlocked
        self.assertFalse(unlocked)

    def test_unlock_error1(self):
        """
        Input: unlock the phone with a non digit pin
        Expected output: value error, phone should not be unlocked
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        unlocked = None # initialize variable

        # unlock the phone with non digit pin
        with self.assertRaises(ValueError):
            unlocked = apple.unlock('ABCD')

        # check if the phone is unlocked
        self.assertFalse(unlocked)

    def test_unlock_error2(self):
        """
        Input: unlock the phone with empty PIN
        Expected output: phone should not be unlocked. error should occur
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        unlocked = None # initialize variable

        # unlock the phone with non digit pin
        with self.assertRaises(ValueError):
            unlocked = apple.unlock('')

        # Check postconditions
        self.assertFalse(unlocked)

    def test_unlock_error3(self):
        """
        Input: incorrect length of PIN
        Expected output: value error, phone should not be unlocked
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        unlocked = None # initialize variable

        # unlock the phone with incorrect length of pin
        with self.assertRaises(ValueError):
            unlocked = apple.unlock('123456')

        # Check postconditions
        self.assertFalse(unlocked)

    def test_set_price_typical1(self):
        """
        Input: change the price of iPhone to 1199
        Expected output: price of the iPhone should be updated to 1199
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # Change the price of the iPhone to $1199
        apple.set_price(1199)

        # Check if the price is updated
        self.assertEqual(apple.get_price(), 1199)

    def test_set_price_typical2(self):
        """
        Input: change the price of samsung to 500
        Expected output: price of the samsung should be updated to 500
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Change the price of the samsung to $500
        samsung.set_price(500)

        # Check if the price is updated
        self.assertEqual(samsung.get_price(), 500)

    def test_set_price_error2(self):
        """
        Input: attempt to change the price of iPhone to negative value
        Expected output: price should not be updated, raises value error
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # change the price of iPhone 13 to negative avlue
        with self.assertRaises(ValueError):
            apple.set_price(-799)

        # check postconditions
        self.assertNotEqual(apple.get_price(), 879)

    def test_set_price_unusual2(self):
        """
        Input: change the price of iPhone to 0
        Expected output: changes price of iPhone to 0
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # change the price of iPhone 13 to a string
        apple.set_price(0)

        # Check if the price is updated
        self.assertEqual(apple.get_price(), 0)

    def test_set_price_unusual3(self):
        """
        Input: change the price of Samsung to very large value
        Expected output: price updates to the very large value, raises value error
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # change the price of Samsung to very large value
        samsung.set_price(9999**10)

        # check postconditions
        self.assertEqual(samsung.get_price(), 9999**10)

    def test_set_price_error1(self):
        """
        Input: attempt to change the price of iPhone to a string
        Expected output: raises type error
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # change the price of iPhone 13 to a string
        with self.assertRaises(TypeError):
            apple.set_price("one thousand")

        # check postconditions
        self.assertNotEqual(apple.get_price, "one thousand")

    def test_set_colour_typical1(self):
        """
        Input: changes the colour of iPhone to blue
        Expected output: colour of the iPhone should be updated to blue
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # Change the color of iPhone 13
        apple.set_colour("Blue")

        # Check if the color is updated
        self.assertEqual(apple.get_colour(), "Blue")

    def test_set_colour_typical2(self):
        """
        Input: changes the colour of Samsung to gold
        Expected output: colour of the Samsung should be updated to gold
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Change the color of Samsung
        samsung.set_colour("Gold")

        # Check if the color is updated
        self.assertEqual(samsung.get_colour(), "Gold")

    def test_set_colour_unusual1(self):
        """
        Input: Attempt to change the color of Samsung to a very long color name
        Expected output: Color should be updated to the very long colour name
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # Attempt to change the color to a very long color name
        samsung.set_colour("Example of a Very Long Colour Name")

        # Check postconditions
        self.assertEqual(samsung.get_colour(), "Example of a Very Long Colour Name")

    def test_set_colour_unusual2(self):
        """
        Input: Attempt to change the color of Samsung to a string with digits only
        Expected output: color changed to the given value
        """
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")
        samsung.set_colour("123456" )
        self.assertEqual(samsung.get_colour(), "123456" )

    def test_set_colour_error1(self):
        """
        Input: Attempt to change the color of iPhone to an empty string
        Expected output: Color should not be updated, raises value error
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # Attempt to change the color to an empty string
        with self.assertRaises(ValueError):
            apple.set_colour("")

        # Check postconditions
        self.assertEqual(apple.get_colour(), "Pink")

    def test_set_colour_error2(self):
        """
        Input: Attempt to change the color of the phone to a numeric value
        Expected output: Color should not be updated, raises type error
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # Attempt to change the color to a numeric value
        with self.assertRaises(TypeError):
            apple.set_colour(123)

        # Check postconditions
        self.assertEqual(apple.get_colour(), "Pink")

    def test_charge_typical1(self):
        """
        Input: charge the phone with 500 mAh
        Expected output: battery should be 2500 mAh, assuming that the phone starts with 2000 mAh
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
        initial_battery_level = apple.get_battery_mah()
        charge_amount = 500
        remaining_battery_level = apple.charge_mah(charge_amount)
        expected_battery_level = initial_battery_level + charge_amount
        self.assertEqual(remaining_battery_level, expected_battery_level)

    def test_charge_typical2(self):
        """
        Input: charge the phone with 200 mAh
        Expected output: battery should be 2700 mAh, assuming that the phone starts with 2500 mAh
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")
        initial_battery_level = samsung.get_battery_mah()
        charge_amount = 200
        remaining_battery_level = samsung.charge_mah(charge_amount)
        expected_battery_level = initial_battery_level + charge_amount
        self.assertEqual(remaining_battery_level, expected_battery_level)

    def test_charge_unusual1(self):
        """
        Input: charge the phone with a very large amount
        Expected output: battery should be maxed out at the given battery capacity
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")
        charge_amount = 9999999
        remaining_battery_level = samsung.charge_mah(charge_amount)
        self.assertEqual(remaining_battery_level, samsung.get_battery_mah())

    def test_charge_unusual2(self):
        """
        Input: charge battery with a decimal amount
        Expected output: battery should be updated with the amount charged
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")
        initial_battery_level = samsung.get_battery_mah()
        charge_amount = 250.5
        remaining_battery_level = samsung.charge_mah(charge_amount)
        expected_battery_level = initial_battery_level + charge_amount
        self.assertEqual(remaining_battery_level, expected_battery_level)

    def test_charge_error1(self):
        """
        Input: charge the phone with negative amonut
        Expected output: raise value error
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
        initial_battery_level = apple.get_battery_mah()
        charge_amount = -500

        # raise value error
        with self.assertRaises(ValueError):
            apple.charge_mah(charge_amount)

        self.assertEqual(apple.get_battery_mah(),
                         initial_battery_level) # battery level remain unchanged

    def test_charge_error2(self):
        """
        Input: charge phone with non-integer amount
        Expected output: raise type error
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
        initial_battery_level = apple.get_battery_mah()
        charge_amount = "500"

        # raise type error
        with self.assertRaises(TypeError):
            apple.charge_mah(charge_amount)

        self.assertEqual(apple.get_battery_mah(),
                         initial_battery_level) # battery level remain unchanged

    def test_set_pin_typical1(self):
        """
        Input: iPhone, set pin with 1234
        Expected output: sets pin of iPhone to 1234
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # set the pin to 1234
        apple.set_pin("1234")

        # check postconditions
        self.assertEqual(apple.get_pin(), "1234")

    def test_set_pin_typical2(self):
        """
        Input: Samsung galaxy phone, set pin to 1989
        Expected output: sets Samsung galaxy phone pin to 1989
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # set the pin to 1989
        samsung.set_pin("1989")

        # check postconditions
        self.assertEqual(samsung.get_pin(), "1989")

    def test_pin_error1(self):
        """
        Input: iPhone, set pin to an empty pin
        Expected output: raise value error, pin should not be updated
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # raise value error
        with self.assertRaises(ValueError):
            apple.set_pin((""))

        # check postconditons
        self.assertNotEqual(apple.get_pin(), (""))

    def test_pin_error2(self):
        """
        Input: Samsung galaxy phone, set the pin to less than 4 digits
        Expected output: raise value error, pin should not be updated
        """
        # Create Phone instance
        samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")

        # raise value error
        with self.assertRaises(ValueError):
            samsung.set_pin("12")

        # check postconditions
        self.assertNotEqual(samsung.get_pin(), "12")

    def test_pin_error3(self):
        """
        Input: iPhone, set pin to more than 4 digits
        Expected output: raise value error, pin should not be updated
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # raise value error
        with self.assertRaises(ValueError):
            apple.set_pin("123456")

        # check postconditions
        self.assertNotEqual(apple.get_pin(), "123456")

    def test_pin_error4(self):
        """
        Input: iPhone, attempt to set pin to a non-digit pin
        Expected output: raise value error, pin should not be updated
        """
        # Create Phone instance
        apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")

        # raise Value Error
        with self.assertRaises(ValueError):
            apple.set_pin("A!#9")

        # check postconditions
        self.assertNotEqual(apple.get_pin(), "A!#9")  # PIN should not be updated
