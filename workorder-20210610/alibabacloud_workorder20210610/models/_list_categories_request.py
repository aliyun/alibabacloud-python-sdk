# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCategoriesRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        name: str = None,
        product_id: int = None,
    ):
        # Multi-language, support, Chinese, English. Value definition: zh: Chinese, en: English.
        self.language = language
        # The name of the classification question. Fuzzy search is supported.
        self.name = name
        # The ID of the product. You can call the ListProducts operation to obtain the product ID. The ProductId parameter is the ID of an Alibaba Cloud product. Multiple Categories are displayed for each product.
        # 
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        return self

