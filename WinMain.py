#coding=utf8
import sys,os
import time
import re
import xlrd
import json
import codecs
import ConfigParser
import urllib2
import win32com.client
import requests
import random
from PyQt4 import QtCore,QtGui,QtNetwork
from PyQt4.QtCore import SIGNAL  
from PyQt4.QtGui import QFileDialog, QDialog, QApplication, QWidget,QPushButton, QLabel, QLineEdit, QHBoxLayout, QFormLayout  
from PyQt4.QtCore import QDir
from Form_Main import Ui_Form
from GetTK import *
from Global import *

reload(sys)
sys.setdefaultencoding('utf-8')
class RunThread(QtCore.QThread):
    #把打印的字符串发送给UI主线程
    signal_text= QtCore.pyqtSignal(str,bool) # 信号
    signal_end = QtCore.pyqtSignal() # 测试完成后终止信号
    def __init__(self, parent=None):
        super(RunThread, self).__init__(parent)
        #获取主UI线程的obj
        self.parent = parent
        self.start_flag = 0
    def start_test(self):
        self.fd = codecs.open(self.parent.logfile,"a+","utf-8")
        self.start()
    def stop_test(self):
        self.fd.close()
        self.terminate()
        self.wait()
        # self.quit()
    def writelog(self,msg):
        # fd = codecs.open(self.parent.logfile,"a+","utf-8")
        self.fd.write(msg)
        self.fd.write("\r\n")
        self.fd.flush()
    def run(self):
        #循环父节点的字典
        for k,v in self.parent.exceldict.iteritems():
            for key,value in v.iteritems():
                lang = self.parent.py2js.translate(value)
                msg = "expe:%s fact:%s------{" %(k,lang)+value
                msg = msg +"}"
                if k in lang:
                    self.signal_text.emit(msg,True)
                else:
                    googlefact = self.parent.py2js.translate(value,k)
                    msg = msg+" {"+googlefact+"}"
                    if googlefact == value:
                        continue
                    self.writelog(msg)
                    self.signal_text.emit(msg,False)
        self.signal_end.emit()
class PyToJs():
    def chklanguage(self,flag,*langjson):
        if not flag:
            try:
                if langjson[-1][-1][-1] in languagelist:
                    return " " .join(langjson[-1][-1])
                elif langjson[2] in languagelist:
                    return langjson[2]
                elif langjson[8][0][0] in languagelist:
                    return langjson[8][0][0]
                elif langjson[8][3][0] in languagelist:
                    return langjson[8][3][0]
                else:
                    return str(langjson)
            except Exception,e:
                print str(e)
                return "error"
        else:
            try:
                if langjson[0][0][0]:
                    return langjson[0][0][0]
            except Exception,e:
                print str(e)
                return "error"
    def translate(self,content,tolang=""):
        if not content.strip():
            return True
        if isinstance(content, unicode):
            content = content.encode("UTF-8")
        filename = os.path.join(path,"cacert.pem")
        headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}
        for x in xrange(5):
            try:
                tk = getTk(content)
                content = urllib2.quote(content)
                if tolang:
                    url = u"""https://translate.google.cn/translate_a/single?client=t&sl=auto&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&pc=1&otf=1&ssel=0&tsel=0&kc=1&tk=""" %(tolang)+tk+"""&q="""+content
                else:
                    url = u"""https://translate.google.cn/translate_a/single?client=t&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&pc=1&otf=1&ssel=0&tsel=0&kc=1&tk="""+tk+"""&q="""+content
                result = requests.get(url,headers=headers, verify=filename)
                # print repr(result.content)
                if result.status_code == 200:
                    jsondict = json.loads(result.content)
                    return self.chklanguage(tolang,*jsondict)
            except Exception,e:
                print str(e)
                time.sleep(1)
        return "error"
class Form(QWidget):  
    def __init__(self, parent=None):  
        super(Form, self).__init__(parent)  
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.py2js = PyToJs()
        # self.py2js = Py4Js()
        self.connect(self.ui.cfgbutton, SIGNAL("clicked()"),self.select_cfgfile)  
        self.connect(self.ui.excelbutton, SIGNAL("clicked()"),self.select_excel)  
        self.connect(self.ui.startchk, SIGNAL("clicked()"),self.startchk)  
        self.setWindowTitle("Translate")
        self.rootdir = ""
        self.cfgflg = 0
        self.excelflag = 0
        self.runthread = RunThread(self)
        self.runthread.signal_text.connect(self.writelogmsg)
        self.runthread.signal_end.connect(self.test_end)
        self.runflag = 0
    def select_cfgfile(self):  
        # absolute_path is a QString object  
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file',   
            '.',"txt files (*.ini)")  
        if absolute_path:  
            relative_path = os.path.join(path,unicode(absolute_path)).replace("\\","/")  
            self.ui.config_file.setText(relative_path)  
            self.cfgfile=unicode(relative_path)
            self.cfgflg = 1
    def select_excel(self):  
        # absolute_path is a QString object  
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file',   
            '.',"xls files (*.xls*)")  
        if absolute_path:  
            relative_path = os.path.join(path,unicode(absolute_path)).replace("\\","/")  
            self.ui.excelfile.setText(relative_path)  
            self.excelfile=unicode(relative_path)
            self.rootdir = os.path.dirname(self.excelfile)
            self.excelflag = 1
    def startchk(self):  
        # absolute_path is a QString object
        #按照年月日生成日志Logo
        if self.runflag:
            self.runthread.stop_test()
            self.ui.startchk.setText(u"开始检查")
            self.runflag = 0
            self.ui.statuslabel.setText(u"已停止检查")
        else:
            if self.excelflag != 1 and self.cfgflg != 1:
                QtGui.QMessageBox.information( self, "check config", u"请确认配置文件和Excel文件已经选择")
                return False
            self.exceldict = self.getexcel()
            now = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            log = now+".log"
            self.logfile = os.path.join(self.rootdir,log)
            self.ui.startchk.setText(u"停止检查")
            self.ui.statuslabel.setText(u"正在运行......")
            self.runflag = 1
            self.runthread.start_test()
    def writelogmsg(self,msg,flag):
        self.ui.logmsg.setText(msg)
    def test_end(self):
         QtGui.QMessageBox.information( self, "check end", u"测试完成")
    def parser_cfgfile(self):
        kargs={}
        cf = ConfigParser.ConfigParser()
        cf.read(self.cfgfile.replace("\\","/"))
        for opt in cf.sections():
            if opt:
                kargs[opt]={}
        for opt in kargs.keys():
            for k,v in cf.items(opt):
                kargs[opt][k]=v
        return kargs
    def getexcel(self):
        multi_dict = self.parser_cfgfile()
        filename=self.excelfile.replace("\\","/")
        data = xlrd.open_workbook(filename)
        table = data.sheets()[0]
        nrows = table.nrows
        dict_ret={}
        index = 1
        dictmap = {}
        excelDict = {}
        for i in range(66,91):
            dictmap[chr(i)] = index
            index = index+1
        for key,value in multi_dict['lang'].iteritems():
            excelDict[key] = {}
        for i in range(1,nrows):
            v=table.row_values(i)
            if v[0].strip():
                for key,value in multi_dict['lang'].iteritems():
                    excelDict[key][v[0]] = v[dictmap[multi_dict['lang'][key]]]
        return excelDict
if __name__ == "__main__":
    app = QApplication(sys.argv)  
    form = Form()  
    form.show()  
    app.exec_() 