# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCatalogRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        name: str = None,
    ):
        # 用于保证请求幂等性的Token。建议使用 UUID
        self.client_token = client_token
        # 要查询的数据目录名称。可通过 ListCatalogs 接口获取已有目录列表
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

