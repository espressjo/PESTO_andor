#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "fwandor.h"
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_btnConnect_clicked();

    void on_input_returnPressed();

    void on_btnStart_clicked();

    void on_btnScript_clicked();

    void on_btnStop_clicked();

    void on_rbtnNone_clicked();

    void on_rbtnPython_clicked();

    void on_rbtnBash_clicked();

    void on_actionTutorial_triggered();

    void on_cboxFilter_currentIndexChanged(int index);

    void on_cboxFilter_activated(int index);

private:
    Ui::MainWindow *ui;
    FILE *f;
    int f_status = 0;

    int rbtnStatus = 0;
    FW fw;
    int previousFilter =6;
    int fwInitialize = 0;
};

#endif // MAINWINDOW_H
