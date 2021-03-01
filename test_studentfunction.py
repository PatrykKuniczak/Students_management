from unittest import TestCase

from studentfunction import Student

class TestStudent(TestCase):
    def test_date_valid(self):
        self.assertTrue(Student.date_valid("01.03.2003"))

    def test_data_correctness(self):
        self.assertTrue(Student.data_correctness("Lolooooooooooooooooooooooooooooooooooo" , "Lolek1" , "11.12.2002"))

    # def test_change_a_semester(self):
    #     self.fail()
    #
    # def test_get_year(self):
    #     self.fail()