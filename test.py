import unittest


class Test(unittest.TestCase):
    def test(self):
        import ipdb; ipdb.set_trace()
        for i in range(1, 10):
            self.assertEqual(i, i)
        

def main():
    import tracemalloc

    tracemalloc.start(25)
    unittest.main()


if __name__ == '__main__':
    main()
