class Car(object):
    """
    Car is a vehicale
    with 2 property
    registration_number and color
    """
    def __init__(self, registration_number, color):
        """
        Create a car with registration_number and color
        """
        self.registration_number = registration_number
        self.color = color
