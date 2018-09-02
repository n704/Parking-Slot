from constant import (
    CREATE_SLOTS_COMMAND, PARK_COMMAND, COMMANDS,
    LEAVE_COMMAND, STATUS_COMMAND,
    REG_CAR_WITH_COLOR,
    SLOTS_WITH_COLOR,
    SLOTS_WIH_REG_NUMBER
    )
from .parking_lot import ParkingLot

def create_parking_lot(commands):
    """
    Create parking lot
    @commands list of command
    """
    if len(commands) == 2:
        parking_lot = ParkingLot(commands[1])
    elif len(commands) == 1:
        raise Exception("Creating ParkingLot need size.\n")
    else:
        raise Exception("Too Many commands. \n")
    return parking_lot

def park_a_car(commands, parking_lot):
    """
    Function to park a new car.

    @commands list of COMMANDS
    @parking_lot ParkingLot object to invoke method
    @returns parking_lot object
    """
    if parking_lot:
        if len(commands) == 3:
            print parking_lot.park_a_car(commands[1], commands[2])
            return parking_lot
        else:
            raise Exception("Input Reg number and color.")
    raise Exception("Sorry, No Parking lot.")

def leave_parking_lot(commands, parking_lot):
    """
    function to leave a car from parking Lot
    @commands list of COMMANDS
    @parking_lot ParkingLot object to invoke method

    @returns parking_lot
    """
    if parking_lot:
        if len(commands) == 2:
            print parking_lot.car_is_leaving(commands[1])
            return parking_lot
        else:
            raise Exception("Input Reg number and color.")
    raise Exception("Sorry, No Parking lot.")

def status_parking_lot(commands, parking_lot):
    """
    print status of the parking_lot
    @commands list of COMMANDS
    @parking_lot ParkingLot object to invoke method

    @returns parking_lot
    """
    if parking_lot:
        parking_lot.status_of_parking_lot()
        return parking_lot
    raise Exception("Sorry, No Parking lot.")

def reg_car_with_color(commands, parking_lot):
    """
    function to leave a car from parking Lot
    @commands list of COMMANDS
    @parking_lot ParkingLot object to invoke method

    @returns parking_lot
    """
    if parking_lot:
        if len(commands) == 2:
            print parking_lot.registration_numbers_for_cars_with_colour(commands[1])
            return parking_lot
        else:
            raise Exception("Input color is needed.")
    raise Exception("Sorry, No Parking lot.")

def slots_with_color(commands, parking_lot):
    """
    function to return slots of car with color
    @commands list of COMMANDS
    @parking_lot ParkingLot object to invoke method

    @returns parking_lot
    """
    if parking_lot:
        if len(commands) == 2:
            print parking_lot.slot_numbers_for_cars_with_colour(commands[1])
            return parking_lot
        else:
            raise Exception("Input Color is needed")
    raise Exception("Sorry, No Parking lot.")

def slots_with_reg_number(commands, parking_lot):
    """
    function to car with registration_number
    @commands list of COMMANDS
    @parking_lot ParkingLot object to invoke method

    @returns parking_lot
    """
    if parking_lot:
        if len(commands) == 2:
            print parking_lot.slot_number_for_registration_number(commands[1])
            return parking_lot
        else:
            raise Exception("Input Reg number needed")
    raise Exception("Sorry, No Parking lot.")

def execute_command(commands, parking_lot=None):
    """
    @commands: list of command
    """

    if commands[0].strip() == CREATE_SLOTS_COMMAND:
        return create_parking_lot(commands)
    elif commands[0].strip() == PARK_COMMAND:
        return park_a_car(commands, parking_lot)
    elif commands[0].strip() == LEAVE_COMMAND:
        return leave_parking_lot(commands, parking_lot)
    elif commands[0].strip() == STATUS_COMMAND:
        return status_parking_lot(commands, parking_lot)
    elif commands[0].strip() == REG_CAR_WITH_COLOR:
        return reg_car_with_color(commands, parking_lot)
    elif commands[0].strip() == SLOTS_WITH_COLOR:
        return slots_with_color(commands, parking_lot)
    elif commands[0].strip() == SLOTS_WIH_REG_NUMBER:
        return slots_with_reg_number(commands, parking_lot)
    return
