import unittest
from io import StringIO
from tests.test_base import captured_io
import cli


class MyTestCase(unittest.TestCase):

    def test_something(self):
        with captured_io(StringIO("https://www.youtube.com/watch?v=dusfmL_bm1o\nhttps://www.youtube.com/watch?v=U97cmp4hTUI\nhttps://www.youtube.com/watch?v=U97cmp\nexit")) as (out, err):
            cli.run()
        actual = out.getvalue().strip()
        self.assertEqual(actual, """Enter your url: {'dusfmL_bm1o'}\nEnter your url: {'U97cmp4hTUI', 'dusfmL_bm1o'}
Enter your url: {'U97cmp4hTUI', 'dusfmL_bm1o'}
Enter your url: Goodbye!""")


if __name__ == '__main__':
    unittest.main()
