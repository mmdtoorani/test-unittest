from main.main import *
import unittest


class TestIt(unittest.TestCase):
    def test_response_type(self):
        url = "https://jsonplaceholder.typicode.com/posts/"
        self.assertEqual(type(get_data(url)), requests.models.Response)

    def test_json_type(self):
        self.assertEqual(type(combine_to_json()), list or dict)

    def test_creation(self):
        p = "../files/myjson.json"
        with open(p, 'r') as f:
            self.assertEqual(type(json.load(f)), type(combine_to_json()))


if __name__ == '__main__':
    unittest.main()
