from .commands import (
                       StatusCommand, UNKNOWNCommand, CreateParkingCommand,
                       LeaveCarCommand, RegCarWithColorCommand,
                       SlotNumWithColorCommand, SlotNumWithRegNumCommand,
                       ParkingCommand
                      )

COMMAND_MAP = {
    "status": StatusCommand,
    "park": ParkingCommand,
    "UNKNOWN": UNKNOWNCommand,
    "create_parking_lot": CreateParkingCommand,
    "leave": LeaveCarCommand,
    "registration_numbers_for_cars_with_colour": RegCarWithColorCommand,
    "slot_numbers_for_cars_with_colour": SlotNumWithColorCommand,
    "slot_number_for_registration_number": SlotNumWithRegNumCommand
}
