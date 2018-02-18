import json

from tests.views import TCBase


class TestAccountControl(TCBase):
    def tearDown(self):
        TCBase.tearDown(self)

    def testA_auth(self):
        """
        TC about authentication

        - Before Test
        None

        - Test
        Auth with TCBase.setUp() generated ID, PW
        * Test passes : status code 200 with 'accessToken', 'refreshToken' in response

        - Exception Test
        Incorrect ID
        * Test passes : status code 401

        Incorrect PW
        * Test passes: status code 401
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        # -- Test --

        # -- Exception Test --
        # -- Exception Test --

    def testB_refresh(self):
        """
        TC about refresh(take new access token)

        - Before Test
        None

        - Test
        Refresh with TCBase.setUp() generated refreshToken
        * Test passes : status code 200 with 'accessToken' in response

        - Exception Test
        Unprocessable entity with access token
        * Test passes : status code 422
        """
        # -- Before Test --
        # -- Before Test --

        # -- Test --
        # -- Test --

        # -- Exception Test --
        res = self.client.post(
            '/refresh',
            headers={'Authorization': self.admin_access_token}
        )
        self.assertEqual(res.status_code, 422)
        # -- Exception Test --
