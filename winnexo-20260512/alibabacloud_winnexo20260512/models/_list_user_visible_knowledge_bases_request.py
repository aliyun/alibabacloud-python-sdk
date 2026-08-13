# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserVisibleKnowledgeBasesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        tenant_id: str = None,
    ):
        # 知识库名称或描述关键词；不传时返回全部可见知识库
        self.keyword = keyword
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

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

