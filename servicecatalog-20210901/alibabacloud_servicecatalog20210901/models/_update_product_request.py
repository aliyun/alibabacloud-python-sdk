# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProductRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        product_id: str = None,
        product_name: str = None,
        provider_name: str = None,
    ):
        # 产品描述
        self.description = description
        # 代表资源一级ID的资源属性字段
        # 
        # This parameter is required.
        self.product_id = product_id
        # 代表资源名称的资源属性字段
        # 
        # This parameter is required.
        self.product_name = product_name
        # 产品提供方
        # 
        # This parameter is required.
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

