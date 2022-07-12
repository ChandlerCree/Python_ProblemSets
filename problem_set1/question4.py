import random

print("\nPS1 Question 4 (David Chandler Cree)")

print("Ratio of pointsw inside circle to the total number of points should be approximately pi/4. ")
print("This can be translated to: ")
print("pi = 4 * [(num points inside circle)/(num points inside square)]")
print("area of square = 4r^2.")
print("area of circle = pi*r^2")
print("area of circle/area of square = (pi*r^2)/(4r^2) = pi/4")
print("To determine if a point is inside the circle the following algorithm will be run:")
print("x^2 + y^2 <= 1 --- and if this is true then the point appears inside the circle.")
print("Now for the proof.")



def calculate_pi(points):
    inside_circle = 0
    inside_square = 0

    for i in range(points):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_distance = rand_x**2 + rand_y**2

        if origin_distance <= 1:
            inside_circle += 1

        inside_square += 1

    #note that every point will fall within the square
    #therefore the value of estimations provided by the user could be used as the value for square
    return inside_circle, inside_square



if __name__ == "__main__":

    estimations = int(input("\n\n\nPlease enter the number of estimation points to be run: "))

    circle, square = calculate_pi(estimations)

    print(f"Number of points within circle = {circle}\nNumber of points within square = {square}")

    pi = 4 * circle/square

    print("Estimation of pi: ", pi)
