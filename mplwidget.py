from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class MplWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        super().__init__(self.fig)
        self.setParent(parent)

        self.ax1 = self.fig.add_subplot(2, 1, 1)
        self.ax2 = self.fig.add_subplot(2, 1, 2)

    def plot(self, signal, fs, NFFT, noverlap, lead):
        t = np.arange(len(signal[lead])) / fs
        self.ax1.clear()
        self.ax1.plot(t, signal[lead])
        self.ax1.set_xlim(0, t[-1])
        self.ax2.clear()
        self.ax2.specgram(signal[lead], Fs=fs, NFFT=NFFT, noverlap=noverlap, cmap='turbo')
        self.draw()
