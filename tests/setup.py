class TestClassDemoInstance:
    value = 1

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

    def test_three(self):
        assert self.value != 3
