# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataResultValue(DaraModel):
    def __init__(
        self,
        sql_id: str = None,
        instance_id: str = None,
        count: int = None,
    ):
        self.sql_id = sql_id
        self.instance_id = instance_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.count is not None:
            result['count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('count') is not None:
            self.count = m.get('count')

        return self

