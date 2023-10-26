*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Move on the edge left of the board      0   0   0   NORTH   0   1   1              
Move on the edge left of the board      0   0   5   SOUTH   0   0   6
Move on the edge left of the board      0   0   42  EAST    1   0   43   
Move on the edge left of the board      0   0   32  WEST    0   0   33
Move on the edge top right edge of the board    9   9   100 NORTH   9   9   101
Move on the edge top right edge of the board    9   9   50  SOUTH   9   8   51
Move on the edge top right edge of the board    9   9   75  EAST    9   9   76
Move on the edge top right edge of the board    9   9   33  WEST    8   9   34
Move on the edge bottom right edge of the board     0   9   NORTH   0   9   12
Move on the edge bottom right edge of the board     0   9   SOUTH   0   9   23             
Lower right - move left     9   0   90  WEST    8   0   91
Lower right - move up     9   0   91  NORTH    9   1   92
Lower right - move right     9   0   92  EAST    9   0   93
Lower right - move down     9   0   93  SOUTH    9   0   94

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}