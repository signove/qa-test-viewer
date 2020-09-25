# -*- coding: utf-8 -*-
import os
import testlink
from testlink.testlinkerrors import TLResponseError


class TestlinkApiService:

    def __init__(self):
        self.apiKey = 'YOUR_API_KEY_HERE'
        self.baseUrl = 'http://127.0.0.1/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        self.prefix = None
        self.externalId = None
        self.internalId = None
        self.projectId = None
        self.planId = None
        self.BuildName = None
        self.platformId = None
        self.tests = []
        os.environ["TESTLINK_API_PYTHON_SERVER_URL"] = self.baseUrl
        os.environ["TESTLINK_API_PYTHON_DEVKEY"] = self.apiKey
        try:
            self.tlh = testlink.TestLinkHelper()
            self.tls = self.tlh.connect(testlink.TestlinkAPIClient)
            print('Init Testlink API ... ok')
        except TLResponseError as err:
            print(err)

    def updateTestCase(self, data):
        try:
            actions = data['actions']
            results = data['results']
            steps = []
            try:
                for i, action in enumerate(actions, start=1):
                    steps.append({'step_number': i, 'actions': action, 'expected_results': results[i-1]})
            except IndexError as err:
                print(f'Ops, It\'s missing steps or actions: {err}')

            user = 'samuel.santos'
            testcasename = data['testcasename']
            external_id = data['externalid']
            summary = data['summary']
            preconditions = data['preconditions']
            r = self.tls.updateTestCase(external_id, testcasename=testcasename, summary=summary, preconditions=preconditions, steps=steps, user=user)
            print(r)
        except TLResponseError as err:
            print('err updating test case ', data)
            print(err)

    def getTestCaseIDByName(self, testCaseName):
        try:
            r = self.tls.getTestCaseIDByName(testCaseName)
            print(r)
            self.externalId = r[0]['tc_external_id']
            self.internalId = r[0]['id']
            return self.getFullExternalId()
        except TLResponseError as err:
            print(err)
            return "ID not found"

    def getProjects(self):
        try:
            return self.tls.getProjects()
        except TLResponseError as err:
            print(err)

    def getProjectTestPlans(self, project_id):
        try:
            return self.tls.getProjectTestPlans(project_id)
        except TLResponseError as err:
            print(err)

    def getBuildsForTestPlan(self, plan_id):
        try:
            return self.tls.getBuildsForTestPlan(plan_id)
        except TLResponseError as err:
            print(err)

    def getProjectPlatforms(self, project_id):
        try:
            platforms = []
            platform_dict = self.tls.getProjectPlatforms(project_id)
            for key in platform_dict:
                platforms.append(platform_dict[key])
            return platforms
        except TLResponseError as err:
            print(err)

    def getTests(self):
        tests = []
        self.tests = []
        tcDict = self.tls.getTestCasesForTestPlan(self.planId)
        for primaryKey in sorted(tcDict.keys()):
            value = tcDict[primaryKey]
            if isinstance(value, dict):
                for key in value:
                    tests.append(value[key])
            elif isinstance(value, list):
                tests.append(value[0])
            else:
                print(f'unknown type {type(value)} value {value}')
        for test in tests:
            if test['platform_id'] == str(self.platformId):
                self.tests.append(test)
        return self.tests


    def setPrefix(self, prefix):
        print('Setting prefix: ', prefix)
        self.prefix = prefix

    def setProjectId(self, project_id):
        print('Setting project id:', project_id)
        self.projectId = project_id

    def getFullExternalId(self):
        return '{0}-{1}'.format(self.prefix, self.externalId)

    def getInternalId(self):
        return self.internalId

    def setPlanId(self, plan_id):
        print(f'setting plan id: {plan_id}')
        self.planId = plan_id

    def getPlanId(self):
        return self.planId

    def setPlatformId(self, platform_id):
        print(f'setting plan id: {platform_id}')
        self.platformId = platform_id

    def getPlatformId(self):
        return self.platformId
