
# %%

%load_ext autoreload
%autoreload 2

import os
import sys
import numpy
import pandas
from matplotlib import pyplot
from statsmodels.tsa.api import VAR as pyvar
from lib import regression as reg
from lib import stats
from lib import config
from lib import var

pyplot.style.use(config.glyfish_style)

# %%

# %%

μ = [0.0, 0.0]
ω = numpy.matrix([[1.0, -0.5], [-0.5, 1.0]])
φ = numpy.array([
        numpy.matrix([[0.2, 0.2],
                      [0.2, 0.3]]),
        numpy.matrix([[0.3, 0.2],
                     [0.1, 0.4]])
])
var.eigen_values(φ)
x0 = numpy.array([[0.0, 1.0], [0.0, 1.0]])
n = 10000
xt = var.var_simulate(x0, μ, φ, ω, n)

# %%

M = var.stationary_mean(φ, μ)
Σ = var.stationary_covariance_matrix(φ, ω)
cov = stats.covariance(xt[0], xt[1])
plot_name = "var_2_estimation_2_x_y_timeseries"
title = f"VAR(2) Simulation: γ={format(Σ[0,1], '2.2f')}, " + \
         r"$\hat{\gamma}$=" + f"{format(cov, '2.2f')}, " + \
         r"$μ_x$=" + f"{format(M[0,0], '2.2f')}, " + \
         r"$σ_x$=" + f"{format(numpy.sqrt(Σ[0,0]), '2.2f')}, " + \
         r"$μ_y$=" + f"{format(M[1,0], '2.2f')}, " + \
         r"$σ_y$=" + f"{format(numpy.sqrt(Σ[1,1]), '2.2f')}"
ylabel = [r"$x$", r"$y$"]
var.timeseries_plot(xt, 1000, ylabel, title, plot_name)

# %%

theta = var.theta_parameter_estimation(xt)
var.split_theta(theta)

# %%

var.omega_parameter_estimation(xt, theta)
# %%

df = pandas.DataFrame({"x":xt[0], "y":xt[1]})
df.shape

n, l = df.shape
fig, axes = pyplot.subplots(l, sharex=True, figsize=(12, 9))
axes.flatten()
