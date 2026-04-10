# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasourceConfigUnified(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # Prometheus 实例 ID（type=PROMETHEUS 时使用）
        self.instance_id = instance_id
        # 地域 ID（各类型可选，缺省与规则/网关一致）
        self.region_id = region_id
        # 数据源类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

