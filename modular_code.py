import math
import numpy as np


def curved_score(arr, n):
    return [i + n for i in arr]


def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]


test_scores = [10, 20, 40, 34, 56, 54]
curved_5 = curved_score(test_scores, 5)
curved_10 = curved_score(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)

for score_list in test_scores, curved_5, curved_10, square_root_curve:
    print(np.mean(score_list))


'''bad code is written like this
import math
import numpy as np

test_scores = [10, 20, 40, 34, 56, 54]

curved_5 = [score + 5 for score in test_scores ]
print(np.mean(curved_5))

curved_10 = [score + 10 for score in test_scores ]
print(np.mean(curved_10))

curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_sqrt))'''
