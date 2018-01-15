from unittest import TestCase

import package_name


class TestFun(TestCase):
    def test_is_string(self):
        s = char_dataset_generator.run()
        self.assertTrue(isinstance(s, basestring))