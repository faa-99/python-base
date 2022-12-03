dummy_dict = {"cat": "kitten", "fish": "fish", "dog": "dogs"}


def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}


def sort_dict_by_value(dictionary, reverse: bool = False):
    """
    If reverse is true, it will sort in descending order
    :param dictionary:
    :param reverse:
    :return:
    """
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


def sort_dict_by_key(dictionary, reverse: bool = False):
    return dict(sorted(dictionary.items(), reverse=reverse))


def sort_dict_by_val_then_key(dictionary, reverse: bool = False):
    return dict(sorted(dictionary.items(), key=lambda x: (x[1], x[0]), reverse=reverse))


if __name__ == "__main__":
    print(sort_dict_by_value(dummy_dict))
    print(sort_dict_by_key(dummy_dict))
    print(sort_dict_by_val_then_key(dummy_dict))
    print(invert_dictionary(dummy_dict))
