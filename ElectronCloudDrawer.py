# -*- coding: utf-8 -*-
import sys
import os
try:
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
except:
    os.system('pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple')
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
try:
    import numpy as np
except:
    os.system('pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple')
    import numpy as np
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    os.system('pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple')
    from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D


def r(x, y, z):
    return np.sqrt(x**2+y**2+z**2)


def s(x, y, z):
    return 1


def pz(x, y, z):
    return z / r(x, y, z)


def px(x, y, z):
    return x / r(x, y, z)


def py(x, y, z):
    return y / r(x, y, z)


def dz2(x, y, z):
    return (2*z**2-x**2-y**2)/r(x, y, z)**2


def dxz(x, y, z):
    return x*z/r(x, y, z)**2


def dyz(x, y, z):
    return y*z/r(x, y, z)**2


def dx2y2(x, y, z):
    return (x**2-y**2)/r(x, y, z)**2


def dxy(x, y, z):
    return x*y/r(x, y, z)**2


def fz3(x, y, z):
    return z*(5*z**2-3*r(x, y, z)**2)/r(x, y, z)**3


def fxz2(x, y, z):
    return x*(5*z**2-r(x, y, z)**2)/r(x, y, z)**3


def fyz2(x, y, z):
    return y*(5*z**2-r(x, y, z)**2)/r(x, y, z)**3


def fy3x2y2(x, y, z):
    return y*(3*x**2-y**2)/r(x, y, z)**3


def fxx23y2(x, y, z):
    return x*(x**2-3*y**2)/r(x, y, z)**3


def fxyz(x, y, z):
    return x*y*z/r(x, y, z)**3


def fzx2y2(x, y, z):
    return z*(x**2-y**2)/r(x, y, z)**3


def gz4(x, y, z):
    return (35*z**4-30*z**2*r(x, y, z)**2+3*r(x, y, z)**4)/r(x, y, z)**4


def gz3x(x, y, z):
    return x*z*(4*z**2-3*x**2-3*y**2)/r(x, y, z)**4


def gz3y(x, y, z):
    return x*z*(4*z**2-3*x**2-3*y**2)/r(x, y, z)**4


def gz2xy(x, y, z):
    return x*y*(6*z**2-x**2-y**2)/r(x, y, z)**4


def gz2x2y2(x, y, z):
    return (x**2-y**2)*(6*z**2-x**2-y**2)/r(x, y, z)**4


def gzx3(x, y, z):
    return x*z*(x**2-3*y**2)/r(x, y, z)**4


def gzy3(x, y, z):
    return y*z*(3*x**2-y**2)/r(x, y, z)**4


def gxyx2y2(x, y, z):
    return x*y*(x**2-y**2)/r(x, y, z)**4


def gx4y4(x, y, z):
    return (x**4+y**4-6*x**2*y**2)/r(x, y, z)**2


def R1s(x, y, z):
    return np.exp(-r(x, y, z))


def R2s(x, y, z):
    return (2-r(x, y, z))*np.exp(-r(x, y, z)/2)


def R2p(x, y, z):
    return r(x, y, z)*np.exp(-r(x, y, z)/2)


def R3s(x, y, z):
    return (6-4*r(x, y, z)+4/9*r(x, y, z)**2)*np.exp(-r(x, y, z)/3)


def R3p(x, y ,z):
    return 2/3*r(x, y, z)*(4-2/3*r(x, y, z))*np.exp(-r(x, y, z)/3)


def R3d(x, y, z):
    return 4/9*r(x, y, z)**2*np.exp(-r(x, y, z)/3)


def R4s(x, y, z):
    return (24-18*r(x, y, z)+3*r(x, y, z)**2-r(x, y, z)**3/8)*np.exp(-r(x, y, z)/4)


def R4p(x, y, z):
    return r(x, y, z)/2*(20-5*r(x, y, z)+r(x, y, z)**2/4)*np.exp(-r(x, y, z)/4)


def R4d(x, y, z):
    return (6-r(x, y, z)/2)*r(x, y, z)**2/4*np.exp(-r(x, y, z)/4)


def R4f(x, y, z):
    return r(x, y, z)**3/8*np.exp(-r(x, y, z)/4)


