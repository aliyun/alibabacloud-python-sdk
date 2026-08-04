# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeptMemberDTO(DaraModel):
    def __init__(
        self,
        allowed_models: str = None,
        auth_config: str = None,
        gmt_create: str = None,
        id: int = None,
        key_count: int = None,
        login_name: str = None,
        monthly_balance: float = None,
        name: str = None,
        permanent_balance: float = None,
        phone: str = None,
        role_code: str = None,
        role_name: str = None,
    ):
        self.allowed_models = allowed_models
        self.auth_config = auth_config
        self.gmt_create = gmt_create
        self.id = id
        self.key_count = key_count
        self.login_name = login_name
        self.monthly_balance = monthly_balance
        self.name = name
        self.permanent_balance = permanent_balance
        self.phone = phone
        self.role_code = role_code
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.auth_config is not None:
            result['authConfig'] = self.auth_config

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.key_count is not None:
            result['keyCount'] = self.key_count

        if self.login_name is not None:
            result['loginName'] = self.login_name

        if self.monthly_balance is not None:
            result['monthlyBalance'] = self.monthly_balance

        if self.name is not None:
            result['name'] = self.name

        if self.permanent_balance is not None:
            result['permanentBalance'] = self.permanent_balance

        if self.phone is not None:
            result['phone'] = self.phone

        if self.role_code is not None:
            result['roleCode'] = self.role_code

        if self.role_name is not None:
            result['roleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('keyCount') is not None:
            self.key_count = m.get('keyCount')

        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')

        if m.get('monthlyBalance') is not None:
            self.monthly_balance = m.get('monthlyBalance')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('permanentBalance') is not None:
            self.permanent_balance = m.get('permanentBalance')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('roleCode') is not None:
            self.role_code = m.get('roleCode')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        return self

