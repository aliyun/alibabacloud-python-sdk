# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SelectionGroupAddProductResponseBody(DaraModel):
    def __init__(
        self,
        product_ids: List[str] = None,
    ):
        self.product_ids = product_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_ids is not None:
            result['productIds'] = self.product_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productIds') is not None:
            self.product_ids = m.get('productIds')

        return self

