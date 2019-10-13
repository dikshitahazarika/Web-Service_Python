import unittest

from main import main

class Test(unittest.TestCase):
     def test_index(self):
        tester = main.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

     def test_ping(self):
        tester = main.test_client(self)
        expected_response = "pong"
        response = tester.get("/ping")
        # print(response.data.decode('utf-8'))
        self.assertEqual(response.data.decode('utf-8'), expected_response)
     def test_system(self):
        tester = main.test_client(self)
        response = tester.get("/system")
        self.assertEqual(response.status_code, 200)
     def test_media(self):
        tester = main.test_client(self)
        input = "11497188"
        response = tester.get("/mediainfo/" + input)
        self.assertEqual(response.status_code, 200)
     def test_exception_id(self):
        tester = main.test_client(self)
        response = tester.get("/mediainfo/11")
        # print(response.data.decode('utf-8'))
        msg = "<h1>Pond Test</h1>\
        <p>Id is not available</p>\
        <p>Please enter a valid id</p>"
        # print(msg)
         self.assertIn(response.data, msg.encode('utf-8'))
         self.assertEqual(response.status_code, 200)
     def test_exception(self):
        tester = main.test_client(self)
        response = tester.get("/service")
        # print(response.data.decode('utf-8'))
        msg = "<h1>ERROR!! PLEASE TRY WITH PING</h1>"
        # print(msg)
         self.assertIn(response.data,msg.encode('utf-8'))
         self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
