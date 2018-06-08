#!/usr/bin/env python

import sys
from sys import path
import sys
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load
from os import path
from PyQt5.QtCore import pyqtSlot, QSettings, Qt, QTimer, QCoreApplication
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
# import tictactoeResources_rc
from time import sleep
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication
from gameObjects import *

class TicTacToe(QMainWindow) :
    """A game of Craps."""

    def __init__( self, parent=None ):
        """Build a g+ame with two dice."""

        super().__init__(parent)
        uic.loadUi("tictactoe.ui", self)

        self.logger = getLogger("John.craps")
        self.appSettings = QSettings()
        self.quitCounter = 0

        uic.loadUi("settings.ui", self)

        self.pickFilename = "ticTactoeSave"

        self.restoreSetting()

        self.wins = 0
        self.losses = 0
        self.playerMark = "X"
        self.gameInProgress = True

        self.gameBoard = Board()

        self.square0.clicked.connect(lambda: self.buttonClickedHandler(0))
        self.square1.clicked.connect(lambda: self.buttonClickedHandler(1))
        self.square2.clicked.connect(lambda: self.buttonClickedHandler(2))
        self.square3.clicked.connect(lambda: self.buttonClickedHandler(3))
        self.square4.clicked.connect(lambda: self.buttonClickedHandler(4))
        self.square5.clicked.connect(lambda: self.buttonClickedHandler(5))
        self.square6.clicked.connect(lambda: self.buttonClickedHandler(6))
        self.square7.clicked.connect(lambda: self.buttonClickedHandler(7))
        self.square8.clicked.connect(lambda: self.buttonClickedHandler(8))

    def updateUI(self):
        if self.createLogFile:
            self.logger.info("Die1: %i, Die2: %i" % (self.die1.getValue(), self.die2.getValue()))
        self.bidSpinBox.setRange(self.minimumBet, self.maximumBet)
        self.bidSpinBox.setSingleStep(5)
        self.die1View.setPixmap(QtGui.QPixmap(":/" + str(self.die1.getValue())))
        self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
        if self.firstRoll:
            self.rollingForLabel.setText("")
        else:
            self.rollingForLabel.setText(str("%i" % self.firstRollValue))
        self.resultsLabel.setText(self.results)
        self.rollButton.setText(self.buttonText)
        self.winsLabel.setText(str("%i" % self.wins))
        self.lossesLabel.setText(str("%i" % self.losses))
        self.bankValue.setText(str("%i" % self.currentBank))




    def restoreGame(self):
        if self.appSettings.contains("ticTactoeSave"):
            self.appSettings.value("ticTactoeSave", type=str)
            with open(path.join(path.dirname(path.realpath(__file__)),
                                self.appSettings.value('pickleFilename', type=str)), 'rb') as pickleFile:
                return load(pickleFile)
        else:
            self.logger.critical("No pickle Filename")

    def saveGame(self):
        self.logger.debug("Saving game")
        saveItems = (self.playerMark, self.gameInProgress, self.gameBoard, self.wins, self.losses)
        if self.appSettings.contains('pickleFilename'):
            with open(path.join(path.dirname(path.realpath(__file__)),
                                self.appSettings.value('pickleFilename', type=str)), 'wb') as pickleFile:
                dump(saveItems, pickleFile)
        else:
            self.logger.critical("No pickle Filename")

    def __str__( self ):
        """String representation for Dice.
        """

        return ""

    def updateUI ( self ):
        self.square0.setText(self.gameBoard.getMark(0))
        self.square1.setText(self.gameBoard.getMark(1))
        self.square2.setText(self.gameBoard.getMark(2))
        self.square3.setText(self.gameBoard.getMark(3))
        self.square4.setText(self.gameBoard.getMark(4))
        self.square5.setText(self.gameBoard.getMark(5))
        self.square6.setText(self.gameBoard.getMark(6))
        self.square7.setText(self.gameBoard.getMark(7))
        self.square8.setText(self.gameBoard.getMark(8))

        # Add your code here to update the GUI view so it matches the game state.

		# Player asked for another roll of the dice.

        # Play the first roll

    def buttonClickedHandler(self, buttonValue):
        if self.gameInProgress:
            if self.gameBoard.isEmpty(buttonValue):
                self.gameBoard.setMark(buttonValue, self.playerMark)
            self.playerMark = "O"
            squareToMark = self.gameBoard.findWin(self.playerMark)
            if squareToMark != None:
                self.gameBoard.setMark(squareToMark, self.playerMark)
                self.playerMark = "X"
                if self.gameBoard.checForWin():
                    self.gameInProgress = False
                self.updateUI()
                return
            squareToMark= self.gameBoard.findBlock(self.playerMark)
            if squareToMark != None:
                self.gameBoard.setMark(squareToMark, self.playerMark)
                self.playerMark = "X"
                if self.gameBoard.checForWin():
                    self.gameInProgress = False
                self.updateUI()
                return
            self.gameBoard.setMark(self.gameBoard.getAvailableSquare(), self.playerMark)
            self.playerMark = "X"
            if self.gameBoard.checForWin():
                self.gameInProgress = False
            self.updateUI()
            return
        @pyqtSlot()  # Player asked to quit the game.
        def closeEvent(self, event):
            self.logger.debug("Closing app event")
            if self.quitCounter == 0:
                self.quitCounter += 1
                quitMessage = "Are you sure you want to quit?"
                reply = QMessageBox.question(self, 'Message', quitMessage, QMessageBox.Yes, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    self.saveGame()
                    event.accept()
                else:
                    event.ignore()
                return super().closeEvent(event)
        def restartGame(self):
            self.logger.debug("Restarting game")
            self.results = ""
            self.playerLost = False
            self.wins = 0
            self.losses = 0
            self.gameBoard.isEmpty
            self.gameInprogress = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tictactoeApp = TicTacToe()
    tictactoeApp.updateUI()
    tictactoeApp.show()
    sys.exit(app.exec_())
    QCoreApplication.setOrganizationName("OMALLEY Software");
    QCoreApplication.setOrganizationDomain("omalleysoftware.com");
    QCoreApplication.setApplicationName("TicTacToe");
    appSettings = QSettings()
    if appSettings.contains('createLogFile'):
        createLogFile = appSettings.value('createLogFile')
    else:
        logFilename = logFilenameDefault
        appSettings.setValue('logFile', logFilename)
    if createLogFile:
        startingFolderName = path.dirname(path.realpath(__file__))
        if appSettings.contains('logFile'):
            logFilename = appSettings.value('logFile', type=str)
        else:
            logFilename = logFilenameDefault
            appSettings.setValue('logFile', logFilename)
        basicConfig(filename=path.join(startingFolderName, logFilename), level=INFO,
                    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s')
class PreferencesDialog(QDialog):
    def __init__(self, parent = TicTacToe):
        super(PreferencesDialog, self).__init__()

        uic.loadUi('preferencesDialog.ui', self)
        self.logger = getLogger("Fireheart.craps")

        self.appSettings = QSettings()
        if self.appSettings.contains('logFile'):
            self.logFilename = self.appSettings.value('logFile', type=str)
        else:
            self.logFilename = "logFilenameDefault"
            self.appSettings.setValue('logFile', self.logFilename )

        if self.appSettings.contains('createLogFile'):
            self.createLogFile = self.appSettings.value('createLogFile')
        else:
            self.createLogFile = "logFilenameDefault"
            self.appSettings.setValue('createLogFile', self.createLogFile )

        self.buttonBox.rejected.connect(self.cancelClickedHandler)
        self.buttonBox.accepted.connect(self.okayClickedHandler)
        self.startingBankValue.editingFinished.connect(self.startingBankValueChanged)
        self.maximumBetValue.editingFinished.connect(self.maximumBetValueChanged)
        self.minimumBetValue.editingFinished.connect(self.minimumBetValueChanged)
        self.createLogfileCheckBox.stateChanged.connect(self.createLogFileChanged)

        self.updateUI()









