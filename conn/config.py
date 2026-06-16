"""Configuração central do Surprise.

Carrega a URL base e o token da API a partir de (nesta ordem de precedência):

1. Variáveis de ambiente ``URL`` / ``TOKEN``
2. Arquivo ``.env`` na raiz (se ``python-dotenv`` estiver instalado)
3. Módulo legado ``var/token.py`` (ignorado pelo git)

Quando nada está configurado, ``URL``/``TOKEN`` ficam como ``None`` e um aviso é
emitido — em vez de quebrar a importação com ``NameError`` como acontecia antes.
"""
import os
import warnings

# Carrega um eventual arquivo .env (opcional — não é erro se a lib não existir).
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def _from_legacy_token_module():
    """Lê url/token do módulo legado var/token.py, se existir."""
    try:
        import var.token as _t  # noqa: WPS433 (import legado opcional)

        return getattr(_t, "url", None), getattr(_t, "token", None)
    except Exception:  # módulo ausente ou malformado — segue sem ele
        return None, None


_legacy_url, _legacy_token = _from_legacy_token_module()

URL = os.getenv("URL") or _legacy_url
TOKEN = os.getenv("TOKEN") or _legacy_token

if not URL or not TOKEN:
    warnings.warn(
        "URL/TOKEN da API não configurados. Defina as variáveis de ambiente "
        "URL e TOKEN (ou um arquivo .env / var/token.py). As chamadas à API "
        "vão falhar até que isso seja configurado.",
        RuntimeWarning,
        stacklevel=2,
    )
