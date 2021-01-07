# backend.py
class Backend:

    def __init__(self, params):
        self.operator, self.operand1, self.operand2 = params

    def add(self):
        return self.operand1 + self.operand2

    def mult(self):
        return self.operand1 * self.operand2

    def subt(self):
        return self.operand1 - self.operand2

    def div(self):
        return self.operand1 / self.operand2

    def mod(self):
        return self.operand1 % self.operand2

    def exp(self):
        return self.operand1 ** self.operand2

    def eval(self):
        # the operator is passed as int from the parser
        # this is the index of the operation needed
        operations = [self.add, self.subt,
                      self.mult, self.exp, self.div, self.mod]
        operation = operations[self.operator]

        return operation()
