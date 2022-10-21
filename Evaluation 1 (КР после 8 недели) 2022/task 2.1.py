import numpy as np


def angle_vec(vec_1, vec_2):
    scalinner = np.inner(vec_1, vec_2)
    vec_norm_1 = np.sqrt(np.inner(vec_1, vec_1))
    vec_norm_2 = np.sqrt(np.inner(vec_2, vec_2))

    angle = 180/np.pi * np.arccos(scalinner/(vec_norm_1 * vec_norm_2))
    return angle
