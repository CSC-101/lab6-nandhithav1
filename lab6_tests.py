import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    import unittest
    from lab6 import Book, selection_sort_books

    class TestSelectionSortBooks(unittest.TestCase):
        def test_empty_list(self):
            self.assertEqual(selection_sort_books([]), [])

        def test_sort_books_by_title(self):
            book1 = Book("C Programming")
            book2 = Book("Java Programming")
            book3 = Book("Python Programming")
            books = [book3, book1, book2]
            sorted_books = selection_sort_books(books)
            self.assertEqual([book.title for book in sorted_books],
                             ["C Programming", "Java Programming", "Python Programming"])

    # Part 2
    class TestSwapCase(unittest.TestCase):
        def test_simple_case(self):
            self.assertEqual(swap_case("Hello World"), "hELLO wORLD")

        def test_mixed_characters(self):
            self.assertEqual(swap_case("PyThOn3!"), "pYtHoN3!")

    # Part 3
    class TestStrTranslate(unittest.TestCase):
        def test_replacement(self):
            self.assertEqual(str_translate("abcdcba", "a", "x"), "xbcdcbx")

        def test_no_occurrence(self):
            self.assertEqual(str_translate("hello", "z", "y"), "hello")

    # Part 4
    class TestHistogram(unittest.TestCase):
        def test_single_word(self):
            self.assertEqual(histogram("hello"), {"hello": 1})

        def test_multiple_words(self):
            self.assertEqual(histogram("hello world hello"), {"hello": 2, "world": 1})


if __name__ == '__main__':
    unittest.main()
