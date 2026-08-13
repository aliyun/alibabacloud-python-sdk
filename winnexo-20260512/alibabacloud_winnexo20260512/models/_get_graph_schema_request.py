# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGraphSchemaRequest(DaraModel):
    def __init__(
        self,
        graph_name: str = None,
        tenant_id: str = None,
    ):
        # 图谱名称，可先调用 listGraphs 获取
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

