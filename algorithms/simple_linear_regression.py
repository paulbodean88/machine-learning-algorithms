# Estimate the mean and the variance for the input and output variables of the data set
# mean(x) = sum(x)/count(x)


def mean(values):
    """

    :param values: list of values
    :return: mean
    """
    return sum(values) / float(len(values))


# Calculate the variance: The variance is the sum squared difference for each value from the mean value.
# variance = sum( (x - mean(x))^2 )

def variance(values, mean_value):
    return sum([(x - mean_value) ** 2 for x in values])


def covariance(x, mean_x, y, mean_y):
    covariance_ = 0.0
    for i in range(len(x)):
        covariance_ += (x[i] - mean_x) * (y[i] - mean_y)

    return covariance_


# Estimate Coefficients
# B1 = sum((x(i) - mean(x)) * (y(i) - mean(y))) / sum( (x(i) - mean(x))^2 )
# B1 = covariance(x, y) / variance(x)
# B0 = mean(y) - B1 * mean(x)

def coefficients(data_set):
    x = [row_[0] for row_ in data_set]
    y = [row_[1] for row_ in data_set]
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]


# Simple linear regression
def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for r in test:
        y = b0 + b1 * r[0]
        predictions.append(y)

    return predictions
