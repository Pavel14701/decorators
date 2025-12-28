test_str = "Hi from"

def apply_chain(func, chain):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for level in chain:
            result = f"{result} [{level}]"
        return result
    return wrapper


class A1Decorator:
    def __init__(self, chain):
        self.chain = chain + ["a1"]

    def __call__(self, func):
        return apply_chain(func, self.chain)


class ADecorator:
    def __init__(self, chain):
        self.chain = chain + ["a"]
        self.a1 = A1Decorator(self.chain)

    def __call__(self, func):
        return apply_chain(func, self.chain)


class FirstDecorator:
    def __init__(self, chain):
        self.chain = chain + ["first"]
        self.a = ADecorator(self.chain)

    def __call__(self, func):
        return apply_chain(func, self.chain)


class Decorator:
    def __init__(self):
        self.first = FirstDecorator(["decorator"])

    def __call__(self, func):
        return apply_chain(func, ["decorator"])


decorator = Decorator()


@decorator.first.a.a1
def testing_a(test_str: str = test_str):
    return test_str


print(testing_a())
