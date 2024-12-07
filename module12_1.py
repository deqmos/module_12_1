import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        obj1 = runner.Runner('Petya')
        for i in range(10):
            obj1.walk()
        self.assertEquals(obj1.distance, 50)

    def test_run(self):
        obj2 = runner.Runner('Peter')
        for i in range(10):
            obj2.run()
        self.assertEquals(obj2.distance, 100)

    def test_challenge(self):
        runer = runner.Runner('Vanya')
        walker = runner.Runner('Kirill')
        for i in range(10):
            runer.run()
            walker.walk()
        self.assertNotEquals(runer.distance, walker.distance)


if __name__ == "__main__":
    unittest.main()
