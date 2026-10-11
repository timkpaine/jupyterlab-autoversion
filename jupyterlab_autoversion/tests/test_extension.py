from unittest.mock import MagicMock

import pytest

from jupyterlab_autoversion.extension import load_jupyter_server_extension


class TestExtension:
    @pytest.mark.parametrize("backend", ["s3", "sql"])
    def test_unimplemented_backend(self, backend):
        app = MagicMock()
        app.web_app.settings = {"base_url": "/test"}
        app.config = {"JupyterLabAutoversion": {"backend": backend}}
        with pytest.raises(NotImplementedError, match=backend):
            load_jupyter_server_extension(app)

    def test_load_jupyter_server_extension(self):
        m = MagicMock()

        m.web_app.settings = {}
        m.web_app.settings["base_url"] = "/test"
        m.config = {"JupyterLabAutoversion": {"backend": "git"}}
        load_jupyter_server_extension(m)
