from flax.serialization import msgpack_restore
import numpy as np

def load_params(filename):
    with open(filename, 'rb') as f:
        serialized_params = f.read()
    return msgpack_restore(serialized_params)

src = load_params('src.dat')
packed_mask_enc_1d = load_params('packed_mask_enc_1d.dat')
dst = load_params('dst.dat')
packed_mask_dec_1d = load_params('packed_mask_dec_1d.dat')

mask_enc_1d = np.unpackbits(packed_mask_enc_1d, axis=1).astype(np.bool_)
mask_dec_1d = np.unpackbits(packed_mask_dec_1d, axis=1).astype(np.bool_)

print('src.dtype:', src.dtype)
print('src.shape:', src.shape)
print('mask_enc_1d.dtype:', mask_enc_1d.dtype)
print('mask_enc_1d.shape:', mask_enc_1d.shape)
print('dst.dtype:', dst.dtype)
print('dst.shape:', dst.shape)
print('mask_enc_1d.dtype:', mask_enc_1d.dtype)
print('mask_enc_1d.shape:', mask_enc_1d.shape)
