# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OSUser(DaraModel):
    def __init__(
        self,
        group: str = None,
        password: str = None,
        user: str = None,
    ):
        # 用户组。
        self.group = group
        # 用户密码。
        self.password = password
        # 用户名称。
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        if self.password is not None:
            result['Password'] = self.password

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

