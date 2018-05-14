#! /usr/bin/env python
__author__ = 'John Omalley'

from random import choice

class Square(object):
    def __init__(self):
        self.content = -1

    def setMark(self, newMark):
        if newMark == 'X':
            self.content = 1
        elif newMark == 'O':
            self.content = 2

    def getMark(self):
        if self.content == 1:
            return 'X'
        elif self.content == 2:
            return 'O'
        return ''

    def isEmpty(self):
        return self.content == -1

class Board(object):
    def __init__(self):
        self.gameBoard = []
        for squareNumber in range(0, 9):
            self.gameBoard.append(Square())
        self.availableList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.winningCombinations = ((0, 1, 2),
                                    (3, 4, 5),
                                    (6, 7, 8),
                                    (0, 4, 8),
                                    (2, 4, 6),
                                    (0, 3, 6),
                                    (1, 4, 6),
                                    (2, 5, 8))


    def isEmpty(self, squareNumber):
        return self.gameBoard[squareNumber].isEmpty()

    def setMark(self, squareNumber, playersMark):
        self.gameBoard[squareNumber].setMark(playersMark)
        del self.availableList[self.availableList.index(squareNumber)]

    def getMark(self, squareNumber):
        return self.gameBoard[squareNumber].getMark()

    def getAvailableList(self):
        return self.availableList

    def getAvailableSquare(self):
        return choice(self.availableList)

    def findBlock(self, playerMark):
        if playerMark == 'X':
            searchMark = 'O'
        else:
            searchMark = 'X'
        for combination in self.winningCombinations:
            if self.getMark(combination[0]) == searchMark and self.getMark(combination[1]) == searchMark and self.getMark(combination[2]) == '':
                return combination[2]
            elif self.getMark(combination[0]) == searchMark and self.getMark(combination[1]) == '' and self.getMark(combination[2]) == searchMark:
                return combination[1]
            elif self.getMark(combination[0]) == '' and self.getMark(combination[1]) == searchMark and self.getMark(combination[2]) == searchMark:
                return combination[0]



    def findWin(self):
        self.availableList[self.winningCombinations]
        self.checkPlayer

