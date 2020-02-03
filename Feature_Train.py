import numpy as np
import librosa
import scipy.io

fs = 8000


def mfcc_from_mat(path, fs):
    mat = scipy.io.loadmat(path)
    mat = mat['y']
    mat = mat[0:8000, :]  # shorten to 1 seconds
    arr = []
    for i in range(mat.shape[1]):
        m = librosa.feature.mfcc(mat[:, i], fs)
        arr.append(m)
    return np.array(arr)


aaa = mfcc_from_mat('data/aaa.mat', fs)
eee = mfcc_from_mat('data/eee.mat', fs)
iii = mfcc_from_mat('data/iii.mat', fs)
ooo = mfcc_from_mat('data/ooo.mat', fs)
uuu = mfcc_from_mat('data/uuu.mat', fs)
yyy = mfcc_from_mat('data/yyy.mat', fs)

train_input = np.concatenate((aaa, eee, iii, ooo, uuu, yyy))
train_input = np.expand_dims(train_input, 3)

ta = np.zeros((30, 6))
ta[:, 0] = 1
te = np.zeros((30, 6))
te[:, 1] = 1
ti = np.zeros((30, 6))
ti[:, 2] = 1
to = np.zeros((30, 6))
to[:, 3] = 1
tu = np.zeros((30, 6))
tu[:, 4] = 1
ty = np.zeros((30, 6))
ty[:, 5] = 1
train_labels = np.concatenate((ta, te, ti, to, tu, ty))
