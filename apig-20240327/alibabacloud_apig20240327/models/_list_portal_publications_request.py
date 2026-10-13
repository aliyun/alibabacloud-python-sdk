# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPortalPublicationsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        product_name: str = None,
    ):
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The API product name. This corresponds to the productName field in the response list items.
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.product_name is not None:
            result['productName'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        return self

