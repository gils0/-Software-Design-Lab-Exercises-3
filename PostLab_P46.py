import numpy as np

p = 0.01
slot_duration = 10
test_duration = 60
timeslots_left = test_duration * 1000 * 1000 / 20
transmission_array = []
while timeslots_left >= 0:
    rand_num = np.random.choice((0, 1), p=[1 - p, p])
    if rand_num == 1:
        for i in range(0, slot_duration):
            for j in range(0, 400):
                transmission_array.append(1)
        timeslots_left -= slot_duration
    else:
        for j in range(0, 400):
            transmission_array.append(0)
        timeslots_left -= 1