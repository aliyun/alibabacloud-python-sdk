# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ProductSaleInfoListQuery(DaraModel):
    def __init__(
        self,
        division_code: str = None,
        product_ids: List[str] = None,
        purchaser_id: str = None,
    ):
        # Area code (recommended to use a five-level township/street-level address code)
        self.division_code = division_code
        # Collection of product IDs to query, supporting batch queries of 1 to 10 items
        # 
        # This parameter is required.
        self.product_ids = product_ids
        # Purchaser ID
        # 
        # This parameter is required.
        self.purchaser_id = purchaser_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        if self.product_ids is not None:
            result['productIds'] = self.product_ids

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        if m.get('productIds') is not None:
            self.product_ids = m.get('productIds')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        return self

