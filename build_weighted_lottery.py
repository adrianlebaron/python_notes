# import random

# weights = {
#         'winning': 1,
#         'losing': 1000
#     }

# # weighted_lottery(weights)

# other_weights = {
#         'winning': 1,
#         'break_even': 2,
#         'losing': 3
#     }

# # weighted_lottery(other_weights)

# print(random.choice([k for k in other_weights for x in other_weights[k]]))



# random.choice([k for k in d for x in d[k]])


# d = {
#  'a': [1, 3, 2],
#  'b': [6],
#  'c': [0, 0]
# }


# import random

# weights = {
#         'winning': 1,
#         'losing': 1000
#     }

# other_weights = {
#         'winning': 1,
#         'break_even': 2,
#         'losing': 3
#     }

# # weighted_lottery(other_weights)

# weighted_lottery = random.choice([key for key, values in other_weights.iteritems() for x in values])

# print(weighted_lottery)


import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight): #underscore is to use with smaller formulas
            container_list.append(name)

    return np.random.choice(container_list)#np.random.choice

#  weights = {
#      'winning': 1,
#      'losing': 1000
#  }
#
#  print(weighted_lottery(weights))

other_weights = {
    'green': 1,
    'yellow': 2,
    'red': 3
}

print(weighted_lottery(other_weights))