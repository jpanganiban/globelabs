import unittest
import globelabs


class GlobeTestCase(unittest.TestCase):

    def setUp(self):
        self.app_id = "BGyKAhGbyoGhRdiA8kTyMXhR9yGEhzoa"
        self.app_secret = "8ed742b6c27e38db323ab24e19460a38eb0bf52804fc08f4df897db206b7b690"
        self.shortcode = "1027"
        self.globe = globelabs.Globe(app_id=self.app_id,
                                     app_secret=self.app_secret,
                                     shortcode=self.shortcode)

    def tearDown(self):
        self.globe = None

    def test_properties(self):
        self.assertEqual(self.globe.app_id, self.app_id)
        self.assertEqual(self.globe.app_secret, self.app_secret)

    def test_get_auth_url(self):
        self.assertEqual(self.globe.get_auth_url(),
                         "http://developer.globelabs.com.ph/dialog/oauth?app_id=%s" % self.app_id)

    def test_get_access_token(self):
        self.globe.get_access_token("r9UoAgXpCjpjE7UepoLGubqq48U5E5aXuBok79FKbdAnhnzEG4sz5Ao8hBzM9XFrLGg5tLy75btz4Ge6u9M4zph857zBu7AaXGsM9xbGfkrKB9Hgz8jRsj5BpLuX8T7jK9iBpKu5q8XBs7aKMkHyjx85fazaqMs8G7Eeu6R4yehr7GgMu597EBtn4G74tnkMoBFAKA6AhA4EzLsb5d7XhLnkzyFer56Lu6dqdjUEgo5xuAzjarUn7gKnCAqGyrU6")

    def test_send_sms(self):
        self.globe.get_access_token("r9UoAgXpCjpjE7UepoLGubqq48U5E5aXuBok79FKbdAnhnzEG4sz5Ao8hBzM9XFrLGg5tLy75btz4Ge6u9M4zph857zBu7AaXGsM9xbGfkrKB9Hgz8jRsj5BpLuX8T7jK9iBpKu5q8XBs7aKMkHyjx85fazaqMs8G7Eeu6R4yehr7GgMu597EBtn4G74tnkMoBFAKA6AhA4EzLsb5d7XhLnkzyFer56Lu6dqdjUEgo5xuAzjarUn7gKnCAqGyrU6")
        self.globe.send_sms("Hello")

    def test_charge(self):
        self.globe.get_access_token("r9UoAgXpCjpjE7UepoLGubqq48U5E5aXuBok79FKbdAnhnzEG4sz5Ao8hBzM9XFrLGg5tLy75btz4Ge6u9M4zph857zBu7AaXGsM9xbGfkrKB9Hgz8jRsj5BpLuX8T7jK9iBpKu5q8XBs7aKMkHyjx85fazaqMs8G7Eeu6R4yehr7GgMu597EBtn4G74tnkMoBFAKA6AhA4EzLsb5d7XhLnkzyFer56Lu6dqdjUEgo5xuAzjarUn7gKnCAqGyrU6")
        self.globe.charge(0, "2158%s0000099" % self.shortcode)


if __name__ == '__main__':
    unittest.main()
