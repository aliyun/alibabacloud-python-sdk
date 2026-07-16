# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class User(DaraModel):
    def __init__(
        self,
        group: str = None,
        password: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        # 用户组。
        self.group = group
        # 用户密码。
        # 
        # This parameter is required.
        self.password = password
        # 用户ID。
        # 
        # This parameter is required.
        self.user_id = user_id
        # 用户名称。
        # 
        # This parameter is required.
        self.user_name = user_name
        # 用户类型。
        self.user_type = user_type

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

