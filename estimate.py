import random

def wallis(x):
    multiplier = 2
    product = 1
    for i in range(x):
        term = multiplier**2 /(multiplier**2 - 1)
        product *= term
        multiplier += 2

    return 2*product


def monte_carlo(x):
    circle_inside_points = 0
    square_inside_points = 0
    for i in range(x):
        rand_x=random.uniform(-1,1)
        rand_y=random.uniform(-1,1)
        distance=math.sqrt(rand_x**2 + rand_y**2)


        if(distance<1):
            circle_inside_points += 1

        square_inside_points += 1


        pi= (4*circle_inside_points)/square_inside_points

    return pi
