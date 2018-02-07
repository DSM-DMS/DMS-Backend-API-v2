import json

from tests.views import TCBase


class TestAccountControl(TCBase):
    def testA_deleteStudentAccount(self):
        """
        TC about existing student account deletion

        - Preparations
        None

        - Process
        Take UUID with signed student account deletion
        * Test passes : status code 201 with new UUID(length 4) in response

        - Exception Tests
        Non-existing student number
        * Test passes : status code 204

        Forbidden with student access token
        * Test passes : status code 403
        """
        # -- Preparations --
        # -- Preparations --

        # -- Process --
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
        # -- Process --

        # -- Exception Tests --
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
        # -- Exception Tests --

    def testB_deleteAlreadySignupWaitingStudent(self):
        """
        TC about already signup waiting student account deletion

        - Preparations
        Remove student account, move student data to signup_waiting
        * DELETE /admin/account-control/student

        - Process
        Get just UUID with already signup waiting student number
        * Test passes : status code 200 with UUID(length 4) in response

        - Exception Tests
        None
        """
        # -- Preparations --
        res = self.client.delete(
            '/admin/account-control',
            data=json.dumps({'number': 1111}),
            content_type='application/json',
            headers={'Authorization': self.admin_access_token},
        )
        self.assertTrue(res.status_code == 201)
        # -- Preparations --

        # -- Process --
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
        # -- Process --

        # -- Exception Tests --
        # -- Exception Tests --
