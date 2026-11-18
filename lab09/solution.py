import numpy as np
def make_hours():
    return np.arange(0,22,3).tolist()

def vector_report(values):
    sl={}
    sl.append(values[2],values[-1])
    sl.append(values[2:6])
    sl.append(values[::2])
    sl.append(values[::-1])
    return np.asarray(sl).tolist()

def change_vector(values):
    new_values=values.copy()
    new_values[2:5]=99
    new_values[::2]=-1
    return np.asarray(new_values).tolist()

def cap_above(values, limit):
    new_values=values.copy()
    mask=new_values>limit
    new_values[mask]=limit
    return new_values.tolist()

def celsius_to_fahrenheit(values):
    new_values = values.copy()
    new_values[::1]*=new_values*9/5+32
    return new_values.tolist()