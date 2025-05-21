class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None

        if name is not None:
            self.name = name  # calls setter
        if breed is not None:
            self.breed = breed  # calls setter

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
