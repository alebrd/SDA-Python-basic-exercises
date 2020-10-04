class BasicCalculator:
    def __init__(self):
        self.numbers = []
        self.operand = ""
        self.result = []
    def provide_number(self, number):
        self.numbers.append(number)
    def provide_operand(self, operand):
        self.operand = operand
    def show_result(self):
        if self.operand == '+':
            self.result.append(self.numbers[0] + self.numbers[1])
        elif self.operand == '-':
            self.result.append(self.numbers[0] - self.numbers[1])
        else:
            raise Exception("operand not supported")

        return self.result