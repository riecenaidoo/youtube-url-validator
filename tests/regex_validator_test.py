import unittest
from gui import MyApp


class MyTestCase(unittest.TestCase):

    def test_id_separator(self):
        app = MyApp()
        app.validate_then_add_to_list("https://www.youtube.com/watch?v=hjIlTaAMsbI&list=PLAVwhsWJ9IelfTuP9zu2i1I-BnxMB8Nde&index=1&ab_channel=ContinuousDelivery")
        app.validate_then_add_to_list("https://www.youtube.com/watch?v=hjIlTaery")
        app.validate_then_add_to_list("https://www.youtube.com/watch?v=0q4p76XQxnA&ab_channel=CobaltCalmLofi")
        self.assertEquals(app.ids_to_check, {"hjIlTaAMsbI", "0q4p76XQxnA"})


if __name__ == '__main__':
    unittest.main()
