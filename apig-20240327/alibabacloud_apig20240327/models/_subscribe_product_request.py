# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubscribeProductRequest(DaraModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # The ID of the API product to subscribe to. This is the primary ID of the API product resource. You can obtain this ID from the productId field in the response of the ListProducts operation.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_id is not None:
            result['productId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        return self

