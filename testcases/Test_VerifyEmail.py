# import json
# import unittest
# import test_utils as tu
#
#
# class TestVerifyEmail(unittest.TestCase):
#
#     def setUp(self):
#         return
#
#     def tearDown(self):
#         return
#
#     def dump(self):
#         json_data = json.dumps({
#             "verify_email": "test@mailinator.com",
#             "type": "account_opening"
#         })
#
#         return json_data
#
#     def test_verify_email(self):
#         i = 1
#         for i in range(10):
#             print("------------------\n")
#             print("RUN NUMBER: ",i)
#             print("------------------\n")
#
#             json_data = self.dump()
#
#             result_js = tu.send_and_receive_ws(json_data)
#
#             print(result_js)
#
