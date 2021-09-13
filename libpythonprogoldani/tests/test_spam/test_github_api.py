from unittest.mock import Mock

import pytest as pytest

from libpythonprogoldani import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/70818371?v=4'
    resp_mock.json.return_value = {'login': 'ggoldani', 'id': 70818371,
                                   'avatar_url': url}
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('ggoldani')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
