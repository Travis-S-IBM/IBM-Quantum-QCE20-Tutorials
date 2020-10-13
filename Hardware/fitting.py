# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Basic module with fitting methods."""

import numpy as np
from scipy.optimize import curve_fit


def fit_function(x_values, y_values, function, init_params):
    fitparams, conv = curve_fit(function, x_values, y_values, init_params)
    y_fit = function(x_values, *fitparams)

    return fitparams, y_fit


def extract_cr_data(qubit, result, num_exps, scale_factor):
    values = []

    for i in range(num_exps*2):
        values.append(result.get_memory(i)[qubit] * scale_factor)

    values = np.real(values)
    values_no_flip = values[num_exps:]
    values_flip = values[:num_exps]
    return values_no_flip, values_flip