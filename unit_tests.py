from calc import My_Calculator

class Bulbulator_Tests:

    def __init__(self):
        self.calc = My_Calculator()
        self.assertion_message_error = " returned assertion error! Here are first term, second term and result:"

    def Sum_of_two_numbers(self):
        # Arrange
        first = 10
        second = 20

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == 30
        except AssertionError:
            print(self.Sum_of_two_numbers.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records)-1])
            print('\n')

    def Sum_negative_positive(self):
        # Arrange
        first = -10
        second = 4

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == -6
        except AssertionError:
            print(self.Sum_negative_positive.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_negative_positiveFloat(self):
        # Arrange
        first = -10
        second = 0.5

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == -9.5
        except AssertionError:
            print(self.Sum_negative_positiveFloat.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_large_numbers(self):
        # Arrange
        first = 192839128398123981239812389
        second = 192839128398123981239812389

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == 3856782567962478
        except AssertionError:
            print(self.Sum_large_numbers.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_large_positive_negative(self):
        # Arrange
        first = 192839128398123981239812389
        second = -192839128398123981239812390

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == -1
        except AssertionError:
            print(self.Sum_large_positive_negative.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_large_float(self):
        # Arrange
        first = 192839128398123981239812389
        second = -192839128398123981239812390.5

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == -1.5
        except AssertionError:
            print(self.Sum_large_float.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_float(self):
        # Arrange
        first = 5.134
        second = 1.23

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == 5.364
        except AssertionError:
            print(self.Sum_float.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_negative_float(self):
        # Arrange
        first = -5.134
        second = -1.23

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == -5.364
        except AssertionError:
            print(self.Sum_negative_float.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_negative_positiveFloat(self):
        # Arrange
        first = -5.134
        second = 1.23

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == 30
        except AssertionError:
            print(self.Sum_negative_positiveFloat.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')

    def Sum_BAZA(self):
        # Arrange
        first = 0.2
        second = 0.1

        # Act
        result = self.calc.sum(first, second)

        # Assert
        try:
            assert result == 0.3
        except AssertionError:
            print(self.Sum_BAZA.__name__ + self.assertion_message_error)
            print(self.calc.data._records[len(self.calc.data._records) - 1])
            print('\n')


if __name__ == '__main__':
    nagibator_machine = Bulbulator_Tests()
    nagibator_machine.Sum_of_two_numbers()
    nagibator_machine.Sum_negative_positive()
    nagibator_machine.Sum_negative_positiveFloat()
    nagibator_machine.Sum_large_numbers()
    nagibator_machine.Sum_large_positive_negative()
    nagibator_machine.Sum_large_float()
    nagibator_machine.Sum_float()
    nagibator_machine.Sum_negative_float()
    nagibator_machine.Sum_negative_positiveFloat()
    nagibator_machine.Sum_BAZA()
