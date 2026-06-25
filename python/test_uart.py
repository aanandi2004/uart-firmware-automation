from uart_controller import send_command, close_connection

def test_version():
    response = send_command("VERSION")
    assert "V1.3.0" in response

def teardown_module(module):
    close_connection()