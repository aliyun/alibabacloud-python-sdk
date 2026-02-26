# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class DistributeProductCommand(DaraModel):
    def __init__(
        self,
        lm_shop_id: str = None,
        products: List[main_models.DistributionProduct] = None,
        request_id: str = None,
        request_time: str = None,
        request_user: str = None,
    ):
        self.lm_shop_id = lm_shop_id
        self.products = products
        self.request_id = request_id
        self.request_time = request_time
        self.request_user = request_user

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lm_shop_id is not None:
            result['lmShopId'] = self.lm_shop_id

        result['products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['products'].append(k1.to_map() if k1 else None)

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

        self.products = []
        if m.get('products') is not None:
            for k1 in m.get('products'):
                temp_model = main_models.DistributionProduct()
                self.products.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        if m.get('requestUser') is not None:
            self.request_user = m.get('requestUser')

        return self

