from test_plus.test import TestCase

from ..management.commands.update_ballers_not_spartacus import Command


class BaseCommand(TestCase):

    def setUp(self):
        self.command = Command()


class TestGetSubmissionsLinked(BaseCommand):

    def test_nothing(self):
        text = ""
        results = self.command.extract_ballers(text)
        self.assertTrue(len(results) == 0)

    def test_no_description(self):
        text = ("\nKhaldor - [reddit](http://www.reddit.com/user/Khaldor)"
                "|[twitter](https://twitter.com/#!/Khaldor) \n")
        results = self.command.extract_ballers(text)
        self.assertTrue(len(results) == 1)

    def test_no_twitter(self):
        text = ("\nNeedsMoreMinerals - [reddit](http://www.reddit.com/user/"
                "NeedsMoreMinerals) - CEO of ONOG  \n")
        results = self.command.extract_ballers(text)
        self.assertTrue(len(results) == 1)

    def test_double_description(self):
        text = ("\nAlexHDGamer aka HD - [reddit](http://www.reddit.com/user/"
                "AlexHDGamer)|[twitter](https://twitter.com/#!/HDstarcraft) \n")
        results = self.command.extract_ballers(text + text)
        self.assertTrue(len(results) == 2)

    def test_with_description(self):
        text = ("\nsantah - [reddit](http://www.reddit.com/user/santah) - "
                "creator and manager of [sc2casts.com](http://www.sc2casts.com)  \n")
        results = self.command.extract_ballers(text)
        self.assertTrue(len(results) == 1)

    def test_return_length(self):
        text = ("\nKhaldor - [reddit](http://www.reddit.com/user/Khaldor)"
                "|[twitter](https://twitter.com/#!/Khaldor) \n")
        results = self.command.extract_ballers(text)
        self.assertEqual(len(results), 1)
        self.assertEqual(len(results[0]), 3)

    def test_extract_known_as(self):
        text = ("\nKhaldor - [reddit](http://www.reddit.com/user/Khaldor)"
                "|[twitter](https://twitter.com/#!/Khaldor) \n")
        results = self.command.extract_ballers(text)
        self.assertEqual(results[0][0], "Khaldor")

    def test_extract_username(self):
        text = ("\nKhaldor - [reddit](http://www.reddit.com/user/Khaldor)"
                "|[twitter](https://twitter.com/#!/Khaldor) \n")
        results = self.command.extract_ballers(text)
        self.assertEqual(results[0][1], "Khaldor")

    def test_extract_description_when_there_is_none(self):
        text = ("\nKhaldor - [reddit](http://www.reddit.com/user/Khaldor)"
                "|[twitter](https://twitter.com/#!/Khaldor) \n")
        results = self.command.extract_ballers(text)
        self.assertEqual(results[0][2], "")

    def test_extract_description(self):
        text = ("\nsantah - [reddit](http://www.reddit.com/user/santah) - "
                "creator and manager of [sc2casts.com](http://www.sc2casts.com)  \n")
        results = self.command.extract_ballers(text)
        self.assertEqual(results[0][2], "creator and manager of [sc2casts.com](http://www.sc2casts.com)")
