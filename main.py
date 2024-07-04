import math

def euclideanDistance (point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    return distance

distances=[]
points = [(3, 4), (5, 6), (1, 7), (3, 8), (5, 8), (2, 1)]

for point in points:

    for point2 in points:

        if point == point2:
            continue

        else:
            distanceBetweenPoints =euclideanDistance(point, point2)
            if distanceBetweenPoints in distances:
                continue
            else:
                distances.append(distanceBetweenPoints)


distances.sort()

for distance in distances:
    print(distance)
print("------------------------")
print("Noktalar arasi en kucuk uzaklik: " + str(distances[0]))