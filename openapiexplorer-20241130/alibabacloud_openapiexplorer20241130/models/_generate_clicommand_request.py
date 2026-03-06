# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenerateCLICommandRequest(DaraModel):
    def __init__(
        self,
        aggregate_pagination: bool = None,
        api: str = None,
        api_params: Dict[str, Any] = None,
        api_version: str = None,
        json_api_params: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable aggregation. If you enable this feature, the CLI automatically reads full data by page and aggregates the results.
        # 
        # >Warning: 
        # 
        # Only List operations that support paging can use this switch.
        # 
        # 
        # 
        # - true: enables aggregation.
        # 
        # - false: disables aggregation.
        self.aggregate_pagination = aggregate_pagination
        # The name of the API.
        # 
        # This parameter is required.
        self.api = api
        # The request parameters.
        self.api_params = api_params
        # The version of the API.
        # 
        # This parameter is required.
        self.api_version = api_version
        # The request parameters for the API in JSON format. This parameter has a lower priority than \\`apiParams\\`. If \\`apiParams\\` is set, this parameter is ignored.
        self.json_api_params = json_api_params
        # The product code.
        # 
        # - Call the GetRequestLog operation to obtain the product code from the response.
        # 
        # - Find the product code in the URL of the product in OpenAPI Portal. For example, <props="china">the OpenAPI Portal URL for Short Message Service is https\\://api.aliyun.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
        #   <props="intl">the OpenAPI Portal URL for Short Message Service is https\\://api.alibabacloud.com/product/Dysmsapi. The product code for Short Message Service is Dysmsapi.
        # 
        # This parameter is required.
        self.product = product
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate_pagination is not None:
            result['aggregatePagination'] = self.aggregate_pagination

        if self.api is not None:
            result['api'] = self.api

        if self.api_params is not None:
            result['apiParams'] = self.api_params

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.json_api_params is not None:
            result['jsonApiParams'] = self.json_api_params

        if self.product is not None:
            result['product'] = self.product

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregatePagination') is not None:
            self.aggregate_pagination = m.get('aggregatePagination')

        if m.get('api') is not None:
            self.api = m.get('api')

        if m.get('apiParams') is not None:
            self.api_params = m.get('apiParams')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('jsonApiParams') is not None:
            self.json_api_params = m.get('jsonApiParams')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

