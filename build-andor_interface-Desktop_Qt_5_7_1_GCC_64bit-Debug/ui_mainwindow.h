/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionTutorial;
    QWidget *centralWidget;
    QPlainTextEdit *output;
    QLineEdit *input;
    QRadioButton *rbtnPython;
    QRadioButton *rbtnBash;
    QRadioButton *rbtnNone;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *btnStart;
    QPushButton *btnStop;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *btnConnect;
    QPushButton *btnScript;
    QWidget *horizontalLayoutWidget_3;
    QHBoxLayout *horizontalLayout_3;
    QComboBox *cboxFilter;
    QLabel *label;
    QMenuBar *menuBar;
    QMenu *menudocumentation;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(882, 326);
        actionTutorial = new QAction(MainWindow);
        actionTutorial->setObjectName(QStringLiteral("actionTutorial"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        output = new QPlainTextEdit(centralWidget);
        output->setObjectName(QStringLiteral("output"));
        output->setGeometry(QRect(310, 10, 471, 211));
        input = new QLineEdit(centralWidget);
        input->setObjectName(QStringLiteral("input"));
        input->setGeometry(QRect(310, 240, 471, 25));
        rbtnPython = new QRadioButton(centralWidget);
        rbtnPython->setObjectName(QStringLiteral("rbtnPython"));
        rbtnPython->setGeometry(QRect(790, 20, 112, 23));
        rbtnBash = new QRadioButton(centralWidget);
        rbtnBash->setObjectName(QStringLiteral("rbtnBash"));
        rbtnBash->setGeometry(QRect(790, 50, 112, 23));
        rbtnNone = new QRadioButton(centralWidget);
        rbtnNone->setObjectName(QStringLiteral("rbtnNone"));
        rbtnNone->setGeometry(QRect(790, 80, 112, 23));
        verticalLayoutWidget = new QWidget(centralWidget);
        verticalLayoutWidget->setObjectName(QStringLiteral("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(20, 180, 191, 71));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        btnStart = new QPushButton(verticalLayoutWidget);
        btnStart->setObjectName(QStringLiteral("btnStart"));

        horizontalLayout->addWidget(btnStart);

        btnStop = new QPushButton(verticalLayoutWidget);
        btnStop->setObjectName(QStringLiteral("btnStop"));

        horizontalLayout->addWidget(btnStop);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        btnConnect = new QPushButton(verticalLayoutWidget);
        btnConnect->setObjectName(QStringLiteral("btnConnect"));

        horizontalLayout_2->addWidget(btnConnect);

        btnScript = new QPushButton(verticalLayoutWidget);
        btnScript->setObjectName(QStringLiteral("btnScript"));

        horizontalLayout_2->addWidget(btnScript);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayoutWidget_3 = new QWidget(centralWidget);
        horizontalLayoutWidget_3->setObjectName(QStringLiteral("horizontalLayoutWidget_3"));
        horizontalLayoutWidget_3->setGeometry(QRect(20, 80, 211, 51));
        horizontalLayout_3 = new QHBoxLayout(horizontalLayoutWidget_3);
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        cboxFilter = new QComboBox(horizontalLayoutWidget_3);
        cboxFilter->setObjectName(QStringLiteral("cboxFilter"));

        horizontalLayout_3->addWidget(cboxFilter);

        label = new QLabel(horizontalLayoutWidget_3);
        label->setObjectName(QStringLiteral("label"));

        horizontalLayout_3->addWidget(label);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 882, 22));
        menudocumentation = new QMenu(menuBar);
        menudocumentation->setObjectName(QStringLiteral("menudocumentation"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menudocumentation->menuAction());
        menudocumentation->addAction(actionTutorial);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        actionTutorial->setText(QApplication::translate("MainWindow", "Tutorial", Q_NULLPTR));
        rbtnPython->setText(QApplication::translate("MainWindow", "Python", Q_NULLPTR));
        rbtnBash->setText(QApplication::translate("MainWindow", "Bash", Q_NULLPTR));
        rbtnNone->setText(QApplication::translate("MainWindow", "None", Q_NULLPTR));
        btnStart->setText(QApplication::translate("MainWindow", "start", Q_NULLPTR));
        btnStop->setText(QApplication::translate("MainWindow", "stop", Q_NULLPTR));
        btnConnect->setText(QApplication::translate("MainWindow", "connect", Q_NULLPTR));
        btnScript->setText(QApplication::translate("MainWindow", "script", Q_NULLPTR));
        cboxFilter->clear();
        cboxFilter->insertItems(0, QStringList()
         << QString()
         << QApplication::translate("MainWindow", "Home", Q_NULLPTR)
         << QApplication::translate("MainWindow", "position 1", Q_NULLPTR)
         << QApplication::translate("MainWindow", "position 2", Q_NULLPTR)
         << QApplication::translate("MainWindow", "position 3", Q_NULLPTR)
         << QApplication::translate("MainWindow", "position 4", Q_NULLPTR)
         << QApplication::translate("MainWindow", "position 5", Q_NULLPTR)
        );
        label->setText(QApplication::translate("MainWindow", "Filter Wheel", Q_NULLPTR));
        menudocumentation->setTitle(QApplication::translate("MainWindow", "documentation", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
