class overload:

    def test_overload(self, toan=None):

        if toan is not None:
            print('A cuong oi em ko bi ' + toan)
        else:
            print('A cuong oi em ko bi nCov 19')
obj = overload()
obj.test_overload()
obj.test_overload('gay')
obj.test_overload('HIV')