# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class OrderListResult(DaraModel):
    def __init__(
        self,
        order_list: List[main_models.OrderResult] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.order_list = order_list
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.order_list:
            for v1 in self.order_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['orderList'] = []
        if self.order_list is not None:
            for k1 in self.order_list:
                result['orderList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_list = []
        if m.get('orderList') is not None:
            for k1 in m.get('orderList'):
                temp_model = main_models.OrderResult()
                self.order_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

