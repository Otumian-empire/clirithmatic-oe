# app.py
import sys
from parser import parser
from backend import Backend


if __name__ == "__main__":

    # sys.argv[0] is the file - app.py
    params = parser(sys.argv[1:])

    app = Backend(params)
    print(app.eval())
