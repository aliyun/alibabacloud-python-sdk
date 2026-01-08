# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ServiceConfig(DaraModel):
    def __init__(
        self,
        code_server_auth: str = None,
        code_server_password: str = None,
        jupyter_server_auth: str = None,
        jupyter_server_password: str = None,
    ):
        self.code_server_auth = code_server_auth
        self.code_server_password = code_server_password
        self.jupyter_server_auth = jupyter_server_auth
        self.jupyter_server_password = jupyter_server_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_server_auth is not None:
            result['CodeServerAuth'] = self.code_server_auth

        if self.code_server_password is not None:
            result['CodeServerPassword'] = self.code_server_password

        if self.jupyter_server_auth is not None:
            result['JupyterServerAuth'] = self.jupyter_server_auth

        if self.jupyter_server_password is not None:
            result['JupyterServerPassword'] = self.jupyter_server_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeServerAuth') is not None:
            self.code_server_auth = m.get('CodeServerAuth')

        if m.get('CodeServerPassword') is not None:
            self.code_server_password = m.get('CodeServerPassword')

        if m.get('JupyterServerAuth') is not None:
            self.jupyter_server_auth = m.get('JupyterServerAuth')

        if m.get('JupyterServerPassword') is not None:
            self.jupyter_server_password = m.get('JupyterServerPassword')

        return self

