from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
import os.path
from PyQt5.uic import loadUiType
import urllib.request
import pafy
import humanize
import os
from os import path

ui,_=loadUiType('main.ui')

class MainApp(QMainWindow,ui):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.setWindowTitle('Download Manager')
        
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
      ## Window Logo  
        self.setWindowIcon(QtGui.QIcon('./icons/logo.png'))
        
        self.Handle_Buttons()
        self.Apply_DarkBlue_Style()
        self.Move_Box_1()
        self.Move_Box_2()
        self.Move_Box_3()
        self.Move_Box_4()
        
        
    def InitUI(self):
        ## Handle all uichanges in loading
        self.tabWidget.tabBar().setVisible(False)
    
    def Handle_Buttons(self):
        ## Handle all buttons
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handle_Browse)
        self.pushButton_3.clicked.connect(self.Get_Video_Data)
        self.pushButton_4.clicked.connect(self.Save_Browse)
        self.pushButton_5.clicked.connect(self.Download_Video)
        self.pushButton_6.clicked.connect(self.Playlist_Save_Browse)
        self.pushButton_7.clicked.connect(self.Playlist_Download)
        self.pushButton_8.clicked.connect(self.Open_Home)
        self.pushButton_9.clicked.connect(self.Open_Download)
        self.pushButton_10.clicked.connect(self.Open_Youtube)
        self.pushButton_11.clicked.connect(self.Open_Setting)
        self.pushButton_19.clicked.connect(self.Apply_Dark_Style)
        self.pushButton_20.clicked.connect(self.Apply_DarkBlue_Style)
        self.pushButton_21.clicked.connect(self.Apply_DarkOrange_Style)
        self.pushButton_22.clicked.connect(self.Apply_Amoled_Style)
    
    def Handle_Progress(self,blocknum,blocksize,totalsize):
        ## Calculate Progress
        readed_data=blocknum*blocksize
        
        if totalsize>0:
            download_percent = readed_data*100/totalsize
            self.progressBar.setValue(download_percent)
            QApplication.processEvents()
    
    def Handle_Browse(self):
        ## Enable Browsing to our OS,pick save location
        save_location = QFileDialog.getSaveFileName(self , caption="Save As" , directory="." , filter="All Files(*.*)")
        self.lineEdit_2.setText(str(save_location[0]))
    
    def Download(self):
        ## Download any file
        print('Starting Download')
        download_url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        if download_url=="" or save_location=="":
            QMessageBox.warning(self,"Data Error","Provide a Valid URL or Save Location")
        else:
            try:
                urllib.request.urlretrieve(download_url,save_location,self.Handle_Progress)
            except Exception:
                QMessageBox.warning(self,"Download Error","Invalid URL , Please provide a valid URL")
                return
        QMessageBox.information(self,"Download Complete","Download Completed Successfully")
        self.lineEdit_2.setText('')
        self.lineEdit.setText('')
        self.progressBar.setValue(0)
    
    
    
### Download YouTube Single Video
    def Save_Browse(self):
        ## Save location in line edit
        save_location = QFileDialog.getSaveFileName(self , caption="Save As" , directory="." , filter="All Files(*.*)")
        self.lineEdit_4.setText(str(save_location[0]))
        

    def Get_Video_Data(self):
        video_url = self.lineEdit_3.text()
        if video_url=="":
            QMessageBox.warning(self,"Data Error","Provide a Valid URL")
        else:
            video = pafy.new(video_url)
            print(video.title)
            print(video.duration)
            print(video.viewcount)
            video_streams = video.videostreams
            for stream in video_streams:
                size = humanize.naturalsize(stream.get_filesize())
                data = "{} {}  {}   {}".format(stream.mediatype , stream.extension , stream.quality , size)
                self.comboBox.addItem(data)

    
    def Download_Video(self):
        video_url = self.lineEdit_3.text()
        save_location = self.lineEdit_4.text()
        if video_url=="" or save_location=="":
            QMessageBox.warning(self,"Data Error","Provide a Valid Video URL or Save Location")
        else:
            try:
                video = pafy.new(video_url)
                video_stream = video.videostreams
                video_quality = self.comboBox.currentIndex()
                download = video_stream[video_quality].download(filepath=save_location , callback=self.Video_Progress)
            except Exception:
                QMessageBox.information(self,"Download Error","Try Again..\nSomething wen't wrong")
                return
                
            QMessageBox.information(self,"Download Complete","Download Completed Successfully")
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.progressBar_2.setValue(0)
            self.label_5.setText('')
        
    
    def Video_Progress(self,total,received,ratio,rate,time):
        read_data = received
        if total > 0:
            download_percent = read_data*100/total
            self.progressBar_2.setValue(download_percent)
            remaining_time = round(time/60,2)
            self.label_5.setText(str("{} remaining time".format(remaining_time)))
            QApplication.processEvents()
            
