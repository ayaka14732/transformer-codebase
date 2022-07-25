import os
os.environ['XLA_FLAGS'] = os.environ.get('XLA_FLAGS', '') + ' --xla_force_host_platform_device_count=32'

import jax
jax.config.update('jax_platform_name', 'cpu')

import jax.numpy as np
import numpy as onp

from jax.experimental.maps import Mesh
from jax.experimental.pjit import PartitionSpec as P
from jax.experimental.pjit import pjit

devices = jax.devices()

def f(a, b, c):
    # a: (16, 32)
    # b: (32, 32)
    # c: (32, 32)
    x = np.vstack((a, a))
    return x + b + c

a = np.asarray(onp.random.rand(16, 32))
b = np.asarray(onp.random.rand(32, 32))
c = np.asarray(onp.random.rand(32, 32))

y1 = f(a, b, c)

g = pjit(
    f,
    in_axis_resources=(P('x', 'y'), P('x', 'y'), P('x', 'y')),
    out_axis_resources=P('x', 'y'),
)

mesh_devices = onp.array(devices).reshape(4, 8)

with Mesh(mesh_devices, ('x', 'y')):
    y2 = g(a, b, c)

y1
y2

y2.shape

for x in y2.device_buffers:
    print(x.shape)
