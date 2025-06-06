from decorators.deprecated import deprecated

@deprecated
def test():
    print("Inside test")
    

def test_deprecated():
    test()
    print("Success")