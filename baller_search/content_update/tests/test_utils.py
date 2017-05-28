from test_plus.test import TestCase

from ..utils import clean_known_as, clean_username, shorten_text


class TestCleanKnownAs(TestCase):

    def test_empty_input(self):
        text = ""
        known_as = clean_known_as(text)
        self.assertEqual("", known_as)

    def test_input_strips(self):
        text = " hello "
        known_as = clean_known_as(text)
        self.assertEqual("hello", known_as)

    def test_input_multiple_words(self):
        text = "Day[9] or bob among friends :)"
        known_as = clean_known_as(text)
        self.assertEqual("Day[9]", known_as)


class TestCleanUsername(TestCase):

    def test_straight_up(self):
        text = "Day[9]"
        known_as = clean_username(text)
        self.assertEqual("Day[9]", known_as)

    def test_same_as_with_reddit_user_reference(self):
        with_text = "/u/Day[9]"
        without_text = "Day[9]"
        self.assertEqual(clean_username(with_text), clean_username(without_text))


class TestShortenText(TestCase):

    def test_too_small(self):
        text = "hello world"
        with self.assertRaises(AssertionError):
            shorten_text(text, 3)

    def test_length_is_longer_than_word(self):
        # So no shortening occurs
        text = "hello world"
        result = shorten_text(text, 99999)
        self.assertEqual(text, result)

    def test_shortening(self):
        text = "hello world"
        result = shorten_text(text, 8)
        self.assertEqual("hello...", result)
