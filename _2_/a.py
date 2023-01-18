import re

import pytest


def get_project_names(links: list[str]):
    pattern = re.compile(
        r'(http(s)?://)?(www\.)?github\.com/([a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[A-Za-z0-9])){0,38})/([a-zA-Z0-9-_\.]*)/?$'
    )
    for link in links:
        if match := re.match(pattern, link):
            yield match.group(5).replace('.git', '')


@pytest.mark.parametrize('links, expected', [
    (
        [
            'https://github.com/miguelgrinberg/Project1/', 
            'https://github.com/miguelgrinberg/Project2.git', 
            'https://github.com/python-dev/Project3/',
            'https://www.github.com/python-dev/Project4/',
            'http://github.com/python-dev/Project5/',
            'github.com/miguelgrinberg/Project6',
            'www.github.com/python-dev/Project7/',
            'https://github.com/-user-/error-service/',
            'https://github.com/p_y_t_h_o_n_d_e_v/error-service/',
            'https://github.com/???/error-service/',
            'https://github.com/python_dev/error-service-?/',
            'https://github.com/python_dev/       /',
            'vk.com/user',
        ],
        [
            'Project1', 'Project2', 
            'Project3', 'Project4', 
            'Project5', 'Project6', 
            'Project7'
        ]
    )
])
def test_get_project_names(links, expected):
    assert list(get_project_names(links)) == expected
