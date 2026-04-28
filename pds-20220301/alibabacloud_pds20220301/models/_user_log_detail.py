# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class UserLogDetail(DaraModel):
    def __init__(
        self,
        email: str = None,
        expired_at: int = None,
        name: str = None,
        phone: str = None,
        role_id: str = None,
        update_to: main_models.UserLogDetailUpdateTo = None,
    ):
        self.email = email
        self.expired_at = expired_at
        self.name = name
        self.phone = phone
        self.role_id = role_id
        self.update_to = update_to

    def validate(self):
        if self.update_to:
            self.update_to.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.expired_at is not None:
            result['expired_at'] = self.expired_at

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.role_id is not None:
            result['role_id'] = self.role_id

        if self.update_to is not None:
            result['update_to'] = self.update_to.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('expired_at') is not None:
            self.expired_at = m.get('expired_at')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        if m.get('update_to') is not None:
            temp_model = main_models.UserLogDetailUpdateTo()
            self.update_to = temp_model.from_map(m.get('update_to'))

        return self

class UserLogDetailUpdateTo(DaraModel):
    def __init__(
        self,
        email: str = None,
        expired_at: int = None,
        name: str = None,
        phone: str = None,
        role_id: str = None,
    ):
        self.email = email
        self.expired_at = expired_at
        self.name = name
        self.phone = phone
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.expired_at is not None:
            result['expired_at'] = self.expired_at

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.role_id is not None:
            result['role_id'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('expired_at') is not None:
            self.expired_at = m.get('expired_at')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        return self

