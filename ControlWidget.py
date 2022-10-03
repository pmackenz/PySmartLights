
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QGridLayout, QPushButton, QSlider, QSizePolicy

import time as tt

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RELAIS_1_GPIO = 23
RELAIS_2_GPIO = 24
RELAIS_3_GPIO = 10
RELAIS_4_GPIO = 25
RELAIS_5_GPIO = 9
RELAIS_6_GPIO = 8
RELAIS_7_GPIO = 11
RELAIS_8_GPIO = 7


class ControlWidget(QFrame):
    """
    class documentation:

    variable:

    methods:
        __init__(self, parent=None)
        __str__(self)
        __repr__(self)
        initUI(self)

    """
    configure = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ControlWidget, self).__init__(parent)
        self.relays = (
            RELAIS_1_GPIO, RELAIS_2_GPIO, RELAIS_3_GPIO, RELAIS_4_GPIO,
            RELAIS_5_GPIO, RELAIS_6_GPIO, RELAIS_7_GPIO, RELAIS_8_GPIO
        )
        self.initUI()
        self.setActiveButton('All')

    def __str__(self):
        return "ControlWidget()"

    def __repr__(self):
        return "ControlWidget()"

    def initUI(self):

        self.setStyleSheet("""
                    background: #334499;
                """)

        self.setStyleSheet("""
                    background: #000000;
                """)

        btnAll  = QPushButton('All ON', self)
        btnTV   = QPushButton('TV', self)
        btnMood = QPushButton('Mood\nlight', self)
        btnMin  = QPushButton('Walkway', self)

        slider  = QSlider(0, self)  # figure out orientation switch
        slider.setFixedWidth(80)
        slider.setMaximum(255)
        slider.setMinimum(32)

        self.buttons = {'All': btnAll,
                        'Min': btnMin,
                        'Mood': btnMood,
                        'TV': btnTV }

        self.states = {'All': False,
                        'Min': False,
                        'Mood': False,
                        'TV': False }

        for key in self.buttons.keys():
            self.setActive(key, False)

        btnAll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMin.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnMood.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnTV.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        slider.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        lyt = QGridLayout(self)
        lyt.addWidget(btnAll,  0, 0)
        lyt.addWidget(btnMin,  0, 1)
        lyt.addWidget(btnMood, 1, 0)
        lyt.addWidget(btnTV,   1, 1)
        lyt.addWidget(slider, 0, 2, 2, 1)
        lyt.setContentsMargins(6,6,6,6)

        btnAll.pressed.connect(self.pressedAll)
        btnMin.pressed.connect(self.pressedMin)
        btnMood.pressed.connect(self.pressedMood)
        btnTV.pressed.connect(self.pressedTV)

        btnAll.released.connect(self.releasedAll)
        btnMin.released.connect(self.releasedMin)
        btnMood.released.connect(self.releasedMood)
        btnTV.released.connect(self.releasedTV)

        slider.valueChanged.connect(self.dimmer)
        slider.sliderPressed.connect(self.highlightSlider)
        slider.sliderReleased.connect(self.dimSlider)

        slider.sliderReleased.emit()

        self.show()

    def highlightSlider(self):
        slider = self.sender()
        slider.setStyleSheet("""
                        QSlider::groove:vertical {
                            border: 1px solid;
                            border: None;
                            width: 80px;
                            margin: 0px;
                            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #802211, stop: 1 #101106);
                            }
                        QSlider::handle:vertical {
                            background-color: #ffcc44;
                            border: 1px solid;
                            height: 50;
                            width: 50px;
                            margin: -15px -15px;
                            margin: 0px 0px;
                            border-radius: 10px;
                            }
                        """)

    def dimSlider(self):
        slider = self.sender()
        slider.setStyleSheet("""
                        QSlider::groove:vertical {
                            border: 1px solid;
                            border: None;
                            width: 80px;
                            margin: 0px;
                            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #802211, stop: 1 #101106);
                            }
                        QSlider::handle:vertical {
                            background-color: #886622;
                            border: 1px solid;
                            height: 20px;
                            width: 50px;
                            margin: -15px -15px;
                            margin: 0px 0px;
                            border-radius: 10px;
                            }
                        """)

    def setActive(self, idx, state=True):
        # control appearance of the active button
        if type(idx) is str:
            if state:
                # self.buttons[idx].setStyleSheet("""
                #     font: bold 45pt;
                #     color: #886622;
                #     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                #                       stop: 0 #ffcc44, stop: 1 #ddaa33);
                #     """)
                self.buttons[idx].setStyleSheet("""
                    font: bold 45pt; 
                    color: #ffcc44;
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #442211, stop: 1 #331106);
                    border: 1px solid;
                    border-color: #ffcc44;
                    margin: 0px 0px;
                    """)
                self.states[idx] = True
            else:
                # self.buttons[idx].setStyleSheet("""
                #     font: bold 45pt;
                #     color: #ffcc44;
                #     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                #                       stop: 0 #aaaaaa, stop: 1 #cccccc);
                #     """)
                self.buttons[idx].setStyleSheet("""
                    font: bold 45pt;
                    color: #886622;
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #111111, stop: 1 #000000);
                    border: 1px solid;
                    border-color: #886622;
                    margin: 3px 3px;
                    """)
                self.states[idx] = False

        # set relays to represent active state


    def setActiveButton(self, idx):
        if type(idx) is str:
            for key in self.buttons.keys():
                self.setActive(key, False)
            self.setActive(idx, True)

    def switched(self, idx):
        if type(idx) is str:
            btn = self.buttons[idx]
            if self.states[idx]:
                self.setActive(idx, False)
            else:
                self.setActiveButton(idx)

    def pressedAll(self):
        self.timestamp = tt.time()

    def releasedAll(self):
        dt = tt.time() - self.timestamp
        # print('time: {} with dt = {}'.format(self.timestamp, dt))
        if (dt<1.000):
            self.switched('All')
        elif (dt>3.00):
            self.configure.emit('settings')
        else:
            self.configure.emit('All')

    def pressedMin(self):
        self.timestamp = tt.time()

    def releasedMin(self):
        dt = tt.time() - self.timestamp
        # print('time: {} with dt = {}'.format(self.timestamp, dt))
        if (dt<1.000):
            self.switched('Min')
        else:
            self.configure.emit('Min')

    def pressedTV(self):
        self.timestamp = tt.time()

    def releasedTV(self):
        dt = tt.time() - self.timestamp
        # print('time: {} with dt = {}'.format(self.timestamp, dt))
        if (dt<1.000):
            self.switched('TV')
        else:
            self.configure.emit('TV')

    def pressedMood(self):
        self.timestamp = tt.time()

    def releasedMood(self):
        dt = tt.time() - self.timestamp
        # print('time: {} with dt = {}'.format(self.timestamp, dt))
        if (dt<1.000):
            self.switched('Mood')
        else:
            self.configure.emit('Mood')

    def dimmer(self, val):
        print('+++ dimmer: {}'.format(val))

    def setLights(self, states, level):
        # set dimmer to level
        pass

        # activate relais
        for (state, relais_GPIO) in zip(states, self.relays):
            GPIO.setup(relais_GPIO, GPIO.OUT)  # GPIO Assign mode
            if state:
                GPIO.output(relais_GPIO, GPIO.LOW)  # out
            else:
                GPIO.output(relais_GPIO, GPIO.HIGH)  # on
