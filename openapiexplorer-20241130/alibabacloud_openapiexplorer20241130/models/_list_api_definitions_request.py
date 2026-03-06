# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiDefinitionsRequest(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        product: str = None,
    ):
        # The version of the API.
        # 
        # This parameter is required.
        self.api_version = api_version
        # The product code.
        # 
        # - Call the GetRequestLog operation to obtain the product code from the response.
        # 
        # - Find the product code in the URL of the OpenAPI Portal. For example, <props="china">the URL of the OpenAPI Portal for Short Message Service is https\\://api.aliyun.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
        #   <props="intl">the URL of the OpenAPI Portal for Short Message Service is https\\://api.alibabacloud.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
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
        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

