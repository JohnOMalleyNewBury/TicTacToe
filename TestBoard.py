#! /usr/bin/env python
__author__ = 'John Omalley'

from gameObjects import Board

testBoard = Board()
testBoard.setMark(3, 'X')
testBoard.setMark(4, 'X')
testBoard.setMark(7, 'O')
print(testBoard.getMark(3))
print(testBoard.getMark(4))
print(testBoard.getMark(7))


print(testBoard.findBlock('O'))
print(testBoard.findWin('X'))
