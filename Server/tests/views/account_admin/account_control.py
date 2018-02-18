import json

from app.models.account import SignupWaitingModel

from tests.views import TCBase


class TestAccountControl(TCBase):
    def tearDown(self):
        SignupWaitingModel.objects.delete()

        TCBase.tearDown(self)

    def testA_deleteStudentAccount(self):
        """
        TC about existing student account deletion

        - Before Test
        None

        - Test
        Take UUID with signed student account deletion
        * Test passes : status code 201 with 'uuid': length=4 in response

        - Exception Test
        Non-existing student number
        * Test passes : status code 204

        Forbidden with student access token
        * Test passes : status code 403
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        res = self.json_request(self.client.delete, '/admin/account-control/student', {'number': 1111}, self.admin_access_token)
        self.assertEqual(res.status_code, 201)

        response_data = json.loads(res.data.decode())
        self.assertTrue('uuid' in response_data)
        self.assertTrue(len(response_data['uuid']) == 4)
        # -- Test --

        # -- Exception Test --
        res = self.json_request(self.client.delete, '/admin/account-control/student', {'number': 1}, self.admin_access_token)
        self.assertEqual(res.status_code, 204)

        res = self.json_request(self.client.delete, '/admin/account-control/student', {'number': 1111}, self.student_access_token)
        self.assertEqual(res.status_code, 403)
        # -- Exception Test --

    def testB_deleteAlreadySignupWaitingStudent(self):
        """
        TC about already signup waiting student account deletion

        - Before Test
        Remove student account : move student data to signup_waiting
        * DELETE /admin/account-control/student

        - Test
        Get just UUID with already signup waiting student number
        * Test passes : status code 200 with 'uuid': length=4 in response

        - Exception Test
        None

        - After Test
        Clear SignupWaitingModel
        """
        # -- Before Test --
        res = self.json_request(self.client.delete, '/admin/account-control/student', {'number': 1111}, self.admin_access_token)
        self.assertEqual(res.status_code, 201)
        # -- Before Test --

        # -- Test --
        res = self.json_request(self.client.delete, '/admin/account-control/student', {'number': 1111}, self.admin_access_token)
        self.assertEqual(res.status_code, 200)

        response_data = json.loads(res.data.decode())
        self.assertTrue('uuid' in response_data)
        self.assertTrue(len(response_data['uuid']) == 4)
        # -- Test --

        # -- Exception Test --
        # -- Exception Test --

    def testC_createNewAdminAccount(self):
        """
        TC about new admin account creation

        - Before Test
        None

        - Test
        Create new admin account
        * Test passes : status code 201

        - Exception Test
        Already existing ID
        * Test passes : status code 204

        Forbidden with student access token
        * Test passes : status code 403
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        res = self.json_request(self.client.post, '/admin/account-control/admin', {'id': 'new', 'pw': 'new', 'name': 'new'}, self.admin_access_token)
        self.assertEqual(res.status_code, 201)
        # -- Test --

        # -- Exception Test --
        res = self.json_request(self.client.post, '/admin/account-control/admin', {'id': 'new', 'pw': 'new', 'name': 'new'}, self.admin_access_token)
        self.assertEqual(res.status_code, 204)

        res = self.json_request(self.client.post, '/admin/account-control/admin', {'id': 'new', 'pw': 'new', 'name': 'new'}, self.student_access_token)
        self.assertEqual(res.status_code, 403)
        # -- Exception Test --

    def testD_deleteAdminAccount(self):
        """
        TC about new admin account deletion

        - Before Test
        Create new admin account to delete
        * POST /admin/account-control/admin

        - Test
        Delete new admin account
        * Test passes : status code 200

        - Exception Test
        Non-existing ID
        * Test passes : status code 204

        Forbidden with student access token
        * Test passes : status code 403
        """
        # -- Before Test --
        res = self.json_request(self.client.post, '/admin/account-control/admin', {'id': 'new', 'pw': 'new', 'name': 'new'}, self.admin_access_token)
        self.assertEqual(res.status_code, 201)
        # -- Before Test --

        # -- Test --
        res = self.json_request(self.client.delete, '/admin/account-control/admin', {'id': 'new'}, self.admin_access_token)
        self.assertEqual(res.status_code, 200)
        # -- Test --

        # -- Exception Test --
        res = self.json_request(self.client.delete, '/admin/account-control/admin', {'id': 'new'}, self.admin_access_token)
        self.assertEqual(res.status_code, 204)

        res = self.json_request(self.client.delete, '/admin/account-control/admin', {'id': 'new'}, self.student_access_token)
        self.assertEqual(res.status_code, 403)
        # -- Exception Test --
