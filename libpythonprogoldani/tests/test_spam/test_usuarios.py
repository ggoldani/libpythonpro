from libpythonprogoldani.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gustavo', email='gustavo@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Goldani', email='goldani@gmail.com'),
        Usuario(nome='Maciel', email='maciel@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
