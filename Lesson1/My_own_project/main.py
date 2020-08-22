from sklearn.ensemble import RandomForestRegressor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot as plt

class Ui1_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 501)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.graphicsView = QtWidgets.QLabel(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(410, 40, 341, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setPixmap(QtGui.QPixmap("images/run.png"))
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(410, 330, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(640, 380, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(520, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(410, 440, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 300, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        train_rmse = (sqrt(mean_squared_error(m.predict(train), y_train)))
        validation_rmse = (sqrt(mean_squared_error(m.predict(validation), y_validation)))
        trainR2 = m.score(train, y_train)
        validationR2 = m.score(validation, y_validation)


        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Go back to model training"))
        self.label.setText(_translate("Dialog", "RMSE of train set          : %.5f" % (train_rmse)))
        self.label_2.setText(_translate("Dialog", "RMSE of validation set  : %.5f" % (validation_rmse)))
        self.label_3.setText(_translate("Dialog", "R^2 of train set            : %.5f" % (trainR2)))
        self.label_4.setText(_translate("Dialog", "R^2 of validation set    : %.5f" % (validationR2)))
        self.label_5.setText(_translate("Dialog", "Select one data from test data set"))
        self.label_6.setText(_translate("Dialog", "Index [0,27999] :"))
        self.pushButton_2.setText(_translate("Dialog", "Test"))
        self.label_7.setText(_translate("Dialog", "Estimation of the model [0,9] : - "))

        if oob == True:

            self.label_8.setText(_translate("Dialog", "OOB Score                     : %.5f" % m.oob_score_))

        self.pushButton.clicked.connect(self.css)

        self.test = pd.read_csv("test.csv")

        self.pushButton_2.clicked.connect(self.testa)

    def css(self):

        ui.mainwin.hide()
        Dialog.hide()
        
        Dialog.show()

    def testa(self):

        self.x = None

        try:

            int(self.lineEdit.text())

            self.x = True

        except:

            self.x = False

            self.pushButton_2.setText("Hata !!!")


        if self.x == True:

            if int(self.lineEdit.text()) >= 0 and int(self.lineEdit.text()) <= 27999: 

                plt.figure(figsize=(3,3))
                row_index = int(self.lineEdit.text())
                grid_data = np.array(self.test.iloc[row_index]).reshape(28,28)
                plt.imshow(grid_data, interpolation = 'none', cmap= "gray")
                plt.savefig("images/a.png")

                self.graphicsView.setPixmap(QtGui.QPixmap("images/a.png"))

                self.a = []

                self.a.append(self.test.iloc[row_index])


                self.tah = m.predict(self.a)

                _translate = QtCore.QCoreApplication.translate

                self.label_7.setText(_translate("Dialog", "Estimation of the model [0,9] : {} ".format(round(self.tah[0]))))

                self.pushButton_2.setText("Test")

            else:

                self.pushButton_2.setText("Hata !!!")



class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 501)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 440, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 150, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 50, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 100, 113, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 200, 113, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 250, 113, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 350, 113, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(260, 300, 113, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.graphicsView = QtWidgets.QLabel(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(400, 50, 361, 331))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setPixmap(QtGui.QPixmap("images/demir.png"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Train"))
        self.label.setText(_translate("Dialog", "n_estimators           : "))
        self.lineEdit.setText(_translate("Dialog", "1"))
        self.label_2.setText(_translate("Dialog", "max_depth              : "))
        self.label_3.setText(_translate("Dialog", "bootstrap                : "))
        self.label_4.setText(_translate("Dialog", "oob_score               : "))
        self.label_5.setText(_translate("Dialog", "n_jobs                     : "))
        self.label_6.setText(_translate("Dialog", "min_samples_leaf   :"))
        self.label_7.setText(_translate("Dialog", "max_features          :"))
        self.lineEdit_2.setText(_translate("Dialog", "100"))
        self.lineEdit_3.setText(_translate("Dialog", "None"))
        self.lineEdit_4.setText(_translate("Dialog", "auto"))
        self.lineEdit_5.setText(_translate("Dialog", "True"))
        self.lineEdit_6.setText(_translate("Dialog", "-1"))
        self.lineEdit_7.setText(_translate("Dialog", "False"))

        self.pushButton.clicked.connect(self.clicka)

    def clicka(self):

        self.train = pd.read_csv("train.csv")
        self.y = self.train.label
        self.train.drop(["label"],axis=1,inplace = True)

        self.n_valid = 12000  # same as Kaggle's test set size
        self.n_train = len(self.train)-self.n_valid

        global train, validation, y_train, y_validation

        train, validation = self.split_train_val(self.train, self.n_train)
        y_train, y_validation = self.split_train_val(self.y, self.n_train)

        try:

            self.n_estimators = int(self.lineEdit_2.text())

            if self.lineEdit_3.text() == "None":

                self.max_depth = None

            else:

                self.max_depth = int(self.lineEdit_3.text())


            if type(eval(self.lineEdit.text())) == float:

                self.min_samples_leaf = float(self.lineEdit.text())

            else:

                self.min_samples_leaf = int(self.lineEdit.text())


            if self.lineEdit_4.text() == "auto":

                self.max_features = "auto"

            elif type(eval(self.lineEdit_4.text())) == float:

                self.max_features = float(self.lineEdit_4.text())

            else:

                self.max_features = int(self.lineEdit_4.text())

            if self.lineEdit_5.text() == "False":

                self.bootstrap = bool(0)

            else:

                self.bootstrap = bool(1)


            if self.lineEdit_7.text() == "False":

                self.oob_score = bool(0)

            else:

                self.oob_score = bool(1)

            global oob

            if self.oob_score == True:

                oob = True

            else:

                oob = False

            self.n_jobs = int(self.lineEdit.text())

            global m

            m = RandomForestRegressor(n_estimators=self.n_estimators, max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf, max_features=self.max_features, bootstrap=self.bootstrap, oob_score=self.oob_score, n_jobs=self.n_jobs)
            
            m.fit(self.train, self.y)

            self.pushButton.setText("Train")


        except:

            self.pushButton.setText("Hata !!!")

        if self.pushButton.text() != "Hata !!!":

            self.mainwin=QMainWindow()
            self.ui=Ui1_Dialog()
            self.ui.setupUi(self.mainwin)
            self.mainwin.setWindowTitle("RandomForestRegressor - Test")
            self.mainwin.setFixedSize(802, 501)
            self.mainwin.move(300,100)
            self.mainwin.show()
            Dialog.hide()

    def split_train_val(self, df, n): 
    
        return df[:n].copy(), df[n:].copy()


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("RandomForestRegressor - Train")
    Dialog.setFixedSize(802, 501)
    Dialog.move(300,100)
    Dialog.show()
    Dialog.show()
    sys.exit(app.exec_())
