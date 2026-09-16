# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLumaNamespacesRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The name of the Agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the Agent. You can call ListLumaCatalogs to obtain the catalog name.
        # 
        # This parameter is required.
        self.catalog = catalog
        # 每页返回的最大数据条数。取值范围 1~100，不传时默认 100。每条记录都需回源查询一次元数据，因此该值同时限制单次调用的回源次数
        self.limit = limit
        # 分页查询的起始Token。首次查询不传或传 "0"；后续翻页使用上一次响应中返回的 NextToken 值
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

