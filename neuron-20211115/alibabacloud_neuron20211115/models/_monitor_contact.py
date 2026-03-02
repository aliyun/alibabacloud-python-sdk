# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonitorContact(DaraModel):
    def __init__(
        self,
        email: str = None,
        enterprise_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_verify: int = None,
        name: str = None,
        phone: str = None,
    ):
        # This parameter is required.
        self.email = email
        # This parameter is required.
        self.enterprise_id = enterprise_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_verify = is_verify
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.is_verify is not None:
            result['isVerify'] = self.is_verify

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isVerify') is not None:
            self.is_verify = m.get('isVerify')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

