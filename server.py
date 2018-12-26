import socket
def calculate(message):
    number = []
    parameters = []
    math_operations =['add','sub','mul','div']
    parameters = message.split()
    if len(parameters)>3:return "Invalid request : you must enter three parameters"
    if not