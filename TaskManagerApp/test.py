import unittest
import app

TEST_DB = 'test.db'

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['DEBUG'] = False
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_baseRoute(self):
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()