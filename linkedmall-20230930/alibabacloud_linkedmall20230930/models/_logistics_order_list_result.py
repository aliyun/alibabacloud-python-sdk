# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class LogisticsOrderListResult(DaraModel):
    def __init__(
        self,
        logistics_order_list: List[main_models.LogisticsOrderResult] = None,
        request_id: str = None,
    ):
        self.logistics_order_list = logistics_order_list
        self.request_id = request_id

    def validate(self):
        if self.logistics_order_list:
            for v1 in self.logistics_order_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['logisticsOrderList'] = []
        if self.logistics_order_list is not None:
            for k1 in self.logistics_order_list:
                result['logisticsOrderList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logistics_order_list = []
        if m.get('logisticsOrderList') is not None:
            for k1 in m.get('logisticsOrderList'):
                temp_model = main_models.LogisticsOrderResult()
                self.logistics_order_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

