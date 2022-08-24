import random

num_done = []

def generate():
    random_num = random.randint(0, 9)

    if random_num in num_done:
        generate()
    else:
        num_done.append(random_num)

for num in range(9):
    generate()