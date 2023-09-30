#mean
def mean(numbers):
    mean = sum(numbers)/len(numbers)
    return mean

#variance
def variance(numbers):
    calc_mean = mean(numbers)
    sqd_vals = []
    for i in numbers:
        sqd_diff = (i-calc_mean)**2
        sqd_vals.append(sqd_diff)
    var = sum(sqd_vals)/len(numbers)
    return var

#standard deviation
def std_dev(numbers):
    calc_var = variance(numbers)
    std_dev = calc_var**0.5
    return std_dev

#standard error
def std_err(numbers):
    calc_SD = std_dev(numbers)
    std_err = calc_SD/((len(numbers)**0.5))
    return std_err

#z-score
def z_score(obs, numbers):
    calc_mean = mean(numbers)
    calc_SD = std_dev(numbers)
    z_score = (obs - calc_mean) / calc_SD
    return z_score