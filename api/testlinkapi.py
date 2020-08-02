# -*- coding: utf-8 -*-
import os
import testlink
from testlink.testlinkerrors import TLResponseError


class TestlinkApiService:

    def __init__(self):
        self.apiKey = 'a16dfe20d95e0aab99b4408a2b0fd8a3'
        self.baseUrl = 'https://testlink.cpv.signove.com/lib/api/xmlrpc/v1/xmlrpc.php'
        # self.apiKey = 'bae5852b0e4a8ac7faa16befb5216c2d'
        # self.baseUrl = 'http://127.0.0.1/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        self.prefix = None
        self.externalId = None
        self.internalId = None
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
            for i, action in enumerate(actions, start=1):
                steps.append({'step_number': i, 'actions': action, 'expected_results': results[i-1]})
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
        except:
            return "ID not found"

    def getProjects(self):
        return self.tls.getProjects()

    def setPrefix(self, prefix):
        print('Setting prefix: ', prefix)
        self.prefix = prefix

    def getFullExternalId(self):
        return '{0}-{1}'.format(self.prefix, self.externalId)

    def getInternalId(self):
        return self.internalId
