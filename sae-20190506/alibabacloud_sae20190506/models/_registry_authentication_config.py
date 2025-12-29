# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegistryAuthenticationConfig(DaraModel):
    def __init__(
        self,
        password: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['Password'] = self.password

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

