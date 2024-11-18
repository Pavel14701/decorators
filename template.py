test_str = 'Hi from'


class A1Decorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result} [a1]'
        return wrapper

class B1Decorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result} [b1]'
        return wrapper

class A2Decorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result} [a2]'
        return wrapper


class B2Decorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result} [b2]'
        return wrapper


class ADecorator:
    a1 = A1Decorator()
    b1 = B2Decorator()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result} [a]'
        return wrapper


class BDecorator:
    a2 = A1Decorator()
    b2 = B2Decorator()

    def __call__(self, func) -> str:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result} [b]'
        return wrapper


class FirstDecorator:
    a = ADecorator()
    b = BDecorator()

    def __call__(self, func) -> str:
        def wrapper(*args, **kwargs) -> str:
            result = func(*args, **kwargs)
            return f'{result} [first]'
        return wrapper

class SecondDecorator:
    a = ADecorator()
    b = BDecorator()

    def __call__(self, func) -> str:
        def wrapper(*args, **kwargs) -> str:
            result = func(*args, **kwargs)
            return f'{result} [second]'
        return wrapper


class MetaDecorator(type):
    def __getattr__(self, name:str) -> FirstDecorator|SecondDecorator:
        if name == 'first':
            return FirstDecorator()
        elif name == 'second':
            return SecondDecorator()
        raise AttributeError(f"'{self.__name__}' object has no attribute '{name}'")


class decorator(metaclass=MetaDecorator):
    def __call__(self, func) -> str:
        def wrapper(*args, **kwargs) -> str:
            result = func(*args, **kwargs)
            return f'{result} [decorator]'
        return wrapper


@decorator.first.a.a1
@decorator.first.a
@decorator.first
@decorator()
def testing_a(test_str:str=test_str):
    return test_str

@decorator.second.b.b2
@decorator.second.b
@decorator.second
@decorator()
def testing_b(test_str:str=test_str):
    return test_str


print(testing_a())
print(testing_b())