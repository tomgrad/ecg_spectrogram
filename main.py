import sys
import wfdb
import neurokit2 as nk
import numpy as np
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clean = False
        self.lead = 0
        self.tFFT = 0.25
        self.overlap = 0.9
        self.length_limit = 10  # seconds

        self.tFFTSpinBox.setValue(self.tFFT)
        self.overlapSpinBox.setValue(self.overlap)

        self.loadButton.clicked.connect(self.load_file)
        self.cleanCheckBox.stateChanged.connect(self.toggle_clean)
        self.tFFTSpinBox.valueChanged.connect(self.update_tFFT)
        self.overlapSpinBox.valueChanged.connect(self.update_overlap)
        self.leadComboBox.currentIndexChanged.connect(self.update_lead)

    def load_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(
            self, "Open File", "", "ECG WFDB (*.hea)")
        if file_path:
            self.record = wfdb.rdrecord(
                file_path[:-4])  # Remove .hea extension
            self.statusbar.showMessage(
                f"Loaded file: {Path(file_path).name} Sampling Rate: {self.record.fs} Hz")

            self.lead = 0

            self.ecg_raw = self.record.p_signal[:
                                                self.length_limit*self.record.fs].T
            clean = [nk.ecg_clean(ecg, sampling_rate=self.record.fs)
                     for ecg in self.ecg_raw]
            self.ecg_clean = np.array(clean)

            self.signal = self.ecg_clean if self.clean else self.ecg_raw

            self.leadComboBox.setEnabled(False)
            self.leadComboBox.clear()
            for i, name in enumerate(self.record.sig_name):
                self.leadComboBox.addItem(f"{i}: {name}")
            self.leadComboBox.setEnabled(True)

            # self.plot()

    def toggle_clean(self, state):
        self.clean = state == 2  # Qt.Checked is 2
        if hasattr(self, 'record'):
            self.signal = self.ecg_clean if self.clean else self.ecg_raw
            self.plot()

    def update_tFFT(self, value):
        self.tFFT = value
        if hasattr(self, 'record'):
            self.plot()

    def update_overlap(self, value):
        self.overlap = value
        if hasattr(self, 'record'):
            self.plot()

    def update_lead(self, index):
        self.lead = index
        if hasattr(self, 'record'):
            self.plot()

    def plot(self):
        if hasattr(self, 'record'):
            self.fig.plot(self.signal, self.record.fs, NFFT=int(self.tFFT * self.record.fs),
                          noverlap=int(self.tFFT * self.record.fs * self.overlap), lead=self.lead)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
