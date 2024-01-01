# Re-calculate the confidence interval for theta when M = 3
# Solving for theta using the CDF formula for the maximum of uniform distributions

# Given M value for calculation
M_observed = 3

# Calculate the confidence interval for theta using the percentiles for a 90% confidence interval
# We find theta for the 5th percentile (lower bound of theta)
theta_5th_percentile = M_observed / (lower_percentile ** (1/12))

# We find theta for the 95th percentile (upper bound of theta)
theta_95th_percentile = M_observed / (upper_percentile ** (1/12))

theta_5th_percentile, theta_95th_percentile
