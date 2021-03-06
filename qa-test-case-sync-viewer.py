#!/usr/bin/env python3


# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from api.testcollabapi import TestCollabApiService
from api.testlinkapi import TestlinkApiService


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 891, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tabTestCaseEditor = QtWidgets.QWidget()
        self.tabTestCaseEditor.setObjectName("tabTestCaseEditor")

        # button Search test case by name
        self.pbSearch = QtWidgets.QPushButton(self.tabTestCaseEditor)
        self.pbSearch.setGeometry(QtCore.QRect(600, 30, 101, 25))
        self.pbSearch.setObjectName("pbSearch")
        self.pbSearch.clicked.connect(self.searchTestCaseClicked)

        # line editor testlink id
        self.leTestlinkId = QtWidgets.QLineEdit(self.tabTestCaseEditor)
        self.leTestlinkId.setGeometry(QtCore.QRect(360, 30, 231, 25))
        self.leTestlinkId.setObjectName("leTestlinkId")

        self.lblTestlinkId = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.lblTestlinkId.setGeometry(QtCore.QRect(360, 10, 131, 17))
        self.lblTestlinkId.setObjectName("lblTestlinkId")

        # Line editor test case name
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

        # Button sync testcollab
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
        self.lblSyncStatus.setGeometry(QtCore.QRect(220, 470, 111, 21))
        self.lblSyncStatus.setObjectName("lblSyncStatus")
        self.lblSyncStatus.setStyleSheet('color: green')

        self.pbClear = QtWidgets.QPushButton(self.tabTestCaseEditor)
        self.pbClear.setGeometry(QtCore.QRect(530, 470, 80, 25))
        self.pbClear.setObjectName("pbClear")

        # Button replace text into action and results
        self.pbReplace = QtWidgets.QPushButton(self.tabTestCaseEditor)
        self.pbReplace.setGeometry(QtCore.QRect(710, 350, 161, 25))
        self.pbReplace.setObjectName("pbReplace")
        self.pbReplace.clicked.connect(self.replace)

        self.leSearchFor = QtWidgets.QLineEdit(self.tabTestCaseEditor)
        self.leSearchFor.setGeometry(QtCore.QRect(710, 180, 161, 25))
        self.leSearchFor.setObjectName("leSearchFor")
        self.leReplaceWith = QtWidgets.QLineEdit(self.tabTestCaseEditor)
        self.leReplaceWith.setGeometry(QtCore.QRect(710, 240, 161, 25))
        self.leReplaceWith.setObjectName("leReplaceWith")
        self.label_5 = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.label_5.setGeometry(QtCore.QRect(710, 160, 71, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tabTestCaseEditor)
        self.label_6.setGeometry(QtCore.QRect(710, 220, 81, 17))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.tabTestCaseEditor)
        self.pushButton.setGeometry(QtCore.QRect(620, 470, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tabTestCaseEditor, "")
        self.tabReport = QtWidgets.QWidget()
        self.tabReport.setObjectName("tabReport")

        # QList tests
        self.lwTests = QtWidgets.QListWidget(self.tabReport)
        self.lwTests.setGeometry(QtCore.QRect(10, 40, 691, 421))
        self.lwTests.setObjectName("lwTests")
        self.lwTests.itemClicked.connect(self.onSelectTestCase)

        self.pbPass = QtWidgets.QPushButton(self.tabReport)
        self.pbPass.setGeometry(QtCore.QRect(10, 470, 80, 25))
        self.pbPass.setObjectName("pbPass")
        self.pbFail = QtWidgets.QPushButton(self.tabReport)
        self.pbFail.setGeometry(QtCore.QRect(100, 470, 80, 25))
        self.pbFail.setObjectName("pbFail")
        self.pbBlock = QtWidgets.QPushButton(self.tabReport)
        self.pbBlock.setGeometry(QtCore.QRect(190, 470, 80, 25))
        self.pbBlock.setObjectName("pbBlock")
        self.chboxNotRun = QtWidgets.QCheckBox(self.tabReport)
        self.chboxNotRun.setGeometry(QtCore.QRect(10, 11, 82, 20))
        self.chboxNotRun.setObjectName("chboxNotRun")
        self.chboxFailed = QtWidgets.QCheckBox(self.tabReport)
        self.chboxFailed.setGeometry(QtCore.QRect(100, 11, 61, 20))
        self.chboxFailed.setObjectName("chboxFailed")
        self.chboxPassed = QtWidgets.QCheckBox(self.tabReport)
        self.chboxPassed.setGeometry(QtCore.QRect(180, 10, 71, 20))
        self.chboxPassed.setObjectName("chboxPassed")
        self.chboxBlocked = QtWidgets.QCheckBox(self.tabReport)
        self.chboxBlocked.setGeometry(QtCore.QRect(270, 10, 82, 23))
        self.chboxBlocked.setObjectName("chboxBlocked")

        # Edit push button
        self.pbEdit = QtWidgets.QPushButton(self.tabReport)
        self.pbEdit.setGeometry(QtCore.QRect(620, 470, 80, 25))
        self.pbEdit.setObjectName("pbEdit")
        self.pbEdit.clicked.connect(self.onEditTestCase)

        self.lblTotalTestCases = QtWidgets.QLabel(self.tabReport)
        self.lblTotalTestCases.setGeometry(QtCore.QRect(710, 40, 151, 17))
        self.lblTotalTestCases.setObjectName("lblTotalTestCases")
        self.lblNotRun = QtWidgets.QLabel(self.tabReport)
        self.lblNotRun.setGeometry(QtCore.QRect(710, 70, 161, 17))
        self.lblNotRun.setObjectName("lblNotRun")
        self.lblPassed = QtWidgets.QLabel(self.tabReport)
        self.lblPassed.setGeometry(QtCore.QRect(710, 100, 171, 17))
        self.lblPassed.setObjectName("lblPassed")
        self.lblFailed = QtWidgets.QLabel(self.tabReport)
        self.lblFailed.setGeometry(QtCore.QRect(710, 130, 161, 17))
        self.lblFailed.setObjectName("lblFailed")
        self.lblBlocked = QtWidgets.QLabel(self.tabReport)
        self.lblBlocked.setGeometry(QtCore.QRect(710, 160, 171, 17))
        self.lblBlocked.setObjectName("lblBlocked")

        self.tabWidget.addTab(self.tabReport, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.gbTestlink = QtWidgets.QGroupBox(self.tabSettings)
        self.gbTestlink.setGeometry(QtCore.QRect(10, 10, 321, 431))
        self.gbTestlink.setObjectName("gbTestlink")

        # Combobox testlink projects
        self.cbTeslinkProjects = QtWidgets.QComboBox(self.gbTestlink)
        self.cbTeslinkProjects.setGeometry(QtCore.QRect(10, 50, 301, 25))
        self.cbTeslinkProjects.setObjectName("cbTeslinkProjects")
        self.cbTeslinkProjects.currentTextChanged.connect(self.onProjectChanged)

        self.lblTestlinkProject = QtWidgets.QLabel(self.gbTestlink)
        self.lblTestlinkProject.setGeometry(QtCore.QRect(10, 30, 81, 17))
        self.lblTestlinkProject.setObjectName("lblTestlinkProject")
        self.lblTestlinkPlan = QtWidgets.QLabel(self.gbTestlink)
        self.lblTestlinkPlan.setGeometry(QtCore.QRect(10, 90, 54, 17))
        self.lblTestlinkPlan.setObjectName("lblTestlinkPlan")
        self.lblTestlinkPlatform = QtWidgets.QLabel(self.gbTestlink)
        self.lblTestlinkPlatform.setGeometry(QtCore.QRect(10, 150, 54, 17))
        self.lblTestlinkPlatform.setObjectName("lblTestlinkPlatform")
        self.lblTestlinkBuild = QtWidgets.QLabel(self.gbTestlink)
        self.lblTestlinkBuild.setGeometry(QtCore.QRect(10, 210, 31, 17))
        self.lblTestlinkBuild.setObjectName("lblTestlinkBuild")

        # combobox plans
        self.cbTestlinkPlans = QtWidgets.QComboBox(self.gbTestlink)
        self.cbTestlinkPlans.setGeometry(QtCore.QRect(10, 110, 301, 25))
        self.cbTestlinkPlans.setObjectName("cbTestlinkPlans")
        self.cbTestlinkPlans.currentTextChanged.connect(self.onPlanChanged)

        # Combobox platforms
        self.cbTestlinkPlatforms = QtWidgets.QComboBox(self.gbTestlink)
        self.cbTestlinkPlatforms.setGeometry(QtCore.QRect(10, 170, 301, 25))
        self.cbTestlinkPlatforms.setObjectName("cbTestlinkPlatforms")
        self.cbTestlinkPlatforms.currentTextChanged.connect(self.onPlatformChanged)

        # Combobox builds
        self.cbTestlinkBuilds = QtWidgets.QComboBox(self.gbTestlink)
        self.cbTestlinkBuilds.setGeometry(QtCore.QRect(10, 230, 301, 25))
        self.cbTestlinkBuilds.setObjectName("cbTestlinkBuilds")

        # Combobox suites
        self.cbTestlinkTopSuites = QtWidgets.QComboBox(self.gbTestlink)
        self.cbTestlinkTopSuites.setGeometry(QtCore.QRect(10, 290, 301, 25))
        self.cbTestlinkTopSuites.setObjectName("cbTestlinkTopSuites")

        self.label = QtWidgets.QLabel(self.gbTestlink)
        self.label.setGeometry(QtCore.QRect(10, 270, 131, 17))
        self.label.setObjectName("label")
        self.gbTestCollab = QtWidgets.QGroupBox(self.tabSettings)
        self.gbTestCollab.setGeometry(QtCore.QRect(350, 10, 341, 431))
        self.gbTestCollab.setObjectName("gbTestCollab")

        # combobox testcollab project
        self.cbTestCollabProjects = QtWidgets.QComboBox(self.gbTestCollab)
        self.cbTestCollabProjects.setGeometry(QtCore.QRect(10, 50, 321, 25))
        self.cbTestCollabProjects.setObjectName("cbTestCollabProjects")
        self.lblTestCollabProject = QtWidgets.QLabel(self.gbTestCollab)
        self.lblTestCollabProject.setGeometry(QtCore.QRect(10, 30, 71, 17))
        self.lblTestCollabProject.setObjectName("lblTestCollabProject")

        # combobox unknown
        self.comboBox_4 = QtWidgets.QComboBox(self.gbTestCollab)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 110, 321, 25))
        self.comboBox_4.setObjectName("comboBox_4")

        self.lblTestCollabSuite = QtWidgets.QLabel(self.gbTestCollab)
        self.lblTestCollabSuite.setGeometry(QtCore.QRect(10, 90, 54, 17))
        self.lblTestCollabSuite.setObjectName("lblTestCollabSuite")

        # Button Save Settings
        self.pbSaveSettings = QtWidgets.QPushButton(self.tabSettings)
        self.pbSaveSettings.setGeometry(QtCore.QRect(100, 460, 80, 25))
        self.pbSaveSettings.setObjectName("pbSaveSettings")
        self.pbSaveSettings.clicked.connect(self.saveSelectedProjects)

        # Button load settings
        self.pbLoad = QtWidgets.QPushButton(self.tabSettings)
        self.pbLoad.setGeometry(QtCore.QRect(10, 460, 80, 25))
        self.pbLoad.setObjectName("pbLoad")
        self.pbLoad.clicked.connect(self.loadSettingsTab)

        # Label status settings
        self.lblStatusSettings = QtWidgets.QLabel(self.tabSettings)
        self.lblStatusSettings.setGeometry(QtCore.QRect(200, 456, 131, 31))
        self.lblStatusSettings.setObjectName("lblStatusSettings")
        self.lblStatusSettings.setStyleSheet('color: green')

        self.tabWidget.addTab(self.tabSettings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
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
        self.pbClear.setText(_translate("MainWindow", "Clear"))
        self.pbReplace.setText(_translate("MainWindow", "Replace"))
        self.label_5.setText(_translate("MainWindow", "Search for:"))
        self.label_6.setText(_translate("MainWindow", "Replace with:"))
        self.pushButton.setText(_translate("MainWindow", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTestCaseEditor), _translate("MainWindow", "Test Case Editor"))
        self.pbPass.setText(_translate("MainWindow", "Pass"))
        self.pbFail.setText(_translate("MainWindow", "Fail"))
        self.pbBlock.setText(_translate("MainWindow", "Block"))
        self.chboxNotRun.setText(_translate("MainWindow", "Not Run"))
        self.chboxFailed.setText(_translate("MainWindow", "Failed"))
        self.chboxPassed.setText(_translate("MainWindow", "Passed"))
        self.chboxBlocked.setText(_translate("MainWindow", "Blocked"))
        self.pbEdit.setText(_translate("MainWindow", "Edit "))
        self.lblTotalTestCases.setText(_translate("MainWindow", "Total Test Case: 0"))
        self.lblNotRun.setText(_translate("MainWindow", "Not run: 0"))
        self.lblPassed.setText(_translate("MainWindow", "Passed: 0 "))
        self.lblFailed.setText(_translate("MainWindow", "Failed: 0"))
        self.lblBlocked.setText(_translate("MainWindow", "Blocked: 0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabReport), _translate("MainWindow", "Report"))
        self.gbTestlink.setTitle(_translate("MainWindow", "Testlink Settings"))
        self.lblTestlinkProject.setText(_translate("MainWindow", "Test Project"))
        self.lblTestlinkPlan.setText(_translate("MainWindow", "Test Plan"))
        self.lblTestlinkPlatform.setText(_translate("MainWindow", "Platform"))
        self.lblTestlinkBuild.setText(_translate("MainWindow", "Build"))
        self.label.setText(_translate("MainWindow", "Top Level Test Suite"))
        self.gbTestCollab.setTitle(_translate("MainWindow", "TestCollab Settings"))
        self.lblTestCollabProject.setText(_translate("MainWindow", "Test Project"))
        self.lblTestCollabSuite.setText(_translate("MainWindow", "Test Suite"))
        self.pbSaveSettings.setText(_translate("MainWindow", "Save"))
        self.pbLoad.setText(_translate("MainWindow", "Load"))
        self.lblStatusSettings.setText(_translate("MainWindow", "Not Loaded Yet !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Settings"))

    def loadSettingsTab(self):
        self.setStatusSettings('Loading...')
        self.testlinkApi = TestlinkApiService()
        self.testcollabApi = TestCollabApiService()
        projects = self.testcollabApi.getProjects()
        self.cbTeslinkProjects.clear()
        self.cbTestCollabProjects.clear()
        for data in projects:
            id = data['Project']['id']
            name = data['Project']['name']
            self.cbTestCollabProjects.addItem(f'{id}-{name}')
        projects = self.testlinkApi.getProjects()
        for project in projects:
            id = project['id']
            prefix = project['prefix']
            name = project['name']
            self.cbTeslinkProjects.addItem(f'{id}-{prefix}-{name}')
        self.setStatusSettings('Loaded!')

    def onProjectChanged(self, value):
        try:
            project_id = int(value.split('-')[0])
            self.loadPlans(project_id)
            self.loadPlatforms(project_id)
        except ValueError as err:
            print(f'invalid value: {value}, {err}')

    def onPlanChanged(self, value):
        try:
            plan_id = int(value.split('-')[0])
            self.testlinkApi.setPlanId(plan_id)
        except ValueError as err:
            print(f'invalid value: {value}, {err}')

    def onPlatformChanged(self, value):
        try:
            platform_id = int(value.split('-')[0])
            self.testlinkApi.setPlatformId(platform_id)
        except ValueError as err:
            print(f'invalid value: {value}, {err}')

    def onSelectTestCase(self, item):
        print(f'test case selected: {item.text()}')
        test_name = item.text().split('-')[2]
        self.leTestCaseName.setText(test_name)

    def onEditTestCase(self):
        self.searchTestCaseClicked()
        self.tabWidget.setCurrentIndex(0)


    def loadPlans(self, project_id):
        plans = self.testlinkApi.getProjectTestPlans(project_id)
        self.cbTestlinkPlans.clear()
        for plan in plans:
            id = plan['id']
            name = plan['name']
            self.cbTestlinkPlans.addItem(f'{id}-{name}')

    def loadPlatforms(self, project_id):
        platforms = self.testlinkApi.getProjectPlatforms(project_id)
        self.cbTestlinkPlatforms.clear()
        for platform in platforms:
            id = platform['id']
            name = platform['name']
            self.cbTestlinkPlatforms.addItem(f'{id}-{name}')

    def loadTestCases(self):
        test_cases = self.testlinkApi.getTests()
        #print(testcases)
        for test in test_cases:
            prefix = test['full_external_id']
            name = test['tcase_name']
            self.lwTests.addItem(f'{prefix}-{name}')

    def saveSelectedProjects(self):
        testCollabValue = self.cbTestCollabProjects.currentText()
        testlinkValue = self.cbTeslinkProjects.currentText()
        print('Testcollab: ', testCollabValue)
        print('Testlink: ', testlinkValue)
        self.testcollabApi.setProjectId(testCollabValue.split('-')[0])
        project_id = testlinkValue.split('-')[0]
        self.testlinkApi.setPrefix(testlinkValue.split('-')[1])
        self.testlinkApi.setProjectId(project_id)
        self.setStatusSettings('Settings Saved!')
        self.loadTestCases()

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
        self.setStatusSync('Sync Testlink Ok!')

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

    def replace(self):
        search_for = self.leSearchFor.text()
        replace_with = self.leReplaceWith.text()
        steps = self.pteSteps.toPlainText()
        results = self.pteExpectedResults.toPlainText()
        description = self.pteDescription.toPlainText()
        criteria = self.pteAcceptanceCriteria.toPlainText()
        pre_condition = self.ptePreconditions.toPlainText()

        steps = steps.replace(search_for, replace_with)
        results = results.replace(search_for, replace_with)
        description = description.replace(search_for, replace_with)
        criteria = criteria.replace(search_for, replace_with)
        pre_condition = pre_condition.replace(search_for, replace_with)

        self.pteSteps.clear()
        self.pteExpectedResults.clear()
        self.pteDescription.clear()
        self.pteAcceptanceCriteria.clear()
        self.ptePreconditions.clear()

        self.pteSteps.textCursor().insertText(steps)
        self.pteExpectedResults.textCursor().insertText(results)
        self.pteDescription.textCursor().insertText(description)
        self.pteAcceptanceCriteria.textCursor().insertText(criteria)
        self.ptePreconditions.textCursor().insertText(pre_condition)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())