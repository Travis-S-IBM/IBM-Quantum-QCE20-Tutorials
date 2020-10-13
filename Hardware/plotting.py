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

"""Basic plots for notebook."""

import matplotlib.pyplot as plt

def plot_cr45(amps, control_values_no_flip, control_values_flip, 
              target_values_no_flip, target_values_flip, 
              target_fit_no_flip, target_fit_flip):
    
    plt.plot(amps, target_fit_no_flip, color='blue')
    plt.plot(amps, target_fit_flip, color='blue')
    plt.scatter(amps, control_values_no_flip, color='red', label='control - |00>')
    plt.scatter(amps, control_values_flip, color='red', label='control - |10>', marker='x')
    plt.scatter(amps, target_values_no_flip, color='blue', label='target - |00>')
    plt.scatter(amps, target_values_flip, color='blue', label='target - |10>', marker='x')
    plt.legend(loc="upper left")
    plt.xlabel("Drive amp [a.u.]", fontsize=15)
    plt.ylabel("Measured signal [a.u.]", fontsize=15)