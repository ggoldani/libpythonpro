import pytest as pytest

from libpythonprogoldani.spam.db import Conexao
# todas as fixtures do conftest ficam disponiveis para todos os testes do modulo test_spam


@pytest.fixture(scope='session')  # pode ser utilizada por escopo de function, module ou session
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
