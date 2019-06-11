from PyQt5.QtCore import pyqtSignal

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QFrame, QVBoxLayout, QLabel, QTableWidget

class SettingsWidget(QFrame):
    """
    class documentation:

    variable:

    methods:
        __init__(self, parent=None)
        __str__(self)
        __repr__(self)
        initUI(self)

    """
    done = pyqtSignal()

    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        self.initUI()

    def __str__(self):
        return "SettingsWidget()"

    def __repr__(self):
        return "SettingsWidget()"

    def initUI(self):

        self.setStyleSheet("""
                background: qlineargradient(x1: 0, y1: 0, x2: 3, y2: 2,
                                      stop: 0 #000044, stop: 1 #111166);
                """)

        lbl = QLabel('Settings', self)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("""
                    font: bold 45pt;
                    color: #ffcc44;
                    """)

        tbl = QTableWidget(self)
        tbl.setStyleSheet("""
                background: white;
                """)

        btn = QPushButton('Done',self)
        btn.setStyleSheet("""
                    font: bold 32pt;
                    color: #ffcc44;
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #5577ff, stop: 1 #334499);
                    """)


        lyt = QVBoxLayout()
        lyt.addWidget(lbl)
        lyt.addWidget(tbl)
        lyt.addWidget(btn)
        self.setLayout(lyt)

        btn.clicked.connect(self.on_btn_clicked)

        self.show()

    def on_btn_clicked(self):
        self.done.emit()

