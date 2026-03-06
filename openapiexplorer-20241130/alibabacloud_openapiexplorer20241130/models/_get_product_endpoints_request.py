# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProductEndpointsRequest(DaraModel):
    def __init__(
        self,
        product: str = None,
    ):
        # The product code.
        # 
        # - Call the GetRequestLog operation and find the product code in the response.
        # 
        # - Find the product code in the URL of the OpenAPI Portal page for the product. For example, <props="china">the URL for the Short Message Service (SMS) OpenAPI Portal page is https\\://api.aliyun.com/product/Dysmsapi. The product code is Dysmsapi.
        #   <props="intl">the URL for the Short Message Service (SMS) OpenAPI Portal page is https\\://api.alibabacloud.com/product/Dysmsapi. The product code is Dysmsapi.
        # 
        # This parameter is required.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')

        return self

