#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Smart light zoned control

author: Peter Mackenzie-Helnwein
contact: mackheln@gmail.com
created: June 9, 2019
last edited: June 2019
"""

import sys
from PyQt5.QtWidgets import QApplication
from switchUI import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = switchUI()
    #w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('LightSwitch')

    sys.exit(app.exec_())