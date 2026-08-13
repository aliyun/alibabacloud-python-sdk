# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseSourceTagsRequest(DaraModel):
    def __init__(
        self,
        source_id: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # 数据源 ID（租户内唯一）
        # 
        # This parameter is required.
        self.source_id = source_id
        # 资源标签（JSON 字符串列表，如 ["tagA","tagB"]；传 null 表示清空标签）
        self.source_tags = source_tags
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

