import random

def run_simulation():
    seed_value = int(raw_input('Enter random seed value: '))
    random.seed(seed_value)
    shots = int(raw_input('How many shots did Hobbes take? '))
    distance = int(raw_input('How far is it to Hobbes\' home? '))
    hole = random.randint(1, distance - 1)
    print 'Hole position is {0}'.format(hole)
    level = get_level(shots)
    print 'Level is {0}'.format(level)
    step_length, forward_steps, backward_steps = get_walk(level)
    print 'Step length is {0}'.format(step_length)
    print 'Step pattern is {0} forward and {1} backward'.format(forward_steps, backward_steps)
    print
    current_position = 0
    step_pattern = [] + [1] * forward_steps + [-1] * backward_steps
    current_position = 0
    current_list = [0]
    while True:
        for direction in step_pattern:
            current_position = update(current_position, direction, step_length)
            current_list.append(current_position)
            if direction > 0:
                print 'Hobbes steps forward to {0}'.format(current_position)
            else:
                print 'Hobbes staggers backward to {0}'.format(current_position)
        print
        if current_position == hole:
            print 'Oh no! Hobbes fell near the bar!'
            break
        elif current_position >= distance:
            print 'Hurray! Hobbes makes it through the day!'
            break
    return current_list

def get_level(num_drinks):
    level = num_drinks / 3
    return level if level <= 4 else 4

def get_walk(drunk_level):
    step_length = random.randint(1, 5 - drunk_level)
    forward_steps = random.randint(4, 6)
    backward_steps = forward_steps - random.randint(1, 3)
    return [step_length, forward_steps, backward_steps]

def update(current_position, step_direction, step_length):
    return current_position + step_direction * step_length

print run_simulation()