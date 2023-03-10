from lib.Point import Point
from lib.ClosestPair import *
from lib.Util import *
import time

continue_solver = True
splash_screen()
while(continue_solver):
    point_list = []
    Point.calculation_count = 0
    print("=========================o=========================")
    print()
    print("Welcome to our closest points generator!")
    print()
    number_of_points = get_num_of_points()
    dimension = get_dimension()
    print()
    print("Generating random points ...")
    for i in range(number_of_points):
        temp_point = generate_random_points(dimension)
        temp_point.print()
        print()
        point_list.append(temp_point)

    # Divide and Conquer
    start_time_1 = time.time()
    result_1 = solve(point_list, 0)
    end_time_1 = time.time()
    elapsed_time_1 = end_time_1 - start_time_1
    print()
    print("Result by divide and conquer:")              
    print_closest_pair(result_1)

    print("Calculation Count: ", Point.calculation_count)
    print("Time taken:", elapsed_time_1, "seconds", "\n")
    print()

    # Brute Force
    Point.calculation_count = 0
    start_time_2 = time.time()
    result_2 = brute_force(point_list)
    end_time_2 = time.time()
    elapsed_time_2 = end_time_2 - start_time_2

    print("Result by brute force: ")              
    print_closest_pair(result_2)

    print("Calculation Count: ", Point.calculation_count)
    print("Time taken:", elapsed_time_2, "seconds", "\n")
    print()

    # Point Plotter
    if (dimension == 3):
        list_of_points = [] # List Containing Points (As List)
        for point in point_list:
            list_of_points.append(point.coordinates)
        show_plotter(list_of_points, result_1[1][0].coordinates, result_1[1][1].coordinates)
    
    valid_continue_choice = False
    while (not valid_continue_choice):
        print("The two closest points have been found! Do you want to try again?")
        continue_choice = input("Input choice (y/n): ")
        if (continue_choice == "y"):
            continue_solver = True
            valid_continue_choice = True
        elif (continue_choice == "n"):
            continue_solver = False
            valid_continue_choice = True
            print()
            print_computer_spec()
            print()
            print("Thank you for trying our closest points generator! :)")
            print()
            print("=========================o========================= \n")
        else:
            print("Input invalid! Please input again! \n")
