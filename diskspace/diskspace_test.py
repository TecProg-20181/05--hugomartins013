import os
import unittest
import sys
from diskspace import *


class TestDiskSpace(unittest.TestCase):

    def test_subprocess_check_output(self):
        func = subprocess_check_output('pwd')
        cwd = os.getcwd()+'\n'
        self.assertEquals(cwd, func)

    def test_subprocess_check_output_error(self):
        with self.assertRaises(OSError): subprocess_check_output('not')

    def test_bytes(self):
        blocks = 0
        output = '0.00B'
        result = bytes_to_readable(blocks)
        assert result == output

    def test_return_type(self):
        blocks = 0
        bytes_size = bytes_to_readable(blocks)
        self.assertIsInstance(bytes_size, str)

    def test_bytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), "50.00Kb")

    def test_bytes_to_readable_wrong(self):
        blocks = 100
        self.assertNotEqual(bytes_to_readable(blocks), "50.00Mb")

    def test_empty_block(self):
        blocks = 0
        output = bytes_to_readable(blocks)
        assert output == "0.00B"
    
    def test_block_size(self):
        blocks = 1
        output = bytes_to_readable(blocks)
        assert output == "512.00B"

    def test_print_tree(self):
        fulldepth = 0
        path = '/home/teste'.split("/")[-1]
        result = '{}{}'.format('   '*fulldepth, os.path.basename(path))
        assert result == path


if __name__ == '__main__':
    unittest.main()