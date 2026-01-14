# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFootprintListRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        page_size: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The pagination parameter. The number of the page that starts from 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries returned on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.product_type is not None:
            result['productType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        return self

