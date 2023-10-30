"""
Phone.py

Author: Melanie Cheung
Email: mcccheun@uwaterloo
Student ID: 20989817
"""

import sys

class Phone:
    """
    Phone
    author: Melanie Cheung

    class representing a phone, with the attributes name, 
    colour, price, battery, capacity in mAh, power consumption in mW, and a 4-digit PIN code

    This class is able to calculate the phone’s battery life in hours, 
    given the battery capacity and power consumption.
    The class can also charge the phone to a given amount
    The mutator methods can also modify class’s attributes.
    """

    def __init__(self, name, colour, price, battery_mah, power_consumption_mw = 200, pin = "1234"):
        """
        Constructor 

        class representing a phone, the name, colour, price, battery, power consumption, and PIN

        name: string representing the name of the phone
        colour: string representing the colour of the phone
        price: float representing the price of the phone
        battery_mah: integer representing the battery capacity of the phone in mAh
        power_consumption_mw: integer representing the power consumption of the phone in mW
        pin: string representing the pin of the phone to unlock it

        """
        self._name = name
        self._colour = colour
        self._price = price
        self._battery_mah = battery_mah
        self._power_consumption_mw = power_consumption_mw
        self._pin = pin

        if not name.strip() or not colour.strip() or not pin.strip():
            raise ValueError("Name, colour, and pin must not be empty")

        if price < 0:
            raise ValueError("Price must be a non-negative value")

# Accessor methods
    def get_name(self):
        """
        get_name()

        Accessor method for the name
        """
        return self._name

    def get_price(self):
        """
        get_price()

        acessor method to get price
        """
        return self._price

    def get_battery_mah(self):
        """
        get_battery_mah()

        accessor method to get battery in mAh
        """
        return self._battery_mah

    def get_power_consumption_mw(self):
        """
        get_power_consumption()

        accessor method to get power consumption in mW
        """
        return self._power_consumption_mw

    def get_colour(self):
        """
        get_colour()
        
        accessor method to get colour
        """
        return self._colour

    def get_pin(self):
        """
        get_pin()

        accessor method to get pin
        """
        return self._pin

    def calculate_battery_life(self, battery_capacity_mah, power_consumption_mw):
        """
        calculate_battery_life()

        calculate hours of battery life based on battery capacity (mAh) and power consumption (mW)
        battery_capacity_mah: The battery capacity in milliampere-hours (mAh)
        power_consumption_mw: The power consumption in milliwatts (mW)

        Returns the estimated battery life in hours as a float
        """
        # calculate battery life in hours
        if power_consumption_mw <= 0:
            raise ValueError("Power consumption must be greater than 0")

        battery_life = battery_capacity_mah / power_consumption_mw
        return battery_life

# Mutator methods
    def set_name(self, name):
        """
        set_name()
        changes the name of the Phone

        name the new name as a string

        returns true if the name is changed, false otherwise
        """
        if name:
            self._name = name
            return True
        return False

    def set_price(self, price):
        """
        set_price()
        changes the price of a product

        price the new price as a float

        returns true if the price is updated, false otherwise
        """
        if price < 0:
            raise ValueError("Price must be a non-negative value")
        self._price = price

    def set_battery_mah(self, battery_mah):
        """
        set_battery_mah()
        changes the battery capacity of the phone

        battery_mah the new battery capacity as an integer

        returns true if the battery is changed, false otherwise
        """
        if battery_mah < 0:
            raise ValueError("Price must be a non-negative value")
        if battery_mah >= 0:
            self._battery_mah = battery_mah
            return True
        return False

    def set_power_consumption_mw(self, power_consumption_mw):
        """
        set_power_consumption_mw()
        changes the power consumption of the phone

        power_consumption_mw the new power consumption as an integer

        returns true if the power consumption is changed, false otherwise
        """
        if not isinstance(power_consumption_mw, int):
            raise TypeError("Power consumption must be an integer")
        if power_consumption_mw <= 0:
            raise ValueError("Power consumption must be greater than 0")
        self._power_consumption_mw = power_consumption_mw
        return True

    def set_pin(self, pin):
        """
        set_pin()
        
        changes the pin of the phone

        pin the new pin as a string

        returns true if the pin is changed, false otherwise
        """
        # raise value error if pin is empty
        if not pin:
            raise ValueError("PIN cannot be empty")

        # raise value error if pin is not an integer
        if len(pin) != 4 or not pin.isalnum():
            raise ValueError("PIN must be a 4-digit integer")

        self._pin = pin
        return True

    def unlock(self, pin):
        """
        unlock()

        unlock the phone with a pin

        pin: pin code as a string

        returns true if the phone is unlocked, false otherwise
        """
        # length of the pin must be 4, and must be a digit
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be a 4-digit number")

        if pin == self._pin:
            return True

        return False

    def charge_mah(self, charge_mah):
        """
        charge_mah()

        charge the phone's battery to a given amount

        charge: the amount to charge the battery in mAh

        returns the remaining battery capacity after charging
        """
        # raise type error if charge amount is not an integer or float
        if not (isinstance(charge_mah, int) or isinstance(charge_mah, float)):
            raise TypeError("Charge amount must be an integer or float")

        # raise value error if charge amount is negative
        if charge_mah < 0:
            raise ValueError("Charge amount must be non-negative")

        # calculation
        self._battery_mah += charge_mah
        return self._battery_mah

    def set_colour(self, colour):
        """
        set_colour()

        set the phone's colour

        colour the new colour as a string

        returns true if the colour is changed, false otherwise
        """
        # raise type error if colour is not a string
        if not isinstance(colour, str):
            raise TypeError("Colour must be a string")

        # raise value error if colour is empty
        if not colour.strip():
            raise ValueError("Colour must not be empty")

        self._colour = colour

    # space analysis empirical memory
    def __sizeof__(self):
        return(sys.getsizeof(self._name)
            + sys.getsizeof(self._price)
            + sys.getsizeof(self._colour)
            + sys.getsizeof(self._battery_mah)
            + sys.getsizeof(self._power_consumption_mw)
            + sys.getsizeof(self._pin)
        )

if __name__ == '__main__':
    phone1 = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
    print("Size of phone1: " + str(sys.getsizeof(phone1)) + " bytes")

    phone2 = Phone("iPhone 13 Pro Max!!!!!!!!!!!!!!", "Crimson Red", 1099, 2000, 100, "2234")
    print("Size of phone2: " + str(sys.getsizeof(phone2)) + " bytes")

apple = Phone("iPhone 13", "Pink", 1099, 2000, 100, "2234")
samsung = Phone("Samsung Galaxy S21", "Purple", 999, 1000, 200, "1234")
