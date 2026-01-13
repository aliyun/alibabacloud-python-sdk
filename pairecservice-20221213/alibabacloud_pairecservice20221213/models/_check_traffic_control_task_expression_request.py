# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckTrafficControlTaskExpressionRequest(DaraModel):
    def __init__(
        self,
        expression: str = None,
        instance_id: str = None,
        table_meta_id: str = None,
    ):
        # This parameter is required.
        self.expression = expression
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.table_meta_id = table_meta_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        return self

