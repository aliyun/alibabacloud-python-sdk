# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTableRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        client_token: str = None,
        name: str = None,
        namespace: str = None,
    ):
        # 表所属的数据目录名称。可通过 ListCatalogs 获取
        self.catalog = catalog
        # 用于保证请求幂等性的Token。建议使用 UUID
        self.client_token = client_token
        # 要删除的事件表名称。删除后不可恢复，表中的所有数据将被永久清除。需同时指定所属 Catalog 和 Namespace。可通过 ListTables 获取
        # 
        # This parameter is required.
        self.name = name
        # 表所属的命名空间名称。可通过 ListNamespaces 获取
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

