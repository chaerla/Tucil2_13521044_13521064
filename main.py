from lib.Point import Point
from lib.ClosestPair import *

point_list = []
for i in range (5):
    temp_point = Point(3)
    temp_point.get_coordinates()
    point_list.append(temp_point)

print(brute_force(point_list)[0])
print(solve(point_list, 0))
brute_force(point_list)[1][0].print()
brute_force(point_list)[1][1].print()
print()
solve(point_list, 0)[1][0].print()
solve(point_list, 0)[1][1].print()