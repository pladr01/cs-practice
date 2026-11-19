import numpy as np
def make_hours():
    return np.arange(0,22,3).tolist()

def vector_report(values):
    return {"third":values[2],
            "last":values[-1],
            "middle":values[2:6],
            "every_second":values[::2],
            "reversed": values[::-1]}

def change_vector(values):
    new_values=np.asanyarray(values).copy()
    new_values[2:5]=99
    new_values[::2]=-1
    return new_values.tolist()

def cap_above(values, limit):
    new_values=values.copy()
    mask=new_values>limit
    new_values[mask]=limit
    return new_values.tolist()

def celsius_to_fahrenheit(values):
    new_values = values.copy()
    new_values[::1]=new_values[::1]*9/5+32
    return new_values.tolist()
