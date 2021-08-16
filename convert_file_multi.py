import numpy as np
from scipy import io
from glob import glob
import os
from scipy.spatial.distance import cdist


ds = glob(os.path.join("multi_dist", "*.npy"))

labels = [int(x.split(os.path.sep)[-1].split("_")[0]) for x in ds]
runfiles = []
for idx, d in enumerate(ds):
    v = np.load(d)

    xs, ys = [], []
    for t in range(v.shape[0]):
        x, y = np.where(v[t, ..., 1])
        xs.append(x.astype(np.float64))
        ys.append(y.astype(np.float64))
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    # Find start loc
    sx, sy = np.where(v[0, ..., 0])
    sx = np.mean(sx)
    sy = np.mean(sy)

    # Find goal loc
    tx, ty = np.where(v[0, ..., 2])
    tx = np.mean(tx)
    ty = np.mean(ty)

    io.savemat(os.path.join("multi_mat", "vid_{}.mat".format(idx)), {"video": v, "xs": xs, "ys": ys, "tx": tx, "ty": ty, "sx": sx, "sy": sy, "label": labels[idx]})
    runfiles.append('matlab -nodisplay -r "multi_dist_fly_tracker_studentdave({}); exit"'.format(idx))

# Create the run script
with open('run_multidist.sh', 'w') as f:
    for item in runfiles:
        f.write("{}\n".format(item))

