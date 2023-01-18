import pytest


def convert_list(elements: list[int | str]) -> list[int | str]:
    return list(map(lambda e: e * e if isinstance(e, int) else f'abc_{e}_cba', elements))


@pytest.mark.parametrize('elements, expected', [
    ([1, 2, 3, 4], [1, 4, 9, 16]),
    (['a', 'b', 'c', 'd'], ['abc_a_cba', 'abc_b_cba', 'abc_c_cba', 'abc_d_cba']),
    ([1, 'a', 'b', 2, 'c', 3], [1, 'abc_a_cba', 'abc_b_cba', 4, 'abc_c_cba', 9]),
])
def test_convert_list(elements, expected):
    assert convert_list(elements) == expected
