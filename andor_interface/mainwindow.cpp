#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "python_expect.h"
#include "fwandor.h"
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->rbtnNone->setChecked(true);
    ui->cboxFilter->setCurrentIndex(6);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnConnect_clicked()
{   ui->rbtnPython->setChecked(true);//set the button for python console
    char out[499];
    f = initF(out);
    f_status = 1;
    ui->output->moveCursor(QTextCursor::End);
    ui->output->insertPlainText(out);

    //import la classe
    int result = command(f,"from python_andor import command as com\n",out);
    ui->output->moveCursor(QTextCursor::End);
    ui->output->insertPlainText(out);
}

void MainWindow::on_input_returnPressed()

{   char out[499];
    QString in= ui->input->text();
    if (rbtnStatus==2)
    {
        command_bash(in.toStdString()+"\n",out);
    }
    else {
        command(f,in.toStdString()+"\n",out);
    }
    ui->input->clear();
    ui->output->moveCursor(QTextCursor::End);
    ui->output->insertPlainText(out);
}


void MainWindow::on_btnStart_clicked()
{
        char out[499];

        command(f,"com.video()\n",out);
        ui->input->clear();
        ui->output->moveCursor(QTextCursor::End);
        ui->output->insertPlainText(out);
}

void MainWindow::on_btnScript_clicked()
{
    char out[499];

    command(f,"com.script()\n",out);
    ui->input->clear();
    ui->output->moveCursor(QTextCursor::End);
    ui->output->insertPlainText(out);
}

void MainWindow::on_btnStop_clicked()
{
    char out[499];

    command(f,"com.stop_acq()\n",out);
    ui->input->clear();
    ui->output->moveCursor(QTextCursor::End);
    ui->output->insertPlainText(out);
}


void MainWindow::on_rbtnNone_clicked()
{
    rbtnStatus = 0;
}

void MainWindow::on_rbtnPython_clicked()
{   char out[499];
    if (f_status==0)
    {
        f = initF(out);

        ui->output->moveCursor(QTextCursor::End);
        ui->output->insertPlainText(out);
        ui->output->moveCursor(QTextCursor::End);
        ui->output->insertPlainText("cou cou");
    }
    rbtnStatus = 1;//python
}

void MainWindow::on_rbtnBash_clicked()
{
    rbtnStatus = 2;//python

}

void MainWindow::on_actionTutorial_triggered()
{
    char out[499];
    command_bash("evince /home/pesto/data_andor/andor_interface/python_andor.pdf\n",out);
    ui->output->moveCursor(QTextCursor::End);
    ui->output->insertPlainText(out);
}

void MainWindow::on_cboxFilter_currentIndexChanged(int index)
{
//    std::cout<<"index: "<<ui->cboxFilter->currentIndex()<<std::endl;
//    std::cout<<"index: "<<index<<std::endl;
//        if (fwInitialize!=1 && ui->cboxFilter->currentIndex()==1)
//        {
//            ui->output->moveCursor(QTextCursor::End);
//            ui->output->insertPlainText("Humming the filter wheel song. Please wait...\n");
//            int error = fw.home();
//            QCoreApplication::processEvents();
//            std::cout<<error<<std::endl;
//            if (error!=0)
//            {
//                //std::cout<<"fuck"<<std::endl;
//                ui->cboxFilter->setCurrentIndex(0);
//            }
//            else
//            {
//                fwInitialize = 1;
//                ui->cboxFilter->setCurrentIndex(2);

//                previousFilter = 0;
//            }
//        }
//        else if (fwInitialize!=1 && ui->cboxFilter->currentIndex()!=1)
//        {
//            ui->output->moveCursor(QTextCursor::End);
//            ui->output->insertPlainText("please home the filter wheel before selecting a position.\n");
//        }
//        else if (ui->cboxFilter->currentIndex()==0)
//        {
//                 ui->cboxFilter->setCurrentIndex(previousFilter);
//                 ui->output->moveCursor(QTextCursor::End);
//                ui->output->insertPlainText("This is not a valid choice!\n");

//        }
//        else
//        {   ui->output->moveCursor(QTextCursor::End);
//            ui->output->insertPlainText("Humming the filter wheel song. Please wait...\n");

//            if (fw.position(ui->cboxFilter->currentIndex()-1)!=ui->cboxFilter->currentIndex()-1)
//            {
//                ui->cboxFilter->setCurrentIndex(previousFilter);
//            }
//            else
//            {
//                previousFilter = ui->cboxFilter->currentIndex();
//            }
//        }
//                 ui->output->moveCursor(QTextCursor::End);
//        ui->output->insertPlainText("Done!\n");
//        ui->cboxFilter->setCurrentIndex(0);
}

void MainWindow::on_cboxFilter_activated(int index)
{
    std::cout<<"index: "<<ui->cboxFilter->currentIndex()<<std::endl;
    std::cout<<"index: "<<index<<std::endl;
        if (fwInitialize!=1 && ui->cboxFilter->currentIndex()==0)
        {
            ui->output->moveCursor(QTextCursor::End);
            ui->output->insertPlainText("Humming the filter wheel song. Please wait...\n");
            QCoreApplication::processEvents();
            int error = fw.home();

            std::cout<<error<<std::endl;
            if (error!=0)
            {
                //std::cout<<"fuck"<<std::endl;
                fwInitialize = 1;
                ui->cboxFilter->setCurrentIndex(0);
            }
            else
            {
                fwInitialize = 1;
                ui->cboxFilter->setCurrentIndex(0);

                previousFilter = 0;
            }
        }
        else if (fwInitialize!=1 && ui->cboxFilter->currentIndex()!=0)
        {
            ui->output->moveCursor(QTextCursor::End);
            ui->output->insertPlainText("please home the filter wheel before selecting a position.\n");
            ui->cboxFilter->setCurrentIndex(6);
        }

        else if (ui->cboxFilter->currentIndex()==0)
        {
                 ui->cboxFilter->setCurrentIndex(previousFilter);
                 ui->output->moveCursor(QTextCursor::End);
                ui->output->insertPlainText("This is not a valid choice!\n");

        }
        else
        {   ui->output->moveCursor(QTextCursor::End);
            ui->output->insertPlainText("Humming the filter wheel song. Please wait...\n");
            QCoreApplication::processEvents();
            int check;
            if (ui->cboxFilter->currentIndex()==0)
            {
                check = fw.home();
            }
            else
            {
                check = fw.position(ui->cboxFilter->currentIndex());
            }
            if (check!=ui->cboxFilter->currentIndex())
            {
                ui->cboxFilter->setCurrentIndex(previousFilter);
            }
            else
            {
                previousFilter = ui->cboxFilter->currentIndex();
            }
        }
                 ui->output->moveCursor(QTextCursor::End);
        ui->output->insertPlainText("Done!\n");

}
