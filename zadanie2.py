import functools
import zadanie1


class MultipleAccumulate:
    def __init__(self, numbers, *functions):
        self.data_list = numbers
        self.accumulate_functions = functions

    def get_data(self):
        results = {}
        for f in self.accumulate_functions:
            results[f.__name__] = functools.reduce(f, self.data_list[:])
        return results


def sum(x, y):
    return x + y


def main():
    multi = MultipleAccumulate([1, 2, 3, 4, 5], sum, max, min)
    text = zadanie1.TextViewer("C:\\Users\\PK\\Downloads\\da1.txt")
    for obj in multi, text:
        print(obj.get_data())


if __name__ == "__main__":
    main()
