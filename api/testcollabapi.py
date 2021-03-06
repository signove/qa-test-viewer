# -*- coding: utf-8 -*-

import requests


class TestCollabApiService:

    def __init__(self):
        self.projectId = None
        self.testCaseId = None
        self.suiteId = None
        self.apiKey = 'YOUR_API_KEY_HERE'
        self.baseUrl = 'YOUR_APP_NAME_HERE.app.testcollab.com'
        print('Init TestCollab ... ok')

    def getProjects(self):
        print('Requesting project ...')
        try:
            project_url = 'https://{0}/index.php/projects/index.json?API_KEY={1}'.format(self.baseUrl, self.apiKey)
            r = requests.get(project_url).json()
            print('request  ... [done]')
            return r['data']['projects']
        except ConnectionError:
            return []

    def getTestCaseByTitle(self, filter):
        print('Searching by : ', filter)
        try:
            filter_url = 'https://{0}/index.php/project/{1}/test_cases/indexv2.json?API_KEY={2}&filters[1][field]=title&filters[1][value]={3}&filters[1][operator]=contains'.format(
            self.baseUrl, self.projectId, self.apiKey, filter)
            r = requests.get(filter_url).json()
            print('search  ... [done]')
            return r
        except ConnectionError as err:
            print(f'Ops, error {err}')

    def setProjectId(self, project_id):
        self.projectId = project_id
        print('Setting TestCollab id: ', self.projectId)

    def setTestCaseId(self, id):
        self.testCaseId = id
        print('Setting test case id: ', self.testCaseId)

    def setSuiteId(self, suite_id):
        self.suiteId = suite_id
        print('Setting suite id: ', self.suiteId)

    def updateTestCase(self, data):
        try:
            print('sending update  ... [started]')
            headers = {'Content-type': 'application/json'}
            update_url = 'https://{0}/index.php/project/{1}/test_cases/edit/{2}.json?API_KEY={3}'.format(self.baseUrl, self.projectId, self.testCaseId, self.apiKey)
            print('post ', update_url)
            r = requests.post(update_url, json=data, headers=headers)
            print('update  ... [done]')
            print(r.json())
        except ConnectionError as err:
            print(f'Ops, error {err}')
