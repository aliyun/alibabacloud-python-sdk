# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTokenRequest(DaraModel):
    def __init__(
        self,
        audience: str = None,
        expire_time: int = None,
        instance_id: str = None,
        type: str = None,
    ):
        self.audience = audience
        # The validity period. Unit: seconds.
        self.expire_time = expire_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audience is not None:
            result['Audience'] = self.audience

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audience') is not None:
            self.audience = m.get('Audience')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

