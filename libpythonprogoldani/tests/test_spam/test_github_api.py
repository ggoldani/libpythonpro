from unittest.mock import Mock

from libpythonprogoldani import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'ggoldani', 'id': 70818371,
                                   'avatar_url': 'https://avatars.githubusercontent.com/u/70818371?v=4'}
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('ggoldani')
    assert 'https://avatars.githubusercontent.com/u/70818371?v=4' == url
