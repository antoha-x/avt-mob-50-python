import pytest
from MainClass import MainClass

class TestMainClass:
    expected_value_test_1 = 14
    expected_value_test_2 = 45
    expected_value_test_3 = ["Hello", "hello"]
    mc = MainClass()


    def test_get_local_number(self):
        assert self.mc.get_local_number() == self.expected_value_test_1, "getLocalNumber return not 14"

    def test_get_class_number(self):
        assert self.mc.get_class_number() > self.expected_value_test_2, "getClassNumber return less than 45"

    def test_get_class_string(self):
        assert any(list(map(lambda x: x in self.mc.get_class_string(), self.expected_value_test_3))), \
            f"getClassString does not contain the substring {self.expected_value_test_3}"
