import numpy as np
from scipy import io
from glob import glob
import os
from matplotlib import pyplot as plt


files = glob(os.path.join("multi_dist_results", "*.mat"))
files.sort(key=os.path.getmtime)
print(files)

perf = []
pos_correct = []
neg_correct = []
for vidx, f in enumerate(files):
    data = io.loadmat(f)
    vidmat = io.loadmat(os.path.join("multi_mat", "vid_{}.mat".format(int(f.split("_")[-1].split(".")[0]))))
    perf.append(data["correct"])
    label = vidmat["label"]
    if label and data["correct"]:
        pos_correct.append(1)
    elif label and not data["correct"]:
        pos_correct.append(0)
    elif not label and not data["correct"]:
        neg_correct.append(0)
    elif not label and data["correct"]:
        neg_correct.append(1)

mean_acc = np.mean(perf)
print("Per-video correctness")
print(perf)
print("Acc: {}".format(mean_acc))
print("Pos: {}/{}".format(np.sum(pos_correct), len(pos_correct)))
print("Neg: {}/{}".format(np.sum(neg_correct), len(neg_correct)))

# Now plot
for vidx in range(len(files)):
    vidmat = io.loadmat(os.path.join("multi_mat", "vid_{}.mat".format(vidx)))
    video = vidmat["video"]
    data = io.loadmat(files[vidx])
    track_h = data["Q_loc_estimateY"]
    track_w = data["Q_loc_estimateX"]

    # Plot the frame-by-frame
    f = plt.figure()
    for idx in range(len(video)):
        plt.subplot(8, 8, idx + 1)
        plt.axis("off")
        plt.imshow(video[idx])
    plt.savefig(os.path.join("multi_ex", "vid_frames_{}.pdf".format(vidx)))
    # plt.show()
    plt.close(f)

    # Plot the summary
    f = plt.figure()
    plt.imshow(video[-1])
    for idx in range(len(track_h[0])):
        plt.scatter(track_h[:, idx], track_w[:, idx], label=idx)
    plt.axis("off")
    plt.title("Video {}, Correct={}, Label={}".format(vidx, data["correct"], vidmat["label"]))
    plt.savefig(os.path.join("multi_ex", "vid_tracks_{}.pdf".format(vidx)))

    # plt.show()
    plt.close(f)

