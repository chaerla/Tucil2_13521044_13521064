from lib.Point import Point
from lib.ClosestPair import *

point_list = []
for i in range (5):
    temp_point = Point(dimension=4)
    temp_point.get_coordinates()
    point_list.append(temp_point)

print()
print("Result by brute force: ")
print(brute_force(point_list)[0])
brute_force(point_list)[1][0].print()
brute_force(point_list)[1][1].print()
print()
print("Result by divide and conquer: ")
print(solve(point_list, 0)[0])
solve(point_list, 0)[1][0].print()
solve(point_list, 0)[1][1].print()