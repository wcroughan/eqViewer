import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read as wavread
import os


def plotEqText():
    # fname = "/home/wcroughan/Unity/Projects/Sliders/Assets/eqvals.txt"
    fname = "/home/wcroughan/Unity/Projects/RayMarching/Assets/eqvals.txt"
    if not os.path.exists(fname):
        fname = "/home/wcroughan/repos/music/Faders/Assets/eqvals.txt"

    vals = np.loadtxt(fname, delimiter=",").T
    s = np.sum(vals, axis=1)
    # vals = np.divide(vals, np.reshape(s, (-1, 1)))
    # plt.imshow(vals)
    plt.plot(np.log(s))
    # e = np.linspace(0, 5, np.size(s))
    # d = np.power(2.5, e)
    # ss = np.multiply(s, d)
    # plt.plot(np.log(ss))
    plt.show()


def plotAudioText():
    fname = "/home/wcroughan/Unity/Projects/RayMarching/Assets/rawAudio.txt"
    if not os.path.exists(fname):
        fname = "/home/wcroughan/repos/music/RayMarching/Assets/rawAudio.txt"

    vals = np.loadtxt(fname, delimiter=",").T
    zt = 0.0001
    mvs = np.max(np.abs(vals), axis=0)
    fracWithNothing = 1 - np.count_nonzero(mvs > zt) / np.size(mvs)
    print(fracWithNothing)
    # plt.imshow(vals)
    # plt.plot(np.max(vals, axis=1))
    # plt.show()


def plotTestWav():
    fname = "/home/wcroughan/tmp.wav"
    fs, wav = wavread(fname)
    plt.plot(wav)
    plt.show()


if __name__ == "__main__":
    plotAudioText()
