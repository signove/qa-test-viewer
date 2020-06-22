# -*- coding: utf-8 -*-
import os
import testlink
from testlink.testlinkerrors import TLResponseError

class TestlinkApiService():

    def __init__(self):
        self.apiKey = 'a16dfe20d95e0aab99b4408a2b0fd8a3'
        self.baseUrl = 'https://testlink.cpv.signove.com/lib/api/xmlrpc/v1/xmlrpc.php'
        #self.apiKey = 'bae5852b0e4a8ac7faa16befb5216c2d'
        #self.baseUrl = 'http://127.0.0.1/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        os.environ["TESTLINK_API_PYTHON_SERVER_URL"] = self.baseUrl
        os.environ["TESTLINK_API_PYTHON_DEVKEY"] = self.apiKey
        self.tlh = testlink.TestLinkHelper()
        self.tls = self.tlh.connect(testlink.TestlinkAPIClient)
        print('init Testlink API ...')

    def getTestCaseIDByName(self, testCaseName):
        r = self.tls.getTestCaseIDByName(testCaseName)
        return r.json()[0]['tc_external_id']

