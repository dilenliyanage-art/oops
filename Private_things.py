class myclass:
    _private_var = 27
    def _method(self):
        print("i am inside a class variable")
    def hello(self):
        print("private massage",myclass._private_var)
foo = myclass()
foo._method()
foo.hello