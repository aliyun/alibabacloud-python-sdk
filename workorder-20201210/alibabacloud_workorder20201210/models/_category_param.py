# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CategoryParam(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        category_name: str = None,
        is_select_from_dialog: bool = None,
        product_id: int = None,
        product_name: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.is_select_from_dialog = is_select_from_dialog
        self.product_id = product_id
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.is_select_from_dialog is not None:
            result['IsSelectFromDialog'] = self.is_select_from_dialog

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('IsSelectFromDialog') is not None:
            self.is_select_from_dialog = m.get('IsSelectFromDialog')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        return self

