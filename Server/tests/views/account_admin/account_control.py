import json

from app.models.account import SignupWaitingModel

from tests.views import TCBase


class TestAccountControl(TCBase):
    def testA_deleteStudentAccount(self):
        """
        TC about existing student account deletion

        - Before Test
        None

        - Test
        Take UUID with signed student account deletion
        * Test passes : status code 201 with new UUID(length 4) in response

        - Exception Test
        Non-existing student number
        * Test passes : status code 204

        Forbidden with student access token
        * Test passes : status code 403

        - After Test
        Clear SignupWaitingModel
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        res = self.client.delete(
            '/admin/account-control/student',
            data=json.dumps({'number': 1111}),
            content_type='application/json',
            headers={'Authorization': self.admin_access_token}
        )
        self.assertTrue(res.status_code == 201)

        response_data = json.loads(res.data.decode())
        self.assertTrue('uuid' in response_data)
        self.assertTrue(len(response_data['uuid']) == 4)
        # -- Test --

        # -- Exception Test --
        res = self.client.delete(
            '/admin/account-control/student',
            data=json.dumps({'number': 0000}),
            content_type='application/json',
            headers={'Authorization': self.admin_access_token}
        )
        self.assertTrue(res.status_code == 204)

        res = self.client.delete(
            '/admin/account-control/student',
            content_type='application/json',
            headers={'Authorization': self.student_access_token}
        )
        self.assertTrue(res.status_code == 403)
        # -- Exception Test --

        # -- After Test --
        SignupWaitingModel.objects.delete()
        # -- After Test --

    def testB_deleteAlreadySignupWaitingStudent(self):
        """
        TC about already signup waiting student account deletion

        - Before Test
        Remove student account, move student data to signup_waiting
        * DELETE /admin/account-control/student

        - Test
        Get just UUID with already signup waiting student number
        * Test passes : status code 200 with UUID(length 4) in response

        - Exception Test
        None

        - After Test
        Clear SignupWaitingModel
        """
        # -- Before Test --
        res = self.client.delete(
            '/admin/account-control',
            data=json.dumps({'number': 1111}),
            content_type='application/json',
            headers={'Authorization': self.admin_access_token},
        )
        self.assertTrue(res.status_code == 201)
        # -- Before Test --

        # -- Test --
        res = self.client.delete(
            '/admin/account-control',
            data=json.dumps({'number': 1111}),
            content_type='application/json',
            headers={'Authorization': self.admin_access_token},
        )
        self.assertTrue(res.status_code == 200)

        response_data = json.loads(res.data.decode())
        self.assertTrue('uuid' in response_data)
        self.assertTrue(len(response_data['uuid']) == 4)
        # -- Test --

        # -- Exception Test --
        # -- Exception Test --

        # -- After Test --
        SignupWaitingModel.objects.delete()
        # -- After Test --
