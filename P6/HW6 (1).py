import random

def run_simulation():
    random_seed = int(raw_input("Enter random seed value:"))
    num_drinkes = int(raw_input("How many shots did Hobbes take?"))
    distance    = int(raw_input("How far is it to Hobbes' home?"))
    random.seed(random_seed)
    pothole = random.randint(1,distance-1)
    print "Hole position is", pothole
    drunk_level = get_level(num_drinkes)
    print "Level is", drunk_level
    [step_length,num_forward,num_backward]=get_walk(drunk_level)
    print "Step length is", step_length
    print "Step pattern is", num_forward, "forward and", num_backward, "backward"
    current_position=0
    pos = []
    pos.append(current_position)
    while current_position != pothole and current_position < distance:
        for i in range(num_forward):
            current_position = update(current_position, 1, step_length)
            pos.append(current_position)

        for i in range(num_backward):
            current_position = update(current_position, -1, step_length)
            pos.append(current_position)
    if current_position == pothole:
        print "Oh no! Hobbes fell near the bar!"
    if current_position >= distance:
        print "Hurray! Hobbes makes it through the day!"
    return pos


def get_level(num_drinks):
    if num_drinks >= 0 and num_drinks <= 2:
        return 0
    elif num_drinks >= 3 and num_drinks <= 5:
        return 1
    elif num_drinks >= 6 and num_drinks <= 8:
        return 2
    elif num_drinks >= 9 and num_drinks <= 11:
        return 3
    elif num_drinks >= 12:
        return 4
    else:
        return None

def get_walk(drunk_level):
    step_length = random.randint(1,5-drunk_level)
    num_forward = random.randint(4,6)
    num_backward = num_forward-random.randint(1,3)
    return [step_length,num_forward,num_backward]

def update(current_position, step_direction, step_length):
    return current_position + step_direction * step_length


if __name__ == "__main__":
    print run_simulation()