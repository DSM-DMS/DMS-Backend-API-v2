import json

from tests.views import TCBase


class Test(TCBase):
    def test_download_extension_11_apply_status(self):
        """
        TC about extension 11 apply status download

        - Before Test
        Apply extension 11 with student's access token
        * POST /extension/11

        - Test
        Download extension 11 apply status included excel file with admin's access token
        * Test passes : status code 200 with excel file in response

        - Exception Test
        Forbidden with student's access token
        * Test passes : status code 403
        """
        # -- Before Test --
        res = self.student_json_request(self.client.post, '/extension/11', {'classNum': 1, 'seatNum': 1})
        self.assertEqual(res.status_code, 201)
        # -- Before Test --

        # -- Test --
        res = self.client.get('/admin/extension/11', headers={'Authorization': self.admin_access_token})
        self.assertEqual(res.status_code, 200)
        # -- Test --

        # -- Exception Test --
        res = self.client.get('/admin/extension/11', headers={'Authorization': self.student_access_token})
        self.assertEqual(res.status_code, 403)
        # -- Exception Test --

    def test_download_extension_12_apply_status(self):
        """
        TC about extension 12 apply status download

        - Before Test
        Apply extension 12 with student's access token
        * POST /extension/12

        - Test
        Download extension 12 apply status included excel file with admin's access token
        * Test passes : status code 200 with excel file in response

        - Exception Test
        Forbidden with student's access token
        * Test passes : status code 403
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        # -- Test --

        # -- Exception Test --
        # -- Exception Test --

    def test_download_goingout_apply_status(self):
        """
        TC about goingout apply status download

        - Before Test
        Apply goingout with student's access token
        * POST /goingout

        - Test
        Download goingout apply status included excel file with admin's access token
        * Test passes : status code 200 with excel file in response

        - Exception Test
        Forbidden with student's access token
        * Test passes : status code 403
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        # -- Test --

        # -- Exception Test --
        # -- Exception Test --

    def test_download_stay_apply_status(self):
        """
        TC about stay apply status download

        - Before Test
        Apply stay with student's access token
        * POST /stay

        - Test
        Download stay apply status included excel file with admin's access token
        * Test passes : status code 200 with excel file in response

        - Exception Test
        Forbidden with student's access token
        * Test passes : status code 403
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        # -- Test --

        # -- Exception Test --
        # -- Exception Test --
