
steps = 8
path = "UDDDUDUU"


def countingValleys(steps, path):
    valleys = 0

    level = 0
    lowest_point = 0

    for i in range(steps):
        step = path[i]
        if step == 'U':
            level = level + 1
        else:
            level = level - 1

        if level == 0:
            if lowest_point < 0:
                # reached sealevel from a valley
                valleys = valleys + 1

            #reset heighest_point
            lowest_point = 0
        
        if level < lowest_point:
            lowest_point = level

    return valleys

print(countingValleys(steps, path))
            
