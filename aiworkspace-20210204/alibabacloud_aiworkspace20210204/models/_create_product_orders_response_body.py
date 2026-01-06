# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateProductOrdersResponseBody(DaraModel):
    def __init__(
        self,
        buy_product_request_id: str = None,
        message: str = None,
        order_id: str = None,
        product_ids: List[str] = None,
        request_id: str = None,
    ):
        # The ID of the product purchase request.
        self.buy_product_request_id = buy_product_request_id
        # The returned message.
        self.message = message
        # The purchase order ID.
        self.order_id = order_id
        self.product_ids = product_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_product_request_id is not None:
            result['BuyProductRequestId'] = self.buy_product_request_id

        if self.message is not None:
            result['Message'] = self.message

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyProductRequestId') is not None:
            self.buy_product_request_id = m.get('BuyProductRequestId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

