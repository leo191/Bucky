from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QWizard, QWizardPage, QComboBox, QTreeView
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QStringListModel
import sys
import Util
from random import randint


def Cloning(li1):
    li_copy = [i for i in li1]
    return li_copy


class MagicWizard(QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.setWindowTitle("Bucky - Backup Infrastructure")
        self.setFixedSize(800, 700)


class Page1(QWizardPage):
    listinsids = []
    customer_lb = None
    selectedIDs = []
    unseletedIDs = []
    # model = None

    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        self.setTitle('Bucky')
        self.setSubTitle('Select profile of the customer you want to get backup')
        self.customer_lb = QtWidgets.QLabel(self)
        self.provider_cmbx = QComboBox(self)
        self.customer_cmbox = QComboBox(self)
        self.customer_list = Util.getProfiles() if Util.getProfiles() is not True else sys.exit(127)
        self.customer_cmbox.addItem("Select an account")
        self.customer_cmbox.addItems(self.customer_list)
        self.customer_lb.setText("Customer Account")
        self.checkAll_cb = QtWidgets.QCheckBox(self)
        self.listinstance_lv = QtWidgets.QListView(self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.customer_lb)
        layout.addWidget(self.customer_cmbox)
        layout.addWidget(self.checkAll_cb)
        layout.addWidget(self.listinstance_lv)
        self.provider_cmbx.currentTextChanged.connect(self.setaccount)
        self.customer_cmbox.currentTextChanged.connect(self.setList)
        self.checkAll_cb.stateChanged.connect(self.selectAll)
        self.setLayout(layout)




    def setaccount(self, provider):
        pass

    def selectAll(self, check):
        model = QStandardItemModel()
        print(self.listinsids)
        if self.listinsids:
            print(self.listinsids)
            print(self.selectedIDs, self.unseletedIDs)
            for instanceid in self.listinsids:
                item = QStandardItem('Instance %s' % instanceid)
                # check = Qt.Checked if randint(0, 1) == 1 else Qt.Unchecked
                item.setCheckState(check)
                item.setCheckable(True)
                item.setEditable(False)
                model.appendRow(item)
            model.itemChanged.connect(self.on_item_changed)
            self.listinstance_lv.setModel(model)
            self.listinstance_lv.show()
            print(self.listinsids)
            if check == Qt.Unchecked:
                self.unseletedIDs = Cloning(self.listinsids)
                self.selectedIDs.clear()
            else:
                self.selectedIDs = Cloning(self.listinsids)
                self.unseletedIDs.clear()
            print(self.listinsids, self.selectedIDs, self.unseletedIDs)

    def setList(self, text):
        if text != "Select an account":
            self.checkAll_cb.setCheckState(Qt.Unchecked)
            self.listinsids = Util.getAllInIds(text)
            print(self.listinsids)
            model = QStandardItemModel()
            for instanceid in self.listinsids:
                item = QStandardItem('Instance %s' % instanceid)
                # check = Qt.Checked if randint(0, 1) == 1 else Qt.Unchecked
                item.setCheckState(Qt.Unchecked)
                item.setCheckable(True)
                item.setEditable(False)
                model.appendRow(item) 
            self.listinstance_lv.setModel(model)
            self.listinstance_lv.show()
            self.selectedIDs.clear()
            self.unseletedIDs = Cloning(self.listinsids)

    def on_item_changed(self, item):
        # If the changed item is not checked, don't bother checking others
        print(item.checkState())
        print(self.selectedIDs, self.unseletedIDs)
        # sys.exit(0)
        if not item.checkState():
            self.unseletedIDs.append(item.text().split()[1])
            if item.text().split()[1] in self.selectedIDs:
                self.selectedIDs.remove(item.text().split()[1])
            print(self.selectedIDs, self.unseletedIDs)
        else:
            self.selectedIDs.append(item.text().split()[1])
            if item.text().split()[1] in self.unseletedIDs:
                self.unseletedIDs.remove(item.text().split()[1])
            print(self.selectedIDs, self.unseletedIDs)
        # loop through the items until you get None, which
        # means you've passed the end of the list
        # while self.model.item(i):
        #     if not self.model.item(i).checkState():
        #         return
        #     i += 1
    def get_selectedIds(self):
        return self.selectedIDs

        
class Page2(QWizardPage):
    timespan = ['Daily', 'Weekly', 'Yearly']
    timestamp = ['12:00', '12:30', '1:00', '1:30', '2:00',
                    '2:30', '3:00', '3:30', '4:00', '4:30', 
                    '5:00', '5:30', '6:00', '6:30', '7:00', 
                    '7:30', '8:00', '8:30', '9:00', '9:30', 
                    '10:00', '10:30', '11:00', '11:30']
    ap = ['AM', 'PM']
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    timez = []
    timespancmbox = None
    dayscmbox = None
    timecmbox = None
    ampm = None
    timezonecmbox = None
    model = None
    view = None

    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
        mainlayout = QVBoxLayout()
        timecontrolLay = QHBoxLayout()
        self.timespancmbox = QComboBox()
        self.dayscmbox = QComboBox()
        self.timecmbox = QComboBox()
        self.ampm = QComboBox()
        self.timezonecmbox = QComboBox()
        self.timespancmbox.addItems(self.timespan)
        self.dayscmbox.addItems(self.day)
        self.timecmbox.addItems(self.timestamp)
        self.ampm.addItems(self.ap)
        self.dayscmbox.hide()
        self.timezonecmbox.addItems(self.timez)
        self.view = QTreeView()
        timecontrolLay.addWidget(self.timespancmbox)
        timecontrolLay.addWidget(self.dayscmbox)
        timecontrolLay.addWidget(self.timecmbox)
        timecontrolLay.addWidget(self.ampm)
        mainlayout.addLayout(timecontrolLay)
        mainlayout.addWidget(self.view)
        self.setLayout(mainlayout)
        self.timespancmbox.currentTextChanged.connect(self.showdays)
        

    def showdays(self, text):
        if text == "Weekly":
            self.dayscmbox.show()
        elif text == "Daily":
            self.dayscmbox.hide()
    
    def init_allVol(self, volumes_of_instances):
        print(volumes_of_instances)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['instance and related voloumns'])
        self.view.setModel(self.model)
        self.view.setUniformRowHeights(True)
        for key, value in volumes_of_instances.items():
            parent1 = QStandardItem(key)
            for v in value:
                vol = QStandardItem(v)
                vol.setCheckState(Qt.Unchecked)
                vol.setCheckable(True)
                vol.setEditable(False)
                parent1.appendRow(vol)
            self.model.appendRow(parent1)
        self.view.show()
        self.model.itemChanged.connect(self.check_vol)
        

    def check_vol(self, item):
        print(item.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)

    wizard = MagicWizard()
    # wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
    page1 = Page1()
    page2 = Page2()
    nxt = wizard.button(QtWidgets.QWizard.NextButton)
    func = lambda:page2.init_allVol(Util.get_instance_volumes(page1.get_selectedIds()))
    nxt.clicked.connect(func)

    wizard.addPage(page1)
    wizard.addPage(page2)
    wizard.show()

    sys.exit(app.exec_())
