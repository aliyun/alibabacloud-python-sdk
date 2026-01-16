# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateXpackMonitorConfigRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enable: bool = None,
        endpoints: List[str] = None,
        password: str = None,
        user_name: str = None,
    ):
        self.client_token = client_token
        self.enable = enable
        self.endpoints = endpoints
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable is not None:
            result['enable'] = self.enable

        if self.endpoints is not None:
            result['endpoints'] = self.endpoints

        if self.password is not None:
            result['password'] = self.password

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