####            Youtube Playlists             #####

    def Playlist_Download(self):
        playlist_url = self.lineEdit_5.text()
        save_location = self.lineEdit_6.text()
        if playlist_url=='' or save_location=='':
            QMessageBox.warning(self,"Data Error","Provide a Valid Playlist URL or Save Location")
        else:
            playlist=pafy.get_playlist(playlist_url)
            playlist_video=playlist['items']
            self.lcdNumber_2.display(len(playlist_video))
            
        os.chdir(save_location)
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))
        
        current_video_in_download=1
        quality=self.comboBox_2.currentIndex()
        QApplication.processEvents()
        
        for video in playlist_video:
            current_video=video['pafy']
            current_video_stream=current_video.videostreams
            self.lcdNumber.display(current_video_in_download)
            download=current_video_stream[quality].download(callback=self.Playlist_Progress)
            current_video_in_download+=1
            
    
    def Playlist_Progress(self,total,received,ratio,rate,time):
        read_data = received
        if total > 0:
            download_percent = read_data*100/total
            self.progressBar_3.setValue(download_percent)
            remaining_time = round(time/60,2)
            self.label_6.setText(str("{} remaining time".format(remaining_time)))
            QApplication.processEvents()
           
    def Playlist_Save_Browse(self):
        playlist_save_location = QFileDialog.getExistingDirectory(self,"Select Download Directory")
        self.lineEdit_6.setText(playlist_save_location)
        
########################### UI Changes Method  ###############################

    def Open_Home(self):
        self.tabWidget.setCurrentIndex(0)
    
    def Open_Download(self):
        self.tabWidget.setCurrentIndex(1)
    
    def Open_Youtube(self):
        self.tabWidget.setCurrentIndex(2)
    
    def Open_Setting(self):
        self.tabWidget.setCurrentIndex(3)
        
############ APP THEMES #################
    
    def Apply_DarkBlue_Style(self):
        style = open("themes/darkblue.css",'r')
        style = style.read()
        self.setStyleSheet(style)
    
    def Apply_DarkOrange_Style(self):
        style = open("themes/darkorange.css",'r')
        style = style.read()
        self.setStyleSheet(style)
    
    def Apply_Dark_Style(self):
        style = open("themes/darkstyle.css",'r')
        style = style.read()
        self.setStyleSheet(style)
    
    def Apply_Amoled_Style(self):
        style = open("themes/amoled.css",'r')
        style = style.read()
        self.setStyleSheet(style)
        
######### APP Animation ################

    def Move_Box_1(self):
        box_animation = QPropertyAnimation(self.groupBox,b"geometry")
        box_animation.setDuration(1000)
        box_animation.setStartValue(QRect(0,0,0,0))
        box_animation.setEndValue(QRect(20,20,281,161))
        box_animation.start()
        self.box_animation = box_animation
        
    def Move_Box_2(self):
        box_animation2 = QPropertyAnimation(self.groupBox_2,b"geometry")
        box_animation2.setDuration(1000)
        box_animation2.setStartValue(QRect(0,0,0,0))
        box_animation2.setEndValue(QRect(320,20,281,161))
        box_animation2.start()
        self.box_animation2 = box_animation2
        
    def Move_Box_3(self):
        box_animation3 = QPropertyAnimation(self.groupBox_3,b"geometry")
        box_animation3.setDuration(1000)
        box_animation3.setStartValue(QRect(0,0,0,0))
        box_animation3.setEndValue(QRect(20,200,281,161))
        box_animation3.start()
        self.box_animation3 = box_animation3
        
    def Move_Box_4(self):
        box_animation4 = QPropertyAnimation(self.groupBox_4,b"geometry")
        box_animation4.setDuration(1000)
        box_animation4.setStartValue(QRect(0,0,0,0))
        box_animation4.setEndValue(QRect(320,200,281,161))
        box_animation4.start()
        self.box_animation4 = box_animation4
    






def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()
    
if __name__=='__main__':
    main()