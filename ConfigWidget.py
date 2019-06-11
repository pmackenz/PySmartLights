from PyQt5.QtCore import pyqtSignal

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFrame, QGridLayout, QPushButton, QSizePolicy, QToolButton
from PyQt5.QtGui import QIcon

class ConfigWidget(QFrame):
    """
    class documentation:

    variable:
        self.groups = (g1,g2,g3,g4,g5,g6,g7,g8)  # pointer to group button
        self.active = [False,False,False,False,False,False,False,False]          # active groups

    methods:
        __init__(self, parent=None)
        __str__(self)
        __repr__(self)
        initUI(self)

    """
    done = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(ConfigWidget, self).__init__(parent)
        self.initUI()
        self.active = [False,False,False,False,False,False,False,False]  # active groups

    def __str__(self):
        return "ConfigWidget()"

    def __repr__(self):
        return "ConfigWidget()"

    def initUI(self):

        self.setStyleSheet("""
                background: qlineargradient(x1: 0, y1: 0, x2: 3, y2: 2,
                                      stop: 0 #000044, stop: 1 #111166);
                """)

        group1 = QToolButton(self)
        group1.setIcon(QIcon('Group1-off.png'))
        group1.setIconSize(QSize(161,111))
        group1.setStyleSheet("""
                border: none;
                padding-left: 0px;
                padding-right: 0px;
                padding-top: 0px;
                padding-bottom: 0px;
                """)
        group1.setMaximumSize(161,111)

        group2 = QToolButton(self)
        group2.setIcon(QIcon('Group1-off.png'))
        group2.setIconSize(QSize(161,111))
        group2.setStyleSheet("""
                border: none;
                padding-left: 0px;
                padding-right: 0px;
                padding-top: 0px;
                padding-bottom: 0px;
                """)
        group2.setMaximumSize(161,111)

        group3 = QToolButton(self)
        group3.setIcon(QIcon('Group3-off.png'))
        group3.setIconSize(QSize(161,211))
        group3.setStyleSheet("""
                 border: none;
                 padding-left: 0px;
                 padding-right: 0px;
                 padding-top: 0px;
                 padding-bottom: 0px;
                """);
        group3.setMaximumSize(161,211)

        group4 = QToolButton(self)
        group4.setIcon(QIcon('Group3-off.png'))
        group4.setIconSize(QSize(161,211))
        group4.setStyleSheet("""
                border: none;
                padding-left: 0px;
                padding-right: 0px;
                padding-top: 0px;
                padding-bottom: 0px;
                """)
        group4.setMaximumSize(161,211)

        group5 = QToolButton(self)
        group5.setIcon(QIcon('Group5-off.png'))
        group5.setIconSize(QSize(461,111))
        group5.setContentsMargins(0,0,0,0)
        group5.setStyleSheet("""
                border: none;
                padding-left: 0px;
                padding-right: 0px;
                padding-top: 0px;
                padding-bottom: 0px;
                """)
        group5.setMaximumSize(461,111)

        group6 = QToolButton(self)
        group6.setIcon(QIcon('Group6-off.png'))
        group6.setIconSize(QSize(311,111))
        group6.setStyleSheet("""
                border: none;
                padding-left: 0px;
                padding-right: 0px;
                padding-top: 0px;
                padding-bottom: 0px;
                """)
        group6.setMaximumSize(311,111)

        group7 = QToolButton(self)
        group7.setIcon(QIcon('Group6-off.png'))
        group7.setIconSize(QSize(311,111))
        group7.setStyleSheet("""
                border: none;
                padding-left: 0px;
                padding-right: 0px;
                padding-top: 0px;
                padding-bottom: 0px;
                """)
        group7.setMaximumSize(311,111)

        group8 = QToolButton(self)
        group8.setIcon(QIcon('Group6-off.png'))
        group8.setIconSize(QSize(311,111))
        group8.setStyleSheet("""
                border: none;
                padding-left: 0px;
                padding-right: 0px;
                padding-top: 0px;
                padding-bottom: 0px;
                """)
        group8.setMaximumSize(311,111)

        # control buttons
        btnOK = QPushButton('OK',self)
        btnOK.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnOK.setStyleSheet("""
                    font: bold 45pt;
                    color: #0000aa;
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #5577ff, stop: 1 #334499);
                    """)

        btnCancel = QPushButton('X',self)
        btnCancel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnCancel.setStyleSheet("""
                    font: bold 45pt;
                    color: #aa0000;
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #5577ff, stop: 1 #334499);
                    """)


        lyt = QGridLayout()
        lyt.setContentsMargins(0,0,0,0)
        lyt.setSpacing(-1)

        lyt.addWidget(group1, 0,0,1,1)
        lyt.addWidget(group2, 0,3,1,1)
        lyt.addWidget(group3, 1,0,2,1)
        lyt.addWidget(group4, 1,3,2,1)
        lyt.addWidget(group5, 3,1,1,3)
        lyt.addWidget(group6, 0,1,1,2)
        lyt.addWidget(group7, 1,1,1,2)
        lyt.addWidget(group8, 2,1,1,2)

        lyt.addWidget(btnCancel, 0,4,2,1)
        lyt.addWidget(btnOK,     2,4,2,1)

        lyt.setColumnStretch(0, 0)
        lyt.setColumnStretch(1, 0)
        lyt.setColumnStretch(2, 0)
        lyt.setColumnStretch(3, 0)
        lyt.setColumnStretch(4, 1)

        lyt.setColumnMinimumWidth(4,100)

        lyt.setRowStretch(0, 1)
        lyt.setRowStretch(1, 1)
        lyt.setRowStretch(2, 1)
        lyt.setRowStretch(3, 1)

        self.setLayout(lyt)

        group1.clicked.connect(self.selectG1)
        group2.clicked.connect(self.selectG2)
        group3.clicked.connect(self.selectG3)
        group4.clicked.connect(self.selectG4)
        group5.clicked.connect(self.selectG5)
        group6.clicked.connect(self.selectG6)
        group7.clicked.connect(self.selectG7)
        group8.clicked.connect(self.selectG8)

        btnOK.clicked.connect(self.confirmation)
        btnCancel.clicked.connect(self.cancel)

        self.groups = (group1, group2, group3, group4, group5, group6, group7, group8)
        self.active = [False, False, False, False, False, False, False, False]  # active groups

        self.show()

    def initSettings(self, settings):
        self.active = settings

        if (self.active[0]):
            self.groups[0].setIcon(QIcon('Group1-on.png'))
        else:
            self.groups[0].setIcon(QIcon('Group1-off.png'))

        if (self.active[1]):
            self.groups[1].setIcon(QIcon('Group1-on.png'))
        else:
            self.groups[1].setIcon(QIcon('Group1-off.png'))

        if (self.active[2]):
            self.groups[2].setIcon(QIcon('Group3-on.png'))
        else:
            self.groups[2].setIcon(QIcon('Group3-off.png'))

        if (self.active[3]):
            self.groups[3].setIcon(QIcon('Group3-on.png'))
        else:
            self.groups[3].setIcon(QIcon('Group3-off.png'))

        if (self.active[4]):
            self.groups[4].setIcon(QIcon('Group5-on.png'))
        else:
            self.groups[4].setIcon(QIcon('Group5-off.png'))

        if (self.active[5]):
            self.groups[5].setIcon(QIcon('Group6-on.png'))
        else:
            self.groups[5].setIcon(QIcon('Group6-off.png'))

        if (self.active[6]):
            self.groups[6].setIcon(QIcon('Group6-on.png'))
        else:
            self.groups[6].setIcon(QIcon('Group6-off.png'))

        if (self.active[7]):
            self.groups[7].setIcon(QIcon('Group6-on.png'))
        else:
            self.groups[7].setIcon(QIcon('Group6-off.png'))

    def selectG1(self):
        #print('*** Group 1 selected ***')
        self.toggleGroup(1)

    def selectG2(self):
        #print('*** Group 2 selected ***')
        self.toggleGroup(2)

    def selectG3(self):
        #print('*** Group 3 selected ***')
        self.toggleGroup(3)

    def selectG4(self):
        #print('*** Group 4 selected ***')
        self.toggleGroup(4)

    def selectG5(self):
        #print('*** Group 5 selected ***')
        self.toggleGroup(5)

    def selectG6(self):
        #print('*** Group 6 selected ***')
        self.toggleGroup(6)

    def selectG7(self):
        #print('*** Group 7 selected ***')
        self.toggleGroup(7)

    def selectG8(self):
        #print('*** Group 8 selected ***')
        self.toggleGroup(8)

    def toggleGroup(self, idx):
        btn = self.groups[idx-1]

        if (self.active[idx-1]):
            if (idx == 1):
                btn.setIcon(QIcon('Group1-off.png'))
            elif (idx == 2):
                btn.setIcon(QIcon('Group1-off.png'))
            elif (idx == 3):
                btn.setIcon(QIcon('Group3-off.png'))
            elif (idx == 4):
                btn.setIcon(QIcon('Group3-off.png'))
            elif (idx == 5):
                btn.setIcon(QIcon('Group5-off.png'))
            elif (idx == 6):
                btn.setIcon(QIcon('Group6-off.png'))
            elif (idx == 7):
                btn.setIcon(QIcon('Group6-off.png'))
            elif (idx == 8):
                btn.setIcon(QIcon('Group6-off.png'))
        else:
            if (idx == 1):
                btn.setIcon(QIcon('Group1-on.png'))
            elif (idx == 2):
                btn.setIcon(QIcon('Group1-on.png'))
            elif (idx == 3):
                btn.setIcon(QIcon('Group3-on.png'))
            elif (idx == 4):
                btn.setIcon(QIcon('Group3-on.png'))
            elif (idx == 5):
                btn.setIcon(QIcon('Group5-on.png'))
            elif (idx == 6):
                btn.setIcon(QIcon('Group6-on.png'))
            elif (idx == 7):
                btn.setIcon(QIcon('Group6-on.png'))
            elif (idx == 8):
                btn.setIcon(QIcon('Group6-on.png'))

        self.active[idx-1] = not self.active[idx-1]

    def confirmation(self):
        self.done.emit(True)

    def cancel(self):
        self.done.emit(False)
