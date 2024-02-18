import main
import pytest
from io import StringIO
import os

#funcion para prueba de iniciar_sesion
def test_iniciar_sesion(monkeypatch, capsys):
    #simulacion de login de user
    monkeypatch.setattr('sys.stdin', StringIO('test_user\ntest_password\n'))

    main.iniciar_sesion()

    #captura de salidad de iniciar_sesion
    captured = capsys.readouterr()
    assert "Inicio de sesión exitoso." in captured.out

#funcion para prueba de guardar_credenciales
@pytest.mark.parametrize("app_name, username, password", [("app_test", "user_test", "pass_test")])
def test_guardar_credenciales(monkeypatch, capsys, tmp_path, app_name, username, password):
    filename = "credenciales.json"

    #simulacion de entrada de las credenciales del usuario
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join([app_name, username, password]) + '\n'))

    main.guardar_credenciales()

    #verificar la credenciales del usuario
    with open(filename, "r") as f:
        data = f.read()
        assert app_name in data
        assert username in data
        assert password in data

#funcion para prueba de verificacion del guardado de las credenciales duplicadas
def test_guardar_credenciales_duplicadas(monkeypatch, capsys, tmp_path):
    filename = tmp_path / "credenciales.json"
    with open(filename, 'w') as f:
        f.write('{"app_existing": {"username": "user_existing", "password": "pass_existing"}}')

    #entrada de las credencias nuevas del usuario
    monkeypatch.setattr('sys.stdin', StringIO('app_existing\nuser_existing\npass_existing\n'))

    main.guardar_credenciales()

    #captura de la salidad de las credenciales duplicadas
    captured = capsys.readouterr()
    assert "Ya se ha guardado una contraseña para esta aplicación." in captured.out