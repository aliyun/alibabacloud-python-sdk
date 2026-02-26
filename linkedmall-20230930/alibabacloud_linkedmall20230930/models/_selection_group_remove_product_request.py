# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SelectionGroupRemoveProductRequest(DaraModel):
    def __init__(
        self,
        product_ids: List[str] = None,
        purchaser_id: str = None,
    ):
        # This parameter is required.
        self.product_ids = product_ids
        # This parameter is required.
        self.purchaser_id = purchaser_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_ids is not None:
            result['productIds'] = self.product_ids

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productIds') is not None:
            self.product_ids = m.get('productIds')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        return self

