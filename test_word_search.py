"""
тесты для word_search
"""
import unittest
import io
from word_search import word_search


class TestFiltering(unittest.TestCase):
    """
    тесты для фильтрации файла
    """
    def setUp(self):
        self.file = io.StringIO()
        self.file.write('яблоко.\nЯблоко!\nбанан\nБанан\n'
                        'кот собака рог\nяблоко, Торт\nкот\n'
                        'кот яблоко собака\nКот торт\nбан "торты"')
        self.file.seek(0)
        self.words = ['яблоко', 'Торт', 'банан', 'тест']

    def test_word_search(self):
        """
        тесты для file_filtering
        """
        get_line = word_search(self.file, self.words)
        self.assertEqual(next(get_line), 'яблоко.\n')
        self.assertEqual(next(get_line), 'Яблоко!\n')
        self.assertEqual(next(get_line), 'банан\n')
        self.assertEqual(next(get_line), 'Банан\n')
        self.assertEqual(next(get_line), 'яблоко, Торт\n')
        self.assertEqual(next(get_line), 'кот яблоко собака\n')
        self.assertEqual(next(get_line), 'Кот торт\n')
        with self.assertRaises(StopIteration):
            next(get_line)

    def test_word_search_file(self):
        words = ['Java', 'hacker']
        get_line = word_search('test_file.txt', words)
        self.assertEqual(next(get_line), 'в 1995 году, а в 1998 году перешел с Perl на Java,'
                                         ' а затем на Python. В 2015 году\n')
        self.assertEqual(next(get_line), 'и сооснователь клуба Garoa Hacker Clube,'
                                         ' первого места для общения хакеров\n')
        with self.assertRaises(StopIteration):
            next(get_line)

    def test_word_search_failed(self):
        """
        тесты для ошибок в file_filtering
        """
        get_line = word_search(1, self.words)
        with self.assertRaises(TypeError) as err:
            next(get_line)
        self.assertEqual(str(err.exception), "'int' object is not iterable")
        get_line = word_search(self.file, 1)
        with self.assertRaises(TypeError) as err:
            next(get_line)
        self.assertEqual(str(err.exception), "'int' object is not iterable")
        with self.assertRaises(TypeError) as err:
            word_search()
        self.assertEqual(str(err.exception),
                         "word_search() missing"
                         " 2 required positional arguments:"
                         " 'file' and 'search_words'")
        get_line = word_search('test_fail.txt', self.words)
        with self.assertRaises(FileNotFoundError) as err:
            next(get_line)
        self.assertEqual(str(err.exception),
                         "[Errno 2] No such file or directory:"
                         " 'test_fail.txt'")
        get_line = word_search('test_file.txt', self.words, 1)
        with self.assertRaises(TypeError) as err:
            next(get_line)
        self.assertEqual(str(err.exception),
                         "open() argument 'encoding'"
                         " must be str or None, not int")
        get_line = word_search('test_file.txt', self.words, 'test')
        with self.assertRaises(LookupError) as err:
            next(get_line)
        self.assertEqual(str(err.exception), 'unknown encoding: test')


if __name__ == '__main__':
    unittest.main()