def R5s(x, y, z):
    return (120-96*r(x, y, z)+19.2*r(x, y, z)**2-1.28*r(x, y, z)**3+0.0256*r(x, y, z)**4)*np.exp(-r(x, y, z)/5)


def R5p(x, y, z):
    return 2/5*r(x, y, z)*(120-36*r(x, y, z)+2.88*r(x, y, z)**2-0.064*r(x, y, z)**3)*np.exp(-r(x, y, z)/5)


def R5d(x, y, z):
    return 0.16*r(x, y, z)*(42-5.6*r(x, y, z)+0.16*r(x, y, z)**2)*np.exp(-r(x, y, z)/5)


def R5f(x, y, z):
    return 0.064*r(x, y, z)**3*(8-0.4*r(x, y, z))*np.exp(-r(x, y, z)/5)


def R5g(x, y, z):
    return 0.0256*r(x, y, z)**4*np.exp(-r(x, y, z)/5)


def chooser(n=1, l=0, m=0, x=0, y=0, z=0):
    if n == 1:
        if l == 0:
            return R1s(x, y, z)*s(x, y, z), '1s'
    elif n == 2:
        if l == 0:
            return R2s(x, y, z)*s(x, y, z), '2s'
        else:
            if m == 0:
                return R2p(x, y, z)*pz(x, y, z), '$2p_z$'
            elif m == 1:
                return R2p(x, y, z)*px(x, y, z), '$2p_x$'
            else:
                return R2p(x, y, z)*py(x, y, z), '$2p_y$'
    elif n == 3:
        if l == 0:
            return R3s(x, y, z)*s(x, y, z), '3s'
        elif l == 1:
            if m == 0:
                return R3p(x, y, z)*pz(x, y, z), '$3p_z$'
            elif m == 1:
                return R3p(x, y, z)*px(x, y, z), '$3p_x$'
            else:
                return R3p(x, y, z)*py(x, y, z), '$3p_y$'
        elif l == 2:
            if m == 0:
                return R3d(x, y, z)*dz2(x, y, z), '$3d_{z^2}$'
            elif m == 1:
                return R3d(x, y, z)*dxz(x, y, z), '$3d_{xz}$'
            elif m == -1:
                return R3d(x, y, z)*dyz(x, y, z), '$3d_{yz}$'
            elif m == 2:
                return R3d(x, y, z)*dx2y2(x, y, z), '$3d_{x^2-y^2}$'
            else:
                return R3d(x, y, z)*dxy(x, y, z), '$3d_{xy}$'
    elif n == 4:
        if l == 0:
            return R4s(x, y, z)*s(x, y, z), '4s'
        elif l == 1:
            if m == 0:
                return R4p(x, y, z)*pz(x, y, z), '$4p_z$'
            elif m == 1:
                return R4p(x, y, z)*px(x, y, z), '$4p_x$'
            else:
                return R4p(x, y, z)*py(x, y, z), '$4p_y$'
        elif l == 2:
            if m == 0:
                return R4d(x, y, z)*dz2(x, y, z), '$4d_{z^2}$'
            elif m == 1:
                return R4d(x, y, z)*dxz(x, y, z), '$4d_{xz}$'
            elif m == -1:
                return R4d(x, y, z)*dyz(x, y, z), '$4d_{yz}$'
            elif m == 2:
                return R4d(x, y, z)*dx2y2(x, y, z), '$4d_{x^2-y^2}$'
            else:
                return R4d(x, y, z)*dxy(x, y, z), '$4d_{xy}$'
        elif l == 3:
            if m == 0:
                return R4f(x, y, z)*fz3(x, y, z), '$4f_{z^3}$'
            elif m == 1:
                return R4f(x, y, z)*fxz2(x, y, z), '$4f_{xz^2}$'
            elif m == -1:
                return R4f(x, y, z)*fyz2(x, y, z), '$4f_{yz^2}$'
            elif m == 3:
                return R4f(x, y, z)*fy3x2y2(x, y, z), '$4f_{y(3x^2-y^2)}$'
            elif m == -3:
                return R4f(x, y, z)*fxx23y2(x, y, z), '$4f_{x(x^2-3y^2)}$'
            elif m == 2:
                return R4f(x, y, z)*fxyz(x, y, z), '$4f_{xyz}$'
            else:
                return R4f(x, y, z)*fzx2y2(x, y, z), '$4f_{z(x^2-y^2)}$'
    elif n == 5:
        if l == 0:
            return R5s(x, y, z)*s(x, y, z), '5s'
        elif l == 1:
            if m == 0:
                return R5p(x, y, z)*pz(x, y, z), '$5p_z$'
            elif m == 1:
                return R5p(x, y, z)*px(x, y, z), '$5p_x$'
            else:
                return R5p(x, y, z)*py(x, y, z), '$5p_y$'
        elif l == 2:
            if m == 0:
                return R5d(x, y, z)*dz2(x, y, z), '$5d_{z^2}$'
            elif m == 1:
                return R5d(x, y, z)*dxz(x, y, z), '$5d_{xz}$'
            elif m == -1:
                return R5d(x, y, z)*dyz(x, y, z), '$5d_{yz}$'
            elif m == 2:
                return R5d(x, y, z)*dx2y2(x, y, z), '$5d_{x^2-y^2}$'
            else:
                return R5d(x, y, z)*dxy(x, y, z), '$5d_{xy}$'
        elif l == 3:
            if m == 0:
                return R5f(x, y, z)*fz3(x, y, z), '$5f_{z^3}$'
            elif m == 1:
                return R5f(x, y, z)*fxz2(x, y, z), '$5f_{xz^2}$'
            elif m == -1:
                return R5f(x, y, z)*fyz2(x, y, z), '$5f_{yz^2}$'
            elif m == 3:
                return R5f(x, y, z)*fy3x2y2(x, y, z), '$5f_{y(3x^2-y^2)}$'
            elif m == -3:
                return R5f(x, y, z)*fxx23y2(x, y, z), '$5f_{x(x^2-3y^2)}$'
            elif m == 2:
                return R5f(x, y, z)*fxyz(x, y, z), '$5f_{xyz}$'
            else:
                return R5f(x, y, z)*fzx2y2(x, y, z), '$5f_{z(x^2-y^2)}$'
        elif l == 4:
            if m == 0:
                return R5g(x, y, z)*gz4(x, y, z), '$5f_{z^4}$'
            elif m == 1:
                return R5g(x, y, z)*gz3x(x, y, z), '$5f_{z^3x}$'
            elif m == -1:
                return R5g(x, y, z)*gz3y(x, y, z), '$5f_{z^3y}$'
            elif m == 2:
                return R5g(x, y, z)*gz2xy(x, y, z), '$5f_{z^2xy}$'
            elif m == -2:
                return R5g(x, y, z)*gz2x2y2(x, y, z), '$5f_{z^2(x^2-y^2)}$'
            elif m == 3:
                return R5g(x, y, z)*gzx3(x, y, z), '$5f_{zx^3}$'
            elif m == -3:
                return R5g(x, y, z)*gzy3(x, y, z), '$5f_{zy^3}$'
            elif m == 4:
                return R5g(x, y, z)*gxyx2y2(x, y, z), '$5f_{xy(x^2-y^2)}$'
            else:
                return R5g(x, y, z)*gx4y4(x, y, z), '$5f_{x^4+y^4}$'


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        Form.setMinimumSize(QtCore.QSize(1280, 720))
        Form.setMaximumSize(QtCore.QSize(1280, 720))
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(1030, 90, 180, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(1030, 160, 180, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1030, 50, 180, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1030, 120, 180, 30))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1030, 570, 180, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1030, 190, 180, 30))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(1030, 230, 180, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(1030, 270, 40, 30))
        self.label_4.setObjectName("label_4")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(1030, 310, 180, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(1070, 270, 140, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(1030, 380, 180, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(1070, 340, 140, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1030, 340, 40, 30))
        self.label_5.setObjectName("label_5")
        self.horizontalSlider_3 = QtWidgets.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(1030, 450, 180, 20))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(1070, 410, 140, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(1030, 410, 40, 30))
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(960, 10, 3, 700))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 941, 701))
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Electron Cloud Drawer -TMJ"))
        self.label.setText(_translate("Form", "主量子数(n):"))
        self.label_2.setText(_translate("Form", "角量子数(l):"))
        self.pushButton.setText(_translate("Form", "计算"))
        self.label_3.setText(_translate("Form", "磁量子数(m):"))
        self.label_4.setText(_translate("Form", "X:"))
        self.label_5.setText(_translate("Form", "Y:"))
        self.label_6.setText(_translate("Form", "Z:"))


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = Axes3D(self.fig)
        # self.axes.hold(False)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def start_plot(self, n, l, m, X, Y, Z):
        self.fig.suptitle('Electron cloud Distribution of {}'.format(chooser(n, l, m)[1]))
        Axes3D.mouse_init(self.axes)
        x = np.linspace(-X, X, 100)
        y = np.linspace(-Y, Y, 100)
        z = np.linspace(-Z, Z, 100)
        ans_x, ans_y, ans_z, ans_x2, ans_y2, ans_z2 = [], [], [], [], [], []
        for i in x:
            for j in y:
                for k in z:
                    if 0.09 < chooser(n, l, m, i, j, k)[0] < 0.11:
                        ans_x.append(i)
                        ans_y.append(j)
                        ans_z.append(k)
                    if -0.11 < chooser(n, l, m, i, j, k)[0] < -0.09:
                        ans_x2.append(i)
                        ans_y2.append(j)
                        ans_z2.append(k)
        self.axes.scatter(ans_x, ans_y, ans_z, c='b', alpha=0.3)
        self.axes.scatter(ans_x2, ans_y2, ans_z2, c='r', alpha=0.3)
        # self.axes.legend(loc=0)
        self.axes.grid(True)
        self.draw()


class MatPlotLibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatPlotLibWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.mpl = PlotCanvas(self, width=8, height=6)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.plot_update)
        self.comboBox.clear()
        for i in range(1, 6):
            self.comboBox.addItem(str(i))
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox_2.addItem('0')
        self.comboBox_3.addItem('0')
        self.comboBox.activated.connect(self.n_changed)
        self.comboBox_2.activated.connect(self.l_changed)
        self.plot = MatPlotLibWidget(self.widget)
        intValidator = QtGui.QIntValidator()
        intValidator.setRange(10, 150)
        self.lineEdit.setText('10')
        self.lineEdit_2.setText('10')
        self.lineEdit_3.setText('10')
        self.lineEdit.setValidator(intValidator)
        self.lineEdit_2.setValidator(intValidator)
        self.lineEdit_3.setValidator(intValidator)
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(150)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.valueChanged.connect(self.x_changed)
        self.horizontalSlider_2.setMinimum(10)
        self.horizontalSlider_2.setMaximum(150)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.valueChanged.connect(self.y_changed)
        self.horizontalSlider_3.setMinimum(10)
        self.horizontalSlider_3.setMaximum(150)
        self.horizontalSlider_3.setSingleStep(1)
        self.horizontalSlider_3.valueChanged.connect(self.z_changed)
        # self.plot.mpl.start_plot(1, 0, 0, 10, 10, 10)
        self.plot.move(50, 0)
        self.plot.show()
        self.show()

    def plot_update(self):
        tip = QMessageBox.about(self, '重要提示', '计算大约需要一到两分钟，期间请不要关闭或对程序做其他操作')
        print(tip)
        self.plot.mpl.axes.cla()
        self.plot.mpl.start_plot(int(self.comboBox.currentText()),
                                 int(self.comboBox_2.currentText()),
                                 int(self.comboBox_3.currentText()),
                                 int(self.lineEdit.text()),
                                 int(self.lineEdit_2.text()),
                                 int(self.lineEdit_3.text()),)
        self.plot.show()
        self.show()

    def n_changed(self):
        self.comboBox_2.clear()
        for i in range(int(self.comboBox.currentText())):
            self.comboBox_2.addItem(str(i))

    def l_changed(self):
        self.comboBox_3.clear()
        for i in range(-int(self.comboBox_2.currentText()), int(self.comboBox_2.currentText())+1):
            self.comboBox_3.addItem(str(i))

    def x_changed(self):
        self.lineEdit.setText(str(self.horizontalSlider.value()))

    def y_changed(self):
        self.lineEdit_2.setText(str(self.horizontalSlider_2.value()))

    def z_changed(self):
        self.lineEdit_3.setText(str(self.horizontalSlider_3.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
