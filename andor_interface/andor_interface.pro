#-------------------------------------------------
#
# Project created by QtCreator 2019-05-24T12:12:18
#
#-------------------------------------------------
QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = andor_interface
TEMPLATE = app
# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS
# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++11

SOURCES += \
        main.cpp \
        mainwindow.cpp \
    python_expect.cpp \
    fwandor.cpp \
    socket.cpp

HEADERS += \
        mainwindow.h \
    python_expect.h \
    fwandor.h \
    socket.h

FORMS += \
        mainwindow.ui


INCLUDEPATH += $$PWD/../../../../../../../../usr/local/lib/expect5.45.4/
DEPENDPATH += $$PWD/../../../../../../../../usr/local/lib/expect5.45.4/





win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../../../../../../usr/local/lib/release/ -lm
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../../../../../../usr/local/lib/debug/ -lm
else:unix: LIBS += -L$$PWD/../../../../../../../../usr/local/lib/ -lm

INCLUDEPATH += $$PWD/../../../../../../../../usr/local/include
DEPENDPATH += $$PWD/../../../../../../../../usr/local/include

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../../../../../../usr/local/lib/release/ -lexpect
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../../../../../../usr/local/lib/debug/ -lexpect
else:unix: LIBS += -L$$PWD/../../../../../../../../usr/local/lib/ -lexpect

INCLUDEPATH += $$PWD/../../../../../../../../usr/local/include
DEPENDPATH += $$PWD/../../../../../../../../usr/local/include

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../../../../../../usr/local/lib/release/ -ltcl8.6
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../../../../../../usr/local/lib/debug/ -ltcl8.6
else:unix: LIBS += -L$$PWD/../../../../../../../../usr/local/lib/ -ltcl8.6

INCLUDEPATH += $$PWD/../../../../../../../../usr/local/include
DEPENDPATH += $$PWD/../../../../../../../../usr/local/include
