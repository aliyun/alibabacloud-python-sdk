# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        client_token: str = None,
        comment: str = None,
        name: str = None,
    ):
        # 命名空间所属的数据目录名称。可通过 ListCatalogs 接口获取已有目录列表
        self.catalog = catalog
        # 用于保证请求幂等性的Token，防止因网络重试导致重复操作。建议使用 UUID
        self.client_token = client_token
        # 命名空间的备注描述信息。传空字符串可清除原有备注，无格式限制
        self.comment = comment
        # 要修改的命名空间名称。名称本身不可修改，此处用于定位目标命名空间。需同时指定所属 Catalog。可通过 ListNamespaces 获取
        # 
        # This parameter is required.
        self.name = name

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

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

