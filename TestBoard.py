#! /usr/bin/env python
__author__ = 'John Omalley'

from gameObjects import Board

testBoard = Board()
testBoard.setMark(0, 'X')
testBoard.setMark(1, 'X')
testBoard.setMark(2, 'O')
print(testBoard.getMark(0))
print(testBoard.getMark(1))
print(testBoard.getMark(2))

