import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    fname = "/home/wcroughan/Unity/Projects/Sliders/Assets/eqvals.txt"
    if not os.path.exists(fname):
        fname = "/home/wcroughan/repos/music/Faders/Assets/eqvals.txt"

    vals = np.loadtxt(fname, delimiter=",").T
    s = np.sum(vals, axis=1)
    # vals = np.divide(vals, np.reshape(s, (-1, 1)))
    # plt.imshow(vals)
    # plt.plot(np.log(s))
    e = np.linspace(0, 5, np.size(s))
    d = np.power(2.5, e)
    ss = np.multiply(s, d)
    plt.plot(np.log(ss))
    plt.show()


if __name__ == "__main__":
    main()
