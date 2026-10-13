# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LoginDeveloperRequest(DaraModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # The password of the developer account. This field is marked as sensitive in the API definition.
        self.password = password
        # The developer logon username.
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

