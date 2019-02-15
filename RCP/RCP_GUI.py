# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from RCP import *
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.store_rounds_nr = 0
        self._rcp = RCP_easy()
        self._rcp_med = RCP_medium()
        self._rcp_hard = RCP_hard()
        self._users = Users()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(552, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(552, 500))
        MainWindow.setMaximumSize(QtCore.QSize(552, 500))
        MainWindow.setDocumentMode(False)
        MainWindow.setWindowIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.rock_img = QtGui.QPixmap(r'F:\RCP\rock.png')
        self.scissors_img = QtGui.QPixmap(r'F:\RCP\scissors.png')
        self.paper_img = QtGui.QPixmap(r'F:\RCP\paper.png')
        self.rock_img = self.rock_img.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        self.scissors_img = self.scissors_img.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        self.paper_img = self.paper_img.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        self.rock_img_small = self.rock_img.scaled(48, 48, QtCore.Qt.KeepAspectRatio)
        self.scissors_img_small = self.scissors_img.scaled(48, 48, QtCore.Qt.KeepAspectRatio)
        self.paper_img_small = self.paper_img.scaled(48, 48, QtCore.Qt.KeepAspectRatio)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 380, 125, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 380, 121, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 380, 121, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 220, 151, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(400, 220, 151, 71))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 150, 161, 71))
        self.label.setStyleSheet("font-size:20px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 220, 181, 71))
        self.label_2.setStyleSheet("font-size:30px")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 110, 151, 71))
        self.label_3.setStyleSheet("font-size:20px")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 270, 71, 21))
        self.label_4.setStyleSheet("font-size:12px")
        self.label_4.setObjectName("label_4")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(270, 270, 64, 23))
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 330, 100, 140))
        self.label_5.setObjectName("label_5") 
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 319, 100, 140))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(455, 320, 100, 140))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 220, 61, 21))
        self.label_8.setStyleSheet("font-size:14px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 220, 61, 21))
        self.label_9.setStyleSheet("font-size:15px; font-style: bold;")
        self.label_9.setObjectName("label_9")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(170, 60, 211, 81))
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 20, 161, 41))
        self.label_10.setStyleSheet("font-size:30px; font-style: italic")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(420, 160, 121, 51))
        self.graphicsView_2.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.scene2 = QtWidgets.QGraphicsScene()
        self.graphicsView_2.setScene(self.scene2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 21))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        self.menuChange_difficulty = QtWidgets.QMenu(self.menuFILE)
        self.menuChange_difficulty.setObjectName("menuChange_difficulty")
        self.menuRounds = QtWidgets.QMenu(self.menuFILE)
        self.menuRounds.setObjectName("menuRounds")
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        self.menuHELP.setObjectName("menuHELP")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart_round = QtWidgets.QAction(MainWindow)
        self.actionRestart_round.setObjectName("actionRestart_round")
        self.actionNew_player = QtWidgets.QAction(MainWindow)
        self.actionNew_player.setObjectName("actionNew_player")
        self.actionLoad_player = QtWidgets.QAction(MainWindow)
        self.actionLoad_player.setObjectName("actionLoad_player")
        self.actionEasy = QtWidgets.QAction(MainWindow)
        self.actionEasy.setObjectName("actionEasy")
        self.actionMedium = QtWidgets.QAction(MainWindow)
        self.actionMedium.setObjectName("actionMedium")
        self.actionHard = QtWidgets.QAction(MainWindow)
        self.actionHard.setObjectName("actionHard")
        self.action15 = QtWidgets.QAction(MainWindow)
        self.action15.setObjectName("action15")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.action7 = QtWidgets.QAction(MainWindow)
        self.action7.setObjectName("action7")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.actionRules = QtWidgets.QAction(MainWindow)
        self.actionRules.setObjectName("actionRules")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.menuChange_difficulty.addAction(self.actionEasy)
        self.menuChange_difficulty.addAction(self.actionMedium)
        self.menuChange_difficulty.addAction(self.actionHard)
        self.menuRounds.addAction(self.action15)
        self.menuRounds.addAction(self.action5)
        self.menuRounds.addAction(self.action7)
        self.menuRounds.addAction(self.actionCustom)
        self.menuFILE.addAction(self.actionRestart_round)
        self.menuFILE.addAction(self.actionNew_player)
        self.menuFILE.addAction(self.actionLoad_player)
        self.menuFILE.addAction(self.menuChange_difficulty.menuAction())
        self.menuFILE.addAction(self.menuRounds.menuAction())
        self.menuHELP.addAction(self.actionRules)
        self.menuHELP.addAction(self.actionInstructions)
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())

        self.menuChange_difficulty.setEnabled(False)
        self.actionRestart_round.setEnabled(False)
        self.menuRounds.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSP GAME"))
        self.pushButton.setText(_translate("MainWindow", "ROCK"))
        self.pushButton_2.setText(_translate("MainWindow", "SCISSORS"))
        self.pushButton_3.setText(_translate("MainWindow", "PAPER"))
        self.label.setText(_translate("MainWindow", "PLAYER"))
        self.label_2.setText(_translate("MainWindow", "VERSUS"))
        self.label_3.setText(_translate("MainWindow", "[AI] BOB"))
        self.label_4.setText(_translate("MainWindow", "Rounds left:"))
        self.label_5.setPixmap(self.rock_img)
        self.label_6.setPixmap(self.scissors_img)
        self.label_7.setPixmap(self.paper_img)
        self.label_8.setText(_translate("MainWindow", "Difficulty:"))
        self.label_9.setText(_translate("MainWindow", "EASY"))
        self.label_10.setText(_translate("MainWindow", "RESULT:"))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE"))
        self.menuChange_difficulty.setTitle(_translate("MainWindow", "Change difficulty"))
        self.menuRounds.setTitle(_translate("MainWindow", "Rounds"))
        self.menuHELP.setTitle(_translate("MainWindow", "HELP"))
        self.actionRestart_round.setText(_translate("MainWindow", "Restart round"))
        self.actionNew_player.setText(_translate("MainWindow", "New player"))
        self.actionLoad_player.setText(_translate("MainWindow", "Load player"))
        self.actionEasy.setText(_translate("MainWindow", "Easy"))
        self.actionMedium.setText(_translate("MainWindow", "Medium"))
        self.actionHard.setText(_translate("MainWindow", "Hard"))
        self.action15.setText(_translate("MainWindow", "15"))
        self.action5.setText(_translate("MainWindow", "5"))
        self.action7.setText(_translate("MainWindow", "7"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))
        self.actionRules.setText(_translate("MainWindow", "Rules"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        

    def unlock_options(self):
        self.menuRounds.setEnabled(True)
        self.actionRestart_round.setEnabled(True)
        self.menuChange_difficulty.setEnabled(True)

    def new_player(self):
        name = self.input_name.text()
        if len(name) < 3:
            self.warning.show()
        elif not self._users.add_player(name):
            self.warning.setText("Player already exists !!!")
            self.warning.show()
        else:
            self.label.setText(name)
            self.unlock_options()
            self.new_player_d.reject()

    def load_player(self):
        if self._users.load_player(self.load_name.text()):
            name = self.load_name.text()
            self.label.setText(name)
            self.unlock_options()
            self.load_player_d.reject()
        else:
            self.invalid.show()

    def handle_rounds(self,rounds):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)

    def AI_display_img(self, result):
        if result == 'ROCK':
            response = QtWidgets.QGraphicsPixmapItem(self.rock_img_small)
        elif result == 'SCISSORS':
            response = QtWidgets.QGraphicsPixmapItem(self.scissors_img_small)
        else:
            response = QtWidgets.QGraphicsPixmapItem(self.paper_img_small)
        return response

    def user_input(self, input):
        if self.label_9.text() == 'EASY':
            AI_res = self._rcp.AI_answer(input)
            result = self._rcp.user_input(input, AI_res)
            upper_AI_res = AI_res.upper()
            AI_display_res = self.AI_display_img(upper_AI_res)
            self.scene2.clear()
            self.scene2.addItem(AI_display_res)
            rounds_left = int(self.lcdNumber_3.value())

            if result == 'WON':
                display_res = QtWidgets.QGraphicsSimpleTextItem('WON')
                self.scene.clear()
                self.scene.addItem(display_res)
                player_score = int(self.lcdNumber.value()) + 1
                self.lcdNumber.display(float(player_score))
                rounds_left = rounds_left - 1
                self.lcdNumber_3.display(float(rounds_left))
                if rounds_left == 0.0:
                    self.handle_rounds(rounds_left)

            elif result == 'LOST':
                display_res = QtWidgets.QGraphicsSimpleTextItem('LOST')
                self.scene.clear()
                self.scene.addItem(display_res)
                AI_score = int(self.lcdNumber_2.value()) + 1
                self.lcdNumber_2.display(float(AI_score))
                rounds_left = rounds_left - 1
                self.lcdNumber_3.display(float(rounds_left))
                if rounds_left == 0.0:
                    self.handle_rounds(rounds_left)

            else:
                display_res = QtWidgets.QGraphicsSimpleTextItem('DRAW')
                self.scene.clear()
                self.scene.addItem(display_res)

        elif self.label_9.text() == 'MEDIUM':
            name = self.label.text()
            AI_res = self._rcp_med.ai_answer(name)
            result = self._rcp_med.user_input(input, AI_res, name)
            upper_AI_res = AI_res.upper()
            AI_display_res = self.AI_display_img(upper_AI_res)
            self.scene2.clear()
            self.scene2.addItem(AI_display_res)
            rounds_left = int(self.lcdNumber_3.value())

            if result == 'WON':
                display_res = QtWidgets.QGraphicsSimpleTextItem('WON')
                self.scene.clear()
                self.scene.addItem(display_res)
                player_score = int(self.lcdNumber.value()) + 1
                self.lcdNumber.display(float(player_score))
                rounds_left = rounds_left - 1
                self.lcdNumber_3.display(float(rounds_left))
                if rounds_left == 0.0:
                    self.handle_rounds(rounds_left)

            elif result == 'LOST':
                display_res = QtWidgets.QGraphicsSimpleTextItem('LOST')
                self.scene.clear()
                self.scene.addItem(display_res)
                AI_score = int(self.lcdNumber_2.value()) + 1
                self.lcdNumber_2.display(float(AI_score))
                rounds_left = rounds_left - 1
                self.lcdNumber_3.display(float(rounds_left))
                if rounds_left == 0.0:
                    self.handle_rounds(rounds_left)

            else:
                display_res = QtWidgets.QGraphicsSimpleTextItem('DRAW')
                self.scene.clear()
                self.scene.addItem(display_res)

        else:
            self.label_9.text() == 'HARD'
            name = self.label.text()
            AI_res = self._rcp_hard.aiHard_answer(name)
            result = self._rcp_hard.user_input(input, AI_res, name)
            upper_AI_res = AI_res.upper()
            AI_display_res = self.AI_display_img(upper_AI_res)
            self.scene2.clear()
            self.scene2.addItem(AI_display_res)
            rounds_left = int(self.lcdNumber_3.value())

            if result == 'WON':
                display_res = QtWidgets.QGraphicsSimpleTextItem('WON')
                self.scene.clear()
                self.scene.addItem(display_res)
                player_score = int(self.lcdNumber.value()) + 1
                self.lcdNumber.display(float(player_score))
                rounds_left = rounds_left - 1
                self.lcdNumber_3.display(float(rounds_left))
                if rounds_left == 0.0:
                    self.handle_rounds(rounds_left)

            elif result == 'LOST':
                display_res = QtWidgets.QGraphicsSimpleTextItem('LOST')
                self.scene.clear()
                self.scene.addItem(display_res)
                AI_score = int(self.lcdNumber_2.value()) + 1
                self.lcdNumber_2.display(float(AI_score))
                rounds_left = rounds_left - 1
                self.lcdNumber_3.display(float(rounds_left))
                if rounds_left == 0.0:
                    self.handle_rounds(rounds_left)

            else:
                display_res = QtWidgets.QGraphicsSimpleTextItem('DRAW')
                self.scene.clear()
                self.scene.addItem(display_res)

    def start_game(self, rounds):
        self.lcdNumber_3.display(float(rounds))
        self.lcdNumber_2.display(0.0)
        self.lcdNumber.display(0.0)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.store_rounds_nr = rounds

    def restart_round(self):
        rounds = self.store_rounds_nr
        self.lcdNumber.display(0.0)
        self.lcdNumber_2.display(0.0)
        self.lcdNumber_3.display(rounds)
        self.scene.clear()
        self.scene2.clear()
        if rounds != 0.0:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)

    
    def set_difficulty(self, difficulty):
        if difficulty == 'easy':
            self.label_9.setText('EASY')
            return 'easy'
        elif difficulty == 'medium':
            self.label_9.setText('MEDIUM')

            return 'medium'

        elif difficulty == 'hard':
            self.label_9.setText('HARD')
            return 'hard'
        else:
            pass




    def show_rules(self):
        rules = QtWidgets.QDialog()
        rules.setWindowIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxWarning))
        rules.resize(250,200)
        label = QtWidgets.QLabel(rules)
        label.setGeometry(QtCore.QRect(10, 40, 250, 71))
        label.setStyleSheet("font-size:12px")
        label.setAlignment(QtCore.Qt.AlignLeft)
        label.setObjectName("label")
        label.setText('1. Rock beats Scissors.')
        label_2 = QtWidgets.QLabel(rules)
        label_2.setGeometry(QtCore.QRect(10, 70, 250, 71))
        label_2.setStyleSheet("font-size:12px")
        label_2.setAlignment(QtCore.Qt.AlignLeft)
        label_2.setObjectName("label_2")
        label_2.setText('2. Scissors beats Paper.')
        label_3 = QtWidgets.QLabel(rules)
        label_3.setGeometry(QtCore.QRect(10, 100, 250, 71))
        label_3.setStyleSheet("font-size:12px")
        label_3.setAlignment(QtCore.Qt.AlignLeft)
        label_3.setObjectName("label_3")
        label_3.setText('3. Paper beats Rock.')
        label_4 = QtWidgets.QLabel(rules)
        label_4.setGeometry(QtCore.QRect(10, 130, 250, 71))
        label_4.setStyleSheet("font-size:12px")
        label_4.setAlignment(QtCore.Qt.AlignLeft)
        label_4.setObjectName("label_4")
        label_4.setText('4. In case of draw, the round is skipped.')
        rules.setMinimumSize(QtCore.QSize(250, 200))
        rules.setMaximumSize(QtCore.QSize(250, 200))
        rules.setWindowTitle("RULES")
        rules.setWindowModality(QtCore.Qt.WindowModal)
        rules.exec_()

    def show_instructions(self):
        rules = QtWidgets.QDialog()
        rules.setWindowIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxWarning))
        rules.resize(250,250)
        label = QtWidgets.QLabel(rules)
        label.setGeometry(QtCore.QRect(10, 20, 250, 71))
        label.setStyleSheet("font-size:12px")
        label.setAlignment(QtCore.Qt.AlignLeft)
        label.setObjectName("label")
        label.setText('1. Create a new player or load an existing \n one by clicking:\n\t FILE -> New player/Load player.')
        label_2 = QtWidgets.QLabel(rules)
        label_2.setGeometry(QtCore.QRect(10, 75, 250, 71))
        label_2.setStyleSheet("font-size:12px")
        label_2.setAlignment(QtCore.Qt.AlignLeft)
        label_2.setObjectName("label_2")
        label_2.setText('2. Select difficulty - Easy, Medium, Hard.')
        label_3 = QtWidgets.QLabel(rules)
        label_3.setGeometry(QtCore.QRect(10, 101, 250, 83))
        label_3.setStyleSheet("font-size:12px")
        label_3.setAlignment(QtCore.Qt.AlignLeft)
        label_3.setObjectName("label_3")
        label_3.setText('3. Select number of rounds:\n\t- 5 rounds = best of 5.\n\t- 7 rounds = best of 7\n\t- 15 rounds = best of 15\n\t- Custom = you choose the\n\t  number of rounds.')
        label_4 = QtWidgets.QLabel(rules)
        label_4.setGeometry(QtCore.QRect(10, 195, 250, 71))
        label_4.setStyleSheet("font-size:12px")
        label_4.setAlignment(QtCore.Qt.AlignLeft)
        label_4.setObjectName("label_4")
        label_4.setText('4. You can restart the rounds at any time\n\t FILE -> Restart round.')
        rules.setMinimumSize(QtCore.QSize(250, 250))
        rules.setMaximumSize(QtCore.QSize(250, 250))
        rules.setWindowTitle("INSTRUCTIONS")
        rules.setWindowModality(QtCore.Qt.WindowModal)
        rules.exec_()
    
    def new_player_dialog(self):
        self.new_player_d = QtWidgets.QDialog()
        self.new_player_d.setWindowIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton))
        self.new_player_d.resize(250,200)
        info = QtWidgets.QLabel(self.new_player_d)
        info.setGeometry(QtCore.QRect(25, 70, 250, 71))
        info.setStyleSheet("font-size:12px")
        info.setAlignment(QtCore.Qt.AlignLeft)
        info.setObjectName("info")
        info.setText('Enter your name(min. 3 characters):')
        pushButton = QtWidgets.QPushButton(self.new_player_d)
        pushButton.setGeometry(QtCore.QRect(103, 130, 40, 30))
        pushButton.setObjectName("OK")
        pushButton.setText('OK')
        self.warning = QtWidgets.QLabel(self.new_player_d)
        self.warning.setGeometry(QtCore.QRect(80, 170, 250, 71))
        self.warning.setStyleSheet("font-size:12px")
        self.warning.setAlignment(QtCore.Qt.AlignLeft)
        self.warning.setObjectName("warning")
        self.warning.setText('Name too short !!!')
        self.warning.hide()  
        self.input_name = QtWidgets.QLineEdit(self.new_player_d)
        self.input_name.setGeometry(QtCore.QRect(48,90,150,30))
        self.new_player_d.setMinimumSize(QtCore.QSize(250, 200))
        self.new_player_d.setMaximumSize(QtCore.QSize(250, 200))
        self.new_player_d.setWindowTitle("New player registration")
        self.new_player_d.setWindowModality(QtCore.Qt.ApplicationModal)
        pushButton.clicked.connect(lambda: self.new_player())
        self.new_player_d.exec_()

    def load_player_dialog(self):
        self.load_player_d = QtWidgets.QDialog()
        self.load_player_d.setWindowIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton))
        self.load_player_d.resize(250,200)
        info = QtWidgets.QLabel(self.load_player_d)
        info.setGeometry(QtCore.QRect(42, 70, 250, 71))
        info.setStyleSheet("font-size:12px")
        info.setAlignment(QtCore.Qt.AlignLeft)
        info.setObjectName("info")
        info.setText('Enter the name of the player:')
        pushButton = QtWidgets.QPushButton(self.load_player_d)
        pushButton.setGeometry(QtCore.QRect(103, 130, 40, 30))
        pushButton.setObjectName("OK")
        pushButton.setText('OK')
        self.invalid = QtWidgets.QLabel(self.load_player_d)
        self.invalid.setGeometry(QtCore.QRect(80, 170, 250, 71))
        self.invalid.setStyleSheet("font-size:12px")
        self.invalid.setAlignment(QtCore.Qt.AlignLeft)
        self.invalid.setObjectName("invalid")
        self.invalid.setText('Name doesnt exist !!!')
        self.invalid.hide()  
        self.load_name = QtWidgets.QLineEdit(self.load_player_d)
        self.load_name.setGeometry(QtCore.QRect(48,90,150,30))
        self.load_player_d.setMinimumSize(QtCore.QSize(250, 200))
        self.load_player_d.setMaximumSize(QtCore.QSize(250, 200))
        self.load_player_d.setWindowTitle("Load existing player")
        self.load_player_d.setWindowModality(QtCore.Qt.ApplicationModal)
        pushButton.clicked.connect(lambda: self.load_player())
        self.load_player_d.exec_()


    def custom_rounds_nr(self):
        rounds = self.input_rounds.text()
        if int(rounds) < 1 or int(rounds)%2 == 0:
            self.wrong_number.show()
        else:
            self.start_game(int(rounds))
            self.custom_rounds.reject()
    
    def start_custom_rounds(self):
        self.custom_rounds = QtWidgets.QDialog()
        self.custom_rounds.setWindowIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton))
        self.custom_rounds.resize(250,200)
        info = QtWidgets.QLabel(self.custom_rounds)
        info.setGeometry(QtCore.QRect(6, 70, 250, 71))
        info.setStyleSheet("font-size:12px")
        info.setAlignment(QtCore.Qt.AlignLeft)
        info.setObjectName("info")
        info.setText('Enter nr. of rounds(odd number, min = 1):')
        pushButton = QtWidgets.QPushButton(self.custom_rounds)
        pushButton.setGeometry(QtCore.QRect(103, 125, 40, 30))
        pushButton.setObjectName("OK")
        pushButton.setText('OK')
        self.wrong_number = QtWidgets.QLabel(self.custom_rounds)
        self.wrong_number.setGeometry(QtCore.QRect(80, 170, 250, 71))
        self.wrong_number.setStyleSheet("font-size:12px")
        self.wrong_number.setAlignment(QtCore.Qt.AlignLeft)
        self.wrong_number.setObjectName("wrong_number")
        self.wrong_number.setText('Invalid number !!!')
        self.wrong_number.hide()  
        self.input_rounds = QtWidgets.QLineEdit(self.custom_rounds)
        self.input_rounds.setGeometry(QtCore.QRect(48,90,150,30))
        self.custom_rounds.setMinimumSize(QtCore.QSize(250, 200))
        self.custom_rounds.setMaximumSize(QtCore.QSize(250, 200))
        self.custom_rounds.setWindowTitle("Custom number of rounds")
        self.custom_rounds.setWindowModality(QtCore.Qt.ApplicationModal)
        pushButton.clicked.connect(lambda: self.custom_rounds_nr())
        self.custom_rounds.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.actionNew_player.triggered.connect(lambda: ui.new_player_dialog())
    ui.actionLoad_player.triggered.connect(lambda: ui.load_player_dialog())

    ui.action7.triggered.connect(lambda: ui.start_game(7))
    ui.action15.triggered.connect(lambda: ui.start_game(15))
    ui.action5.triggered.connect(lambda: ui.start_game(5))
    ui.actionCustom.triggered.connect(lambda: ui.start_custom_rounds())

    ui.actionRestart_round.triggered.connect(lambda: ui.restart_round())

    ui.actionEasy.triggered.connect(lambda: ui.set_difficulty('easy'))
    ui.actionMedium.triggered.connect(lambda: ui.set_difficulty('medium'))
    ui.actionHard.triggered.connect(lambda: ui.set_difficulty('hard'))
    
    
    ui.pushButton.clicked.connect(lambda: ui.user_input('rock'))
    ui.pushButton_2.clicked.connect(lambda: ui.user_input('scissors'))
    ui.pushButton_3.clicked.connect(lambda: ui.user_input('paper'))
    
    ui.actionRules.triggered.connect(lambda: ui.show_rules())
    ui.actionInstructions.triggered.connect(lambda: ui.show_instructions())

    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


