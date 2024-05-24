#Python Qt 5 GUI for Windston
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QColor, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QLabel, QFileDialog, QLineEdit, QSpacerItem, QButtonGroup, QComboBox, QTabWidget
from colour import Color
import numpy as np
import pyqtgraph as pg
import vars
import signal
import sched
from datetime import date
import threading

G = 6.67430e-11


class SolarSystemGui(QWidget):
    def __init__(self):
        pass