import pytest as pytest

from libpythonprogoldani.spam.enviador_de_email import Enviador
from libpythonprogoldani.spam.main import EnviadorDeSpam
from libpythonprogoldani.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        self.parametros_de_envio = None
        self.qtd_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavo@gmail.com',
        'Assunto',
        'Conteudo'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Maciel', email='maciel@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'goldani@gmail.com',
        'Assunto',
        'Conteudo'
    )
    assert enviador.parametros_de_envio == ('goldani@gmail.com', 'maciel@gmail.com', 'Assunto', 'Conteudo')