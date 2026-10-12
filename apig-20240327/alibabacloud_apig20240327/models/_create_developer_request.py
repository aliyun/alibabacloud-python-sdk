# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeveloperRequest(DaraModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # The password of the developer account. The length must be 6 to 32 characters.
        self.password = password
        # The logon username of the developer. The length must not exceed 64 characters.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['password'] = self.password

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

