*** Settings ***
Documentation     I want to identify the x,y coordinates. 
Test Template     Position coordinates
Library           PositionLibrary.py

*** Test Cases ***      X     Y
Get coordinates       3   4

*** Keywords ***
Position coordinates
    [Arguments]    ${x}    ${y}
    Initialize character xposition with  ${x}
    Initialize character yposition with  ${y}
