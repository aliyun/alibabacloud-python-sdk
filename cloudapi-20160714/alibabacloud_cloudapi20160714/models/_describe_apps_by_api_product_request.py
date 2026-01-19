# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppsByApiProductRequest(DaraModel):
    def __init__(
        self,
        api_product_id: str = None,
        app_name: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        # The ID of the API product.
        # 
        # This parameter is required.
        self.api_product_id = api_product_id
        # The application name.
        self.app_name = app_name
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_product_id is not None:
            result['ApiProductId'] = self.api_product_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProductId') is not None:
            self.api_product_id = m.get('ApiProductId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

