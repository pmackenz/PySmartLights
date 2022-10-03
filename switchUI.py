
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from ControlWidget import *
from ConfigWidget import *
from SettingsWidget import *

import json

class switchUI(QWidget):
    """
    class documentation

    variables:

    methods:

    """

    CONTROL = 0
    CONFIGURATION = 1
    SETTINGS = 2

    def __init__(self, parent=None):
        super(switchUI, self).__init__(parent)
        self.setGeometry(0,0,600,400)
        self.initUI()
        self.initConfig()

    def __str__(self):
        return "switchUI(): smart lights zone control switch"

    def __repr__(self):
        return "switchUI()"

    def initUI(self):
        # this will hide the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.stack = QStackedWidget(self)

        self.control  = ControlWidget(self)
        self.config   = ConfigWidget(self)
        self.settings = SettingsWidget(self)

        self.stack.addWidget(self.control)
        self.stack.addWidget(self.config)
        self.stack.addWidget(self.settings)

        lyt = QVBoxLayout(self)
        lyt.addWidget(self.stack)
        lyt.setContentsMargins(0,0,0,0)

        self.stack.setCurrentIndex(self.CONTROL)  # control screen

        self.control.configure.connect(self.configure)
        self.config.done.connect(self.doneConfiguring)
        self.settings.done.connect(self.doneSettings)

        self.show()

    def initConfig(self):
        # we should check if a config file exists

        # read if exists

        # create defaults if no file exists
        self.settings = {
                'All':[True,True,True,True,True,True,True,True],
                'Min':[False,False,False,False,True,False,False,False],
                'TV':[True,False,True,False,False,False,False,False],
                'Mood':[True,True,True,True,False,True,False,False]
                         }

        self.activeKey = 'All'

    def configure(self, key):

        print('** configure "{}"'.format(key))

        if (key.lower() == 'settings'):
            self.stack.setCurrentIndex(self.SETTINGS)
        else:
            self.activeKey = key
            self.activeSetting = self.settings[key][:]

            self.stack.setCurrentIndex(self.CONFIGURATION)
            self.stack.currentWidget().initSettings(self.activeSetting)

    def doneConfiguring(self, state):

        if (state):
            self.settings[self.activeKey] = self.activeSetting[:]

        self.stack.setCurrentIndex(self.CONTROL)
        self.stack.currentWidget().setActiveButton(self.activeKey)

        print('*** status {} : {} ***'.format('changed' if state else 'unchanged', self.settings[self.activeKey]))

    def doneSettings(self):

        self.stack.setCurrentIndex(self.CONTROL)
