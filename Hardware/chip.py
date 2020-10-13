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

"""Basis module for representing a quantum chip's information."""

import json

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
    
        
class Qubit(AttrDict):
    def __init__(self, index, attrs=None):
        self.index = index
        if attrs is None:
            attrs = AttrDict()
        
        self.attrs = attrs
    
    @classmethod
    def from_dict(cls, in_dict):
        return Qubit(in_dict['index'], attrs=AttrDict(**in_dict['attrs']))
    
    def to_dict(self):
        return {
            'index': self.index,
            'attrs': dict(self.attrs)
        }
    
    def __repr__(self):
        return "Qubit({0}, attrs={1})".format(self.index, self.attrs)

class Chip:
    def __init__(self, qubits):
        self._qubits = {}
        
        for qubit in qubits:
            if isinstance(qubit, Qubit):
                self._qubits[qubit.index] = qubit
            else:
                self._qubits[qubit] = Qubit(qubit)
    
    @property
    def qubits(self):
        return sorted(self._qubits.values(), key=lambda q: q.index)
    
    @classmethod
    def load(cls, filepath):
        with open(filepath, 'r') as f:
            in_dict = json.load(f)
        
        return cls.from_dict(in_dict)
    
    @classmethod
    def from_dict(cls, in_dict):
        return Chip(Qubit.from_dict(qubit) for qubit in in_dict['qubits'])
        
    def save(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f)
    
    def to_dict(self):
        qubits = []
        for qubit in self._qubits.values():
            qubits.append(qubit.to_dict())
        
        return {
            'qubits': qubits
        }

    def get_qubit(self, qubit):
        return self._qubits[qubit]
    
    def __repr__(self):
        return "Chip({})".format(repr(self.qubits)[1:-1])