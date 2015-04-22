import unittest

from nocredentials.__main__ import main


class MainTestCase(unittest.TestCase):
    def test_main(self):
        with self.assertRaises(SystemExit) as cm:
            main([])
        self.assertEqual(cm.exception.code, 2)


class ArgTestCase(unittest.TestCase):
    def test_help(self):
        with self.assertRaises(SystemExit) as cm:
            main(['-h'])
        self.assertEqual(cm.exception.code, 0)

    def test_help_long(self):
        with self.assertRaises(SystemExit) as cm:
            main(['--help'])
        self.assertEqual(cm.exception.code, 0)

    def test_bad_arg(self):
        with self.assertRaises(SystemExit) as cm:
            main(['-X'])
        self.assertEqual(cm.exception.code, 2)

if __name__ == '__main__':
    unittest.main(buffer=True)
