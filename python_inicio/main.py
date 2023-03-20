import math


class ShapeCalculator:
    def circle(self):
        try:
            c_radius = float(input("Try to type the radius value: "))
            if c_radius < 0:
                print("Number invalid! Try another above 0.")
            else:
                circ_res = 2 * math.pi * c_radius
                formatted_result = "{:.2f}".format(circ_res)
                print("The circle's area is:", formatted_result)
        except ValueError:
            print("Your input is invalid, try a real number.")

    def rectangle(self):
        try:
            a_rect = float(input("Try to type the area value: "))
            if a_rect < 0:
                print("Number invalid! Try another above 0.")
            else:
                b_rect = float(input("Try to type the base value: "))
                if b_rect < 0:
                    print("Number invalid! Try another above 0.")
                else:
                    rec_res = (a_rect * b_rect) / 2
                    formatted_result = "{:.2f}".format(rec_res)
                    print("The rectangle's area is:", formatted_result)
        except ValueError:
            print("Your input is invalid, try a real number.")


if __name__ == "__main__":
    x = ShapeCalculator()
    y = ShapeCalculator()

    choice = input("What area do you wanna know? Circle or Rectangle? ")

    if choice.lower() == "circle":
        x.circle()
    elif choice.lower() == "rectangle":
        y.rectangle()
    else:
        print("Your type is invalid, try circle or rectangle.")
