# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTablesRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        limit: int = None,
        namespace: str = None,
        next_token: str = None,
    ):
        # 表所属的数据目录名称。可通过 ListCatalogs 获取
        self.catalog = catalog
        # 每页返回的最大数据条数。不传时默认 10，最大 100
        self.limit = limit
        # 表所属的命名空间名称。可通过 ListNamespaces 获取
        self.namespace = namespace
        # 分页查询的起始Token。首次查询不传或传 "0"；后续翻页使用上一次响应中返回的 NextToken 值
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

