#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kayma
#
# Created:     07-05-2024
# Copyright:   (c) kayma 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


d1 = {
    "A0": "MAX",
    "A1": "same-india",
    "A2": "america",
    "A3": {
        "B1": {"COMPLEX1": "VAL", "COMPLEX2": "VAL2"},
        "B2": ["AR1", "AR2", "AR3"],
        "B3": ["AR4", "AR5"],
        "B4": ["A6"],
    },
    "A4": {
        "B1": {"COMPLEX1": "VAL", "COMPLEX2": "VAL2"},
        "B2": ["AR1", "AR2", "AR3"],
        "B3": ["AR4", "AR5"],
        "B4": ["A6"],
    },
    "A5": "will-remove-german",
    "A5C": {"COMP1": "VAL", "COMP2":"VAL2"}
}

d2 = {
    "A0": ["MAX", "TYPE-CHANGED"],
    "A1": "same-india",
    "A2": "modifed-america",
    "A3": {
        "B1": {"COMPLEX1": "VALMOD", "COMPLEX2": "VAL2"},
        "B2": ["AR1", "AR3"],
        "B3": ["AR4", "AR5", "AR6"],
        "B4": ["A7"],
        "BZ": {
                    "SOME":"ONE"
                }
    },
    "A4": {
        "B1": {"COMPLEX1": "VAL"},
        "B2": ["AR2", "AR1", "AR3"],
        "B4": ["A6"]},
    "A6": "added-paks",
    "A6C": {"COMP1": "VAL", "COMP2":"VAL2"}
}

from deepdiff import DeepDiff 
import json


diff = DeepDiff(d1, d2)


##
##for each in diff:
##    print(each + '->' + str(diff[each]))




def handleValueChanged(inp):
    dpath = inp.replace('root','').replace('][','.').replace('[','').replace(']','').replace('\'','').split('.')

    inp = {}
    for key in reversed(dpath):
        inp = {key: inp}

    return inp

inp = "root['A3']['B1']['COMPLEX1']"
res = handleValueChanged(inp)
print res


