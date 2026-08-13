# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenameKnowledgeBaseSourceRequest(DaraModel):
    def __init__(
        self,
        new_name: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # 新的数据源名称
        # 
        # This parameter is required.
        self.new_name = new_name
        # 数据源 ID（租户内唯一）
        # 
        # This parameter is required.
        self.source_id = source_id
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_name is not None:
            result['newName'] = self.new_name

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newName') is not None:
            self.new_name = m.get('newName')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

