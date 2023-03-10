from .Point import *

def brute_force(point_list):
    """
    Recursively find the closest pair of points in point_list using brute force algorithm

    Args:
        point_list (list): List of Point objects

    Returns:
        tuple: A tuple of the minimum distance and the related pair of points 
    """
    min = float("inf")
    if(len(point_list)==1):
        return (min, None)
    for i in range (len(point_list)):
        for j in range (i+1, len(point_list)):
            dist = Point.distance(point_list[i], point_list[j])
            if (dist < min):
                min = dist
                closest_pair = (point_list[i], point_list[j])
    return (min, closest_pair)

def strip_closest(strip, closest_pair):
    """
    Recursively find the closest pair of points in point_list using divide and conquer algorithm

    Args:
        point_list (list): List of Point objects (prereq: size must be >= 2)
        step (int): current step (the pointss will be sorted by "step" dimension)

    Returns:
        tuple: A tuple of the minimum distance and the related pair of points 
    """
    # closest_pair = (strip[0], strip[1])
    dim = strip[0].dimension-1 # use the "last" dimension 
    strip = sort_points_by_dimension(strip, dim) # sort the points by the "last" dimension
    n = len(strip)
    for i in range (n):
        for j in range (i+1, n):
            if (strip[j].coordinates[dim] - strip[i].coordinates[dim] >= closest_pair[0]): 
                break
            dist = Point.distance(strip[i], strip[j])
            if dist < closest_pair[0]:
                closest_pair = (dist, (strip[i], strip[j]))
    return closest_pair


def solve(point_list, step):
    """
    Recursively find the closest pair of points in point_list using divide and conquer algorithm

    Args:
        point_list (list): List of Point objects (prereq: size must be >= 2)
        step (int): current step (the pointss will be sorted by "step" dimension)

    Returns:
        tuple: A tuple of the minimum distance and the related pair of points 
    """

    point_list = sort_points_by_dimension(point_list, step)
    n = len(point_list)

    # if the size of the point_list is <= 3, no need to divide
    if (n<=3):
        return brute_force(point_list)
    
    # get the middle point
    mid = n//2
    mid_point = point_list[mid]

    # partition the list
    left_points = point_list[:mid]
    right_points = point_list[mid:]

    # find the closest pair of each of the partitions
    closest_left_points = solve(left_points, step)
    closest_right_points = solve(right_points, step)

    # find the closer pair between the left closest pair and the right closest pair
    if (closest_left_points[0]<closest_right_points[0]):
        closest_pair = closest_left_points
    else:
        closest_pair = closest_right_points

    # Handle the points whose distance with the middle slab is smaller than the closest pair distance
    slab = []
    for point in point_list:
        if (abs(point.coordinates[step]-mid_point.coordinates[step]) < closest_pair[0]):
            slab.append(point)
    
    if (step < mid_point.dimension - 2): # If the current step is examining in larger than 2 dimensional
        closest_pair_slab = solve(slab, step+1)
        if(closest_pair_slab[0] < closest_pair[0]):
            return closest_pair_slab
    else: # The current step is examining in 2D and there are at least two points in the strip
        closest_pair = strip_closest(slab, closest_pair)
    return closest_pair

    
def sort_points_by_dimension(point_list, n):
    """
    Sort a list of points by the n-th dimension using merge sort algorithm

    Args:
        point_list (list): List of Point objects
        n (int): Index of the dimension to sort by (0-based)

    Returns:
        list: Sorted list of Point objects
    """
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].coordinates[n] <= right[j].coordinates[n]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    
    def merge_sort(point_list):
        if len(point_list) <= 1:
            return point_list
        mid = len(point_list) // 2
        left = merge_sort(point_list[:mid])
        right = merge_sort(point_list[mid:])
        return merge(left, right)
    
    return merge_sort(point_list)

def print_closest_pair(closest_pair):
    print("Distance:", closest_pair[0]) 
    print("Point 1: "), closest_pair[1][0].print()
    print("\n")
    print("Point 2: "), closest_pair[1][1].print()
    print("\n")