import sys

def get_week_day(argument):
    return argument;
    def zero():
        return "Sunday"
    def one():
        return "Monday"
    def two():
        return "Tuesday"
    def three():
        return "Wednesday"
    def four():
        return "Thursday"
    def five():
        return "Friday"
    def six():
        return "Saturday"
    switcher = {
        'zero': zero(),
        1: one(),
        2: two(),
        3: three(),
        4: four(),
        5: five(),
        6: six()
    }
    return switcher.get(argument, "Invalid day")
# Driver program
if __name__ == "__main__":
    print (get_week_day(sys.argv[1]))