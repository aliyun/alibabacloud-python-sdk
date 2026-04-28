# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAdvisorResourcesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        resource_id: str = None,
    ):
        self.keyword = keyword
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product is not None:
            result['Product'] = self.product

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

