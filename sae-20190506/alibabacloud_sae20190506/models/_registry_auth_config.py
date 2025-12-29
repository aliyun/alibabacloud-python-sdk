# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegistryAuthConfig(DaraModel):
    def __init__(
        self,
        password: str = None,
        role: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['password'] = self.password

        if self.role is not None:
            result['role'] = self.role

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

