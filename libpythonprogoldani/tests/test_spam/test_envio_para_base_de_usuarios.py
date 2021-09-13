from unittest.mock import Mock

import pytest as pytest

from libpythonprogoldani.spam.enviador_de_email import Enviador
from libpythonprogoldani.spam.main import EnviadorDeSpam
from libpythonprogoldani.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Goldani', email='goldani@gmail.com'),
            Usuario(nome='Maciel', email='maciel@gmail.com')
        ],
        [
           Usuario(nome='Gustavo', email='gustavo@gmail.com')
        ]
    ]
)
def test_qnt_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavo@gmail.com',
        'Assunto',
        'Conteudo'
    )
    assert len(usuarios) == enviador.enviar.call_count # metodo do mock que conta qnts vezes o metodo foi chamado


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Maciel', email='maciel@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'goldani@gmail.com',
        'Assunto',
        'Conteudo'
    )
    enviador.enviar.assert_called_once_with('goldani@gmail.com', 'maciel@gmail.com', 'Assunto', 'Conteudo')