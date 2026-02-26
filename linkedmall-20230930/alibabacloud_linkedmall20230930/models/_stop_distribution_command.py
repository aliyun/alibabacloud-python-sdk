# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopDistributionCommand(DaraModel):
    def __init__(
        self,
        lm_shop_id: str = None,
        product_id: str = None,
        request_id: str = None,
        request_time: str = None,
        request_user: str = None,
    ):
        self.lm_shop_id = lm_shop_id
        self.product_id = product_id
        self.request_id = request_id
        self.request_time = request_time
        self.request_user = request_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lm_shop_id is not None:
            result['lmShopId'] = self.lm_shop_id

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.request_time is not None:
            result['requestTime'] = self.request_time

        if self.request_user is not None:
            result['requestUser'] = self.request_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lmShopId') is not None:
            self.lm_shop_id = m.get('lmShopId')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        if m.get('requestUser') is not None:
            self.request_user = m.get('requestUser')

        return self

