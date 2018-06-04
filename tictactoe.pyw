#!/usr/bin/env python

import sys
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tictactoeApp = TicTacToe()
    tictactoeApp.updateUI()
    tictactoeApp.show()
    sys.exit(app.exec_())
def restarButtonClickedHandler(self, gameInProgress):
    self.gameInProgress = True
    self.gameBoard.isEmpty

def logging (self):
    self.wins.settext
    self.losses
    self.gameboard.getmark
def resultCounter(self,wins,losses):
    self.wins
    self.losses
    if wins +1 :
        settext.wins





