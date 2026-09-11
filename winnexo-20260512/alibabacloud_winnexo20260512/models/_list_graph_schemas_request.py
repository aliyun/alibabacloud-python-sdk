# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListGraphSchemasRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        semantic_tags: List[str] = None,
        tenant_id: str = None,
    ):
        # 关键词，匹配 graphName / displayName（可选，忽略大小写）
        self.keyword = keyword
        # 语义标签过滤（可选，命中任一标签即保留）
        self.semantic_tags = semantic_tags
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.semantic_tags is not None:
            result['semanticTags'] = self.semantic_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('semanticTags') is not None:
            self.semantic_tags = m.get('semanticTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

