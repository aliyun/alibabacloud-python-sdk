# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetUserPasswordRequest(DaraModel):
    def __init__(
        self,
        generate_random_password: bool = None,
        password: str = None,
        user_name: str = None,
        user_pool_name: str = None,
    ):
        self.generate_random_password = generate_random_password
        self.password = password
        self.user_name = user_name
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_random_password is not None:
            result['GenerateRandomPassword'] = self.generate_random_password

        if self.password is not None:
            result['Password'] = self.password

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateRandomPassword') is not None:
            self.generate_random_password = m.get('GenerateRandomPassword')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

