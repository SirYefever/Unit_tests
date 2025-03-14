class My_Calculator:

    def __init__(self):
        self.data = History()

    def sum(self, a, b):
        result = a + b
        self.data.add_record(a, b, result)
        return result

class History:

    def __init__(self):
        self._records = []

    def add_record(self, a, b, result):
        self._records.append([a, b, result])

    def get_records(self):
        return self._records

