import unittest
from temp_tracker import TempTracker
from flatten_array import flatten


class TestFlattenArray(unittest.TestCase):
    
    def test_flatten(self):
        arr = [[1,2,[3]],4]
        self.assertEqual(flatten(arr), [1,2,3,4])
        arr = [[1],2,[3],4]
        self.assertEqual(flatten(arr), [1,2,3,4])
        arr = [[1],2,[3],4,[[[[[[[6]]]]]]]]
        self.assertEqual(flatten(arr), [1,2,3,4,6])
        arr = [1,[2,[3,[4,[5,[6,[7,[8],9],10],11],12],13],14]]
        self.assertEqual(flatten(arr), [1,2,3,4,5,6,7,8,9,10,11,12,13,14])

class TestTempTracker(unittest.TestCase):

    def test_insert(self):
        temp = TempTracker()
        temp.insert(68)
        with self.assertRaises(TypeError):
            temp.insert("not a number")

        with self.assertRaises(ValueError):
            temp.insert(-1)

        with self.assertRaises(ValueError):
            temp.insert(115)

    def test_get_min(self):
        temp = TempTracker()
        temp.insert(68)
        self.assertEqual(temp.get_min(), 68)
        temp.insert(78)
        temp.insert(89)
        self.assertEqual(temp.get_min(), 68)
        temp.insert(50)
        self.assertEqual(temp.get_min(), 50)
        temp.insert(23)
        temp.insert(1)
        self.assertEqual(temp.get_min(), 1)

    def test_get_max(self):
        temp = TempTracker()
        temp.insert(68)
        self.assertEqual(temp.get_max(), 68)
        temp.insert(78)
        temp.insert(89)
        self.assertEqual(temp.get_max(), 89)
        temp.insert(50)
        self.assertEqual(temp.get_max(), 89)
        temp.insert(23)
        temp.insert(91)
        self.assertEqual(temp.get_max(), 91)

    def test_get_mean(self):
        temp = TempTracker()
        temp.insert(68)
        self.assertEqual(temp.get_mean(), 68)
        temp.insert(78)
        temp.insert(89)
        self.assertEqual(temp.get_mean(), 78.33)
        temp.insert(50)
        self.assertEqual(temp.get_mean(), 71.25)
        temp.insert(23)
        temp.insert(1)
        self.assertEqual(temp.get_mean(), 51.5)

if __name__ == '__main__':
    unittest.main()
