#!/usr/bin/env python3


# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from api.testcollabapi import TestCollabApiService
from api.testlinkapi import TestlinkApiService



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 711, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tabTestCaseEditor = QtWidgets.QWidget()
        self.tabTestCaseEditor.setObjectName("tabTestCaseEditor")

        # Button search test case by title
        self.pbSearch = QtWidgets.QPushButton(self.tabTestCaseEditor)
        self.pbSearch.setGeometry(QtCore.QRect(600, 30, 101, 25))
        self.pbSearch.setObjectName("pbSearch")
        self.pbSearch.clicked.connect(self.searchTestCaseClicked)

        self.leTestlinkId = QtWidgets.QLineEdit(self.tabTestCaseEditor)
        self.leTestlinkId.setGeometry(QtCore.QRect(360, 30, 231, 25))
        self.leTestlinkId.setObjectName("leTestlinkId")
        self.lblTestlinkId = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblTestlinkId.setGeometry(QtCore.QRect(360, 10, 131, 17))
        self.lblTestlinkId.setObjectName("lblTestlinkId")
        self.leTestCaseName = QtWidgets.QLineEdit(self.tabTestCaseEditor)
        self.leTestCaseName.setGeometry(QtCore.QRect(10, 30, 341, 25))
        self.leTestCaseName.setObjectName("leTestCaseName")
        self.lblTestCaseName = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblTestCaseName.setGeometry(QtCore.QRect(10, 10, 151, 17))
        self.lblTestCaseName.setObjectName("lblTestCaseName")
        self.lblSteps = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblSteps.setGeometry(QtCore.QRect(10, 140, 31, 17))
        self.lblSteps.setObjectName("lblSteps")
        self.lblExpectedResults = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblExpectedResults.setGeometry(QtCore.QRect(360, 140, 111, 17))
        self.lblExpectedResults.setObjectName("lblExpectedResults")
        self.pteSteps = QtWidgets.QPlainTextEdit(self.tabTestCaseEditor)
        self.pteSteps.setGeometry(QtCore.QRect(10, 160, 341, 221))
        self.pteSteps.setObjectName("pteSteps")
        self.pteExpectedResults = QtWidgets.QPlainTextEdit(self.tabTestCaseEditor)
        self.pteExpectedResults.setGeometry(QtCore.QRect(360, 160, 341, 221))
        self.pteExpectedResults.setObjectName("pteExpectedResults")
        self.lblPreconditions = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblPreconditions.setGeometry(QtCore.QRect(10, 390, 91, 17))
        self.lblPreconditions.setObjectName("lblPreconditions")
        self.lblAcceptanceCriteria = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblAcceptanceCriteria.setGeometry(QtCore.QRect(360, 390, 121, 17))
        self.lblAcceptanceCriteria.setObjectName("lblAcceptanceCriteria")
        self.ptePreconditions = QtWidgets.QPlainTextEdit(self.tabTestCaseEditor)
        self.ptePreconditions.setGeometry(QtCore.QRect(10, 410, 341, 51))
        self.ptePreconditions.setObjectName("ptePreconditions")
        self.pteAcceptanceCriteria = QtWidgets.QPlainTextEdit(self.tabTestCaseEditor)
        self.pteAcceptanceCriteria.setGeometry(QtCore.QRect(360, 410, 341, 51))
        self.pteAcceptanceCriteria.setObjectName("pteAcceptanceCriteria")

        # Button sync testlink
        self.pbSyncTestlink = QtWidgets.QPushButton(self.tabTestCaseEditor)
        self.pbSyncTestlink.setGeometry(QtCore.QRect(120, 470, 91, 25))
        self.pbSyncTestlink.setObjectName("pbSyncTestlink")
        self.pbSyncTestlink.clicked.connect(self.updateTestlink)

        # Button Sync TestCollab
        self.pbSyncTestCollab = QtWidgets.QPushButton(self.tabTestCaseEditor)
        self.pbSyncTestCollab.setGeometry(QtCore.QRect(10, 470, 101, 25))
        self.pbSyncTestCollab.setObjectName("pbSyncTestCollab")
        self.pbSyncTestCollab.clicked.connect(self.updateTestCollab)

        self.pteDescription = QtWidgets.QPlainTextEdit(self.tabTestCaseEditor)
        self.pteDescription.setGeometry(QtCore.QRect(10, 80, 691, 51))
        self.pteDescription.setObjectName("pteDescription")
        self.lblDescription = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblDescription.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.lblDescription.setObjectName("lblDescription")

        # Label sync status
        self.lblSyncStatus = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblSyncStatus.setGeometry(QtCore.QRect(220, 470, 81, 21))
        self.lblSyncStatus.setObjectName("lblSyncStatus")
        self.lblSyncStatus.setStyleSheet('color: green')

        self.tabWidget.addTab(self.tabTestCaseEditor, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.gbTestlink = QtWidgets.QGroupBox(self.tabSettings)
        self.gbTestlink.setGeometry(QtCore.QRect(10, 10, 321, 161))
        self.gbTestlink.setObjectName("gbTestlink")
        self.cbTeslinkProjects = QtWidgets.QComboBox(self.gbTestlink)
        self.cbTeslinkProjects.setGeometry(QtCore.QRect(10, 50, 301, 25))
        self.cbTeslinkProjects.setObjectName("cbTeslinkProjects")
        self.lblTestlinkProject = QtWidgets.QLabel(self.gbTestlink)
        self.lblTestlinkProject.setGeometry(QtCore.QRect(10, 30, 81, 17))
        self.lblTestlinkProject.setObjectName("lblTestlinkProject")
        self.gbTestCollab = QtWidgets.QGroupBox(self.tabSettings)
        self.gbTestCollab.setGeometry(QtCore.QRect(350, 10, 341, 161))
        self.gbTestCollab.setObjectName("gbTestCollab")
        self.cbTestCollabProjects = QtWidgets.QComboBox(self.gbTestCollab)
        self.cbTestCollabProjects.setGeometry(QtCore.QRect(10, 50, 321, 25))
        self.cbTestCollabProjects.setObjectName("cbTestCollabProjects")
        self.lblTestCollabProject = QtWidgets.QLabel(self.gbTestCollab)
        self.lblTestCollabProject.setGeometry(QtCore.QRect(10, 30, 71, 17))
        self.lblTestCollabProject.setObjectName("lblTestCollabProject")

        # Button save settings
        self.pbSaveSettings = QtWidgets.QPushButton(self.tabSettings)
        self.pbSaveSettings.setGeometry(QtCore.QRect(100, 460, 80, 25))
        self.pbSaveSettings.setObjectName("pbSaveSettings")
        self.pbSaveSettings.clicked.connect(self.saveSelectedProjects)

        # Load button
        self.pbLoad = QtWidgets.QPushButton(self.tabSettings)
        self.pbLoad.setGeometry(QtCore.QRect(10, 460, 80, 25))
        self.pbLoad.setObjectName("pbLoad")
        self.pbLoad.clicked.connect(self.loadSettingsTab)

        # Label settings status
        self.lblStatusSettings = QtWidgets.QLabel(self.tabSettings)
        self.lblStatusSettings.setGeometry(QtCore.QRect(200, 456, 101, 31))
        self.lblStatusSettings.setObjectName("lblStatusSettings")
        self.lblStatusSettings.setStyleSheet('color: green')

        self.tabWidget.addTab(self.tabSettings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QA - Test Case Sync Viewer"))
        self.pbSearch.setText(_translate("MainWindow", "Search"))
        self.lblTestlinkId.setText(_translate("MainWindow", "Teslink External ID"))
        self.lblTestCaseName.setText(_translate("MainWindow", "Teste Case Name"))
        self.lblSteps.setText(_translate("MainWindow", "Steps"))
        self.lblExpectedResults.setText(_translate("MainWindow", "Expected results"))
        self.lblPreconditions.setText(_translate("MainWindow", "Preconditions"))
        self.lblAcceptanceCriteria.setText(_translate("MainWindow", "Acceptance Criteria"))
        self.pbSyncTestlink.setText(_translate("MainWindow", "Sync TestLink"))
        self.pbSyncTestCollab.setText(_translate("MainWindow", "Sync TestCollab"))
        self.lblDescription.setText(_translate("MainWindow", "Description"))
        self.lblSyncStatus.setText(_translate("MainWindow", "Not Sync Yet !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTestCaseEditor),
                                  _translate("MainWindow", "Test Case Editor"))
        self.gbTestlink.setTitle(_translate("MainWindow", "Testlink Settings"))
        self.lblTestlinkProject.setText(_translate("MainWindow", "Test Project"))
        self.gbTestCollab.setTitle(_translate("MainWindow", "TestCollab Settings"))
        self.lblTestCollabProject.setText(_translate("MainWindow", "Test Project"))
        self.pbSaveSettings.setText(_translate("MainWindow", "Save"))
        self.pbLoad.setText(_translate("MainWindow", "Load"))
        self.lblStatusSettings.setText(_translate("MainWindow", "Not Loaded Yet !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Settings"))

    def loadSettingsTab(self):
        self.setStatusSettings('Loading ...')
        self.testlinkApi = TestlinkApiService()
        self.testcollabApi = TestCollabApiService()
        projects = self.testcollabApi.getProjects()
        for data in projects:
            id = data['Project']['id']
            name = data['Project']['name']
            self.cbTestCollabProjects.addItem('{0}-{1}'.format(id, name))
        projects = self.testlinkApi.getProjects()
        for project in projects:
            prefix = project['prefix']
            name = project['name']
            self.cbTeslinkProjects.addItem('{0}-{1}'.format(prefix, name))
        self.setStatusSettings('Loaded!')

    def saveSelectedProjects(self):
        testCollabValue = self.cbTestCollabProjects.currentText()
        testlinkValue = self.cbTeslinkProjects.currentText()
        print('Testcollab: ', testCollabValue)
        print('Testlink: ', testlinkValue)
        self.testcollabApi.setProjectId(testCollabValue.split('-')[0])
        self.testlinkApi.setPrefix(testlinkValue.split('-')[0])
        self.setStatusSettings('Settings Saved!')

    def searchTestCaseClicked(self):
        try:
            query = self.leTestCaseName.text()
            test_case = self.testcollabApi.getTestCaseByTitle(query)
            self.loadTestCase(test_case)
            self.leTestlinkId.setText(self.testlinkApi.getTestCaseIDByName(query))
            self.setStatusSync('Not sync yet!')
        except AttributeError as err:
            print(err)
            self.setStatusSync('Err, no settings loaded!')


    def loadTestCase(self, data):
        try:
            test_case = data['data']['testCases'][0]
            self.testCaseId = test_case['id']
            self.suiteId = test_case['suite_id']
            self.title = test_case['title']
            self.description = test_case['description']
            self.steps = test_case['steps']
            self.expectedResults = test_case['expected_result']
            self.pteSteps.textCursor().insertText(self.steps)
            self.pteExpectedResults.textCursor().insertText(self.expectedResults)
            self.pteDescription.textCursor().insertText(self.description)
        except:
            print('err load test case: ', data)

    def getFormData(self):
        self.title = self.leTestCaseName.text()
        self.description = self.pteDescription.toPlainText()
        self.steps = self.pteSteps.toPlainText()
        self.expectedResults = self.pteExpectedResults.toPlainText()
        self.criteria = self.pteAcceptanceCriteria.toPlainText()
        self.preconditions = self.ptePreconditions.toPlainText()
        self.testlinkId = self.leTestlinkId.text()

    def updateTestlink(self):
        self.getFormData()
        self.setStatusSync('Updating ...')
        data = {
            'testcasename': self.title,
            'summary': self.description,
            'actions': self.steps.split('\n\n'),
            'results': self.expectedResults.split('\n\n'),
            'preconditions': self.preconditions,
            'externalid': self.testlinkId
        }
        self.testlinkApi.updateTestCase(data)
        self.clearForm()
        self.setStatusSync('Sync Testlink ... Ok!')

    def updateTestCollab(self):
        self.getFormData()
        self.setStatusSync('Updating ...')
        data = {"data": {"TestCase": {}}}
        data["data"]["TestCase"]["suite_id"] = self.suiteId
        data["data"]["TestCase"]["title"] = self.title
        data["data"]["TestCase"]["description"] = self.description
        data["data"]["TestCase"]["steps"] = self.steps
        data["data"]["TestCase"]["expected_result"] = self.expectedResults
        data["data"]["TestCase"]["priority"] = 1
        data["data"]["TestCase"]["criteria"] = self.criteria
        data["data"]["TestCase"]["preconditions"] = self.preconditions
        data["data"]["TestCase"]["testlinkid"] = self.testlinkId

        self.testcollabApi.setTestCaseId(self.testCaseId)
        self.testcollabApi.setSuiteId(self.suiteId)
        self.testcollabApi.updateTestCase(data)
        self.setStatusSync('Sync TestCollab ... Ok!')


    def clearForm(self):
        self.pteSteps.clear()
        self.ptePreconditions.clear()
        self.pteDescription.clear()
        self.pteExpectedResults.clear()
        self.leTestlinkId.clear()
        self.leTestCaseName.clear()
        self.leTestCaseName.clear()
        self.pteAcceptanceCriteria.clear()

    def setStatusSettings(self, status):
        self.lblStatusSettings.setText(status)

    def setStatusSync(self, status):
        self.lblSyncStatus.setText(status)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())