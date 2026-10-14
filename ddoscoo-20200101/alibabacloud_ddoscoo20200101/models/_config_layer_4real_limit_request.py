# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigLayer4RealLimitRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        limit_value: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.limit_value = limit_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.limit_value is not None:
            result['LimitValue'] = self.limit_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LimitValue') is not None:
            self.limit_value = m.get('LimitValue')

        return self

