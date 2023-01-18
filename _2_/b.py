import pytest

from collections import OrderedDict
from typing import Iterable


def map_lists(keys: list, values: list) -> OrderedDict:
    unique_keys = set(keys)
    validate_keys_and_values(unique_keys, values)
    value_iterator = iter(values + [None] * (len(unique_keys) - len(values)))
    mapping = {}
    for key in keys:
        if not key in unique_keys:
            continue
        mapping[key] = next(value_iterator)
        unique_keys.remove(key)
    mapping = OrderedDict(sorted(mapping.items(), key=lambda pair: pair[0]))
    return mapping


def validate_keys_and_values(keys: Iterable, values: Iterable):
    if len(keys) < len(values):
        raise ValueError(
            (
                'count of different elements in the first list should be ' 
                'greater or equal than count of elements in the second list.'
            )
        )


@pytest.mark.parametrize('keys, values, expected', [
    (
        [2, 1, 3], [4, 5], {1: 5, 2: 4, 3: None}
    ),
    (
        [2, 1, 3], [], {1: None, 2: None, 3: None}
    ),
    (
        [2, 1, 3, 2, 1, 4], ['a', 'b', 'c'], {1: 'b', 2: 'a', 3: 'c', 4: None}
    )
])
def test_map_lists_success(keys, values, expected):
    assert map_lists(keys, values) == expected


@pytest.mark.parametrize('keys, values', [
    (
        [2, 1], [3, 4, 5]
    )
])
def test_map_lists_exception(keys, values):
    with pytest.raises(ValueError):
        map_lists(keys, values)
