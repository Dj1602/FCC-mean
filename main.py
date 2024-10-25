import numpy as np

def calculate(arr):
    if len(arr) != 9:
        raise ValueError('List must contain nine numbers.')
    reshaped_arr = np.array(arr).reshape((3,3))
    # Calculate mean
    mean = np.mean(reshaped_arr).item()
    mean_axis1 = np.mean(reshaped_arr, axis=0)
    mean_axis2 = np.mean(reshaped_arr, axis=1)

    # Calculate variance
    var = np.var(reshaped_arr).item()
    var_axis1 = np.var(reshaped_arr, axis=0)
    var_axis2 = np.var(reshaped_arr, axis=1)

    # Calculate standard deviation
    std = np.std(reshaped_arr).item()
    std_axis1 = np.std(reshaped_arr, axis=0)
    std_axis2 = np.std(reshaped_arr, axis=1)

    # Find the max
    max = np.max(reshaped_arr).item()
    max_axis1 = np.max(reshaped_arr, axis=0)
    max_axis2 = np.max(reshaped_arr, axis=1)

    # Find the min
    min = np.min(reshaped_arr).item()
    min_axis1 = np.min(reshaped_arr, axis=0)
    min_axis2 = np.min(reshaped_arr, axis=1)

    # Find the sum
    sum = np.sum(reshaped_arr).item()
    sum_axis1 = np.sum(reshaped_arr, axis=0)
    sum_axis2 = np.sum(reshaped_arr, axis=1)

    # Structure the result
    result = {
        'mean': [mean_axis1.tolist(), mean_axis2.tolist(), mean],
        'variance': [var_axis1.tolist(), var_axis2.tolist(), var],
        'standard deviation': [std_axis1.tolist(), std_axis2.tolist(), std],
        'max': [max_axis1.tolist(), max_axis2.tolist(), max],
        'min': [min_axis1.tolist(), min_axis2.tolist(), min],
        'sum': [sum_axis1.tolist(), sum_axis2.tolist(), sum]
    }
    return result

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
