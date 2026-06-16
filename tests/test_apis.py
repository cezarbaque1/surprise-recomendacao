import conn.apis as apis


def test_make_request_sem_credenciais(monkeypatch):
    monkeypatch.setattr(apis, "URL", None)
    monkeypatch.setattr(apis, "TOKEN", None)
    msg = apis.make_request("GET", "http://x")
    assert "Configuração ausente" in msg


def test_make_request_sucesso(monkeypatch):
    monkeypatch.setattr(apis, "URL", "http://api")
    monkeypatch.setattr(apis, "TOKEN", "t")

    class FakeResp:
        status_code = 200
        text = '[{"a": 1}]'

    monkeypatch.setattr(apis.requests, "request", lambda *a, **k: FakeResp())
    assert apis.make_request("GET", "http://api/x") == [{"a": 1}]


def test_make_request_status_erro(monkeypatch):
    monkeypatch.setattr(apis, "URL", "http://api")
    monkeypatch.setattr(apis, "TOKEN", "t")

    class FakeResp:
        status_code = 500
        text = ""

    monkeypatch.setattr(apis.requests, "request", lambda *a, **k: FakeResp())
    assert "status code 500" in apis.make_request("GET", "http://api/x")
