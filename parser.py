# parser.py
# data from the CLI is a list - params
# the parser shall also return a list if the parsing
# was successful else raise an error and exit with an
# error message

import sys

# destructure param
# operator, first operand, second operand = param


def parser(params=[]):
    operators = ['+', '-', '*', '**', '/', '%']

    # an operand can only be an integer or a float
    operand_types = [int, float]

    try:
        # only 3 parameters are needed
        if len(params) != 3:
            message = "In essence, an operator and two number"
            message += " operands are required. Eg: + 2 4.6"
            raise ValueError(message)

        if not params[0] in operators:
            raise ValueError(f"Unknown operator, choose from {operators}")

        if (type(params[1]) in operand_types and
                type(params[2]) in operand_types):
            raise ValueError(f"A number is required as operand")

        parsed_params = [params[0], float(params[1]), float(params[2])]

        if parsed_params[0] in operators[4:] and parsed_params[2] == 0:
            message = "None zero second operand is required for division"
            raise ZeroDivisionError(message)

        # pass the index of the operator rather than the character
        # we shall use the index to easily determine the operation
        # to call using few or not if statements
        parsed_params[0] = operators.index(parsed_params[0])

    except Exception as err_message:
        print(err_message)
        sys.exit()

    return parsed_params
