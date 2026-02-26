# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class GetDistributionProductResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        products: List[main_models.DistributionProduct] = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.products = products
        self.request_id = request_id

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
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['products'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.products = []
        if m.get('products') is not None:
            for k1 in m.get('products'):
                temp_model = main_models.DistributionProduct()
                self.products.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

