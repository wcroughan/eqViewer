import matplotlib.pyplot as plt
import numpy as np


def main():
    fname = "/home/wcroughan/Unity/Projects/Sliders/Assets/eqvals.txt"
    vals = np.loadtxt(fname, delimiter=",").T
    s = np.sum(vals, axis=1)
    # vals = np.divide(vals, np.reshape(s, (-1, 1)))
    # plt.imshow(vals)
    # plt.plot(np.log(s))
    d = np.ones_like(s)
    for i in range(len(d)):
        d[i] *= pow(10, float(i) / (float(len(d)) * float(1)))
    plt.plot(np.divide(s, d))
    plt.show()


if __name__ == "__main__":
    main()
