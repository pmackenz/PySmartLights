from PyQt5.QtCore import pyqtSignal

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QPushButton, QFrame, QGridLayout, QLabel, QTableWidget, QSizePolicy

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

        quit_btn = QPushButton('Quit Controller',self)
        quit_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        quit_btn.setStyleSheet("""
                    font: bold 24pt;
                    color: #ffcc44;
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #ff7755, stop: 1 #994433);
                    """)

        ok_btn = QPushButton('Done',self)
        ok_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ok_btn.setStyleSheet("""
                    font: bold 32pt;
                    color: #ffcc44;
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #5577ff, stop: 1 #334499);
                    """)


        lyt = QGridLayout()
        lyt.addWidget(lbl,0,0,1,2)
        lyt.addWidget(tbl,1,0,1,2)
        lyt.addWidget(quit_btn,2,0,1,1)
        lyt.addWidget(ok_btn,2,1,1,1)

        lyt.setRowStretch(1,2)
        self.setLayout(lyt)

        ok_btn.clicked.connect(self.on_btn_clicked)
        quit_btn.clicked.connect(self.terminate)

        self.show()

    def terminate(self):
        QCoreApplication.quit()

    def on_btn_clicked(self):
        self.done.emit()

