#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: logo.py
@Time: 18-8-16 14:42
@Last_update: 18-8-16 14:42
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
LINKINGMED_LOGO = \
    "===================================================\n"\
    "   __ _       _    _                             _ \n" \
    "  / /(_)_ __ | | _(_)_ __   __ _  /\/\   ___  __| |\n" \
    " / / | | '_ \| |/ / | '_ \ / _` |/    \ / _ \/ _` |\n" \
    "/ /__| | | | |   <| | | | | (_| / /\/\ \  __/ (_| |\n" \
    "\____/_|_| |_|_|\_\_|_| |_|\__, \/    \/\___|\__,_|\n" \
    "                           |___/       LinkingMed  \n"\
    "                                   version:%s\n"\
    "===================================================\n"

HEART_LOGO = \
    "===================================================\n"\
    "                   ***    ***                      \n"\
    "                  ************                     \n"\
    "                   **********     HEART FOUR ORGAN \n"\
    "                     ******            SEGMENT     \n"\
    "                       **        version:%s\n"\
    "===================================================\n"

WHOLE_HEART_LOGO = \
    "===================================================\n"\
    "                   ***    ***                      \n"\
    "                  ************                     \n"\
    "                   **********        WHOLE HEART   \n"\
    "                     ******            SEGMENT     \n"\
    "                       **        version:%s\n"\
    "===================================================\n"

def print_linkingmed_logo(version):
    print(LINKINGMED_LOGO%version)

def print_heart_logo(version):
    print(HEART_LOGO%version)

def print_whole_heart_logo(version):
    print(WHOLE_HEART_LOGO%version)

if __name__ == '__main__':
    print_linkingmed_logo('1.3.7')
    print_heart_logo('2018.8.2')