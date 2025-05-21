def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

        for name, value in zip(arg_names, args):
            expected_type = annotations.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{name}' must be of type {expected_type.__name__}, got {type(value).__name__}")

        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

#Оставил как в примере
if __name__ == '__main__':
    print(sum_two(1, 2))
    print(sum_two(1, 2.4))
