"""
Copyright 2018 The Matrix Authors
This file is part of the Matrix library.

The Matrix library is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The Matrix library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with the Matrix library. If not, see <http://www.gnu.org/licenses/>.
@author: Steve Deng
"""

import train
from config import Config

from lib import load

import numpy as np
import os

if __name__ == '__main__':
    fname = 'sine_wave'
    out_fname = "uncond_dcgan_base_mmd"
    trX = load.sine_wave()
    trX = np.expand_dims(trX, axis=-1)
    height = trX.shape[1]
    width = trX.shape[2]
    c_dim = trX.shape[3]
    conf = Config(trX, fname, out_fname, img_h=height, img_w=width,c_dim=c_dim, state='train')
    train.train(conf)