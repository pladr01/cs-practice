import Numpy  as np

def reshape_rows(values, width):
    data=np.asarray(values)
    if width>0 and data.size % width==0:
        return np.round(data.reshape(-1, width), 6).tolist()
    return []


def block(matrix,rows,columns):
    data=np.asarray(matrix)
    if data.size==0:
        return []
    return np.round(data[np.ix_(rows, columns)], 6).tolist()


def column_means(matrix):
    data=np.asarray(matrix)
    if data.size==0:
        return []
    return np.round(data.mean(axis=0), 6).tolist()


def column_range(matrix, column):
    data=np.asarray(matrix)
    if data.size==0:
        return 0.0
    values=data[:, column]
    return float(np.round(values.max() - values.min(), 6))