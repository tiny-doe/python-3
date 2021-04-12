def get_y(m, x, b):
    y = (m * x) + b
    return y

#testing time
print(get_y(1, 0, 7) == 7)
#should return true
print(get_y(5, 10, 3) == 25)
#should return false
print(get_y(.3, 6, 1.7) == 3.5)
#should return true
print(get_y(.3, 20, 10) == 16)
#should return true
print()

#time to calculate the best fit line
def calculate_error(m, b, point):
    x_point, y_point = point
    y = m*x_point + b
    distance = abs(y - y_point)
    return distance
  
#testing time
#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))
print()

#our dataset: 1st value is the ball number, 2nd value is bounce height
#don't ask how the 2cm ball literally didn't bounce
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print(datapoints)
print()

def calculate_all_error(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error
  
#testing time
#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))
#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))
#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))
print()

possible_ms = [m * -.1 for m in range(-100, 101)]
possible_bs = [b * -.1 for b in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        all_errors = calculate_all_error(m, b, datapoints)
        if all_errors < smallest_error:
            best_m = m
            best_b = b
            smallest_error = all_errors
print(best_m, best_b, smallest_error)
print("For the best fit line, use a slope of " + str(round(best_m, 2)) + ", a y-intercept of " + str(round(best_b, 2)) + ".")