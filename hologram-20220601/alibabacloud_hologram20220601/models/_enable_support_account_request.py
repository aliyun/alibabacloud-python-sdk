# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableSupportAccountRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        enabled: bool = None,
        expire_time: str = None,
        password: str = None,
    ):
        self.region_id = region_id
        self.enabled = enabled
        self.expire_time = expire_time
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.password is not None:
            result['password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('password') is not None:
            self.password = m.get('password')

        return self

