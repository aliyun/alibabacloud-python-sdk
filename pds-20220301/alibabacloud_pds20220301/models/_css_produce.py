# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CssProduce(DaraModel):
    def __init__(
        self,
        bid: str = None,
        buyer_id: int = None,
        child_id: int = None,
        from_app: str = None,
        order_id: int = None,
        payer_id: int = None,
        purchases: List[main_models.CssPurchase] = None,
        request_id: str = None,
        skip_channel: bool = None,
        token: str = None,
        user_id: int = None,
    ):
        self.bid = bid
        self.buyer_id = buyer_id
        self.child_id = child_id
        self.from_app = from_app
        self.order_id = order_id
        self.payer_id = payer_id
        self.purchases = purchases
        self.request_id = request_id
        self.skip_channel = skip_channel
        self.token = token
        self.user_id = user_id

    def validate(self):
        if self.purchases:
            for v1 in self.purchases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['bid'] = self.bid

        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id

        if self.child_id is not None:
            result['childId'] = self.child_id

        if self.from_app is not None:
            result['fromApp'] = self.from_app

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.payer_id is not None:
            result['payerId'] = self.payer_id

        result['purchases'] = []
        if self.purchases is not None:
            for k1 in self.purchases:
                result['purchases'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.skip_channel is not None:
            result['skipChannel'] = self.skip_channel

        if self.token is not None:
            result['token'] = self.token

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bid') is not None:
            self.bid = m.get('bid')

        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')

        if m.get('childId') is not None:
            self.child_id = m.get('childId')

        if m.get('fromApp') is not None:
            self.from_app = m.get('fromApp')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('payerId') is not None:
            self.payer_id = m.get('payerId')

        self.purchases = []
        if m.get('purchases') is not None:
            for k1 in m.get('purchases'):
                temp_model = main_models.CssPurchase()
                self.purchases.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skipChannel') is not None:
            self.skip_channel = m.get('skipChannel')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

