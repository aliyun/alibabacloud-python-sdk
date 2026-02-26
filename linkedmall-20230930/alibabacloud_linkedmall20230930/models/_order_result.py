# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class OrderResult(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        distributor_id: str = None,
        logistics_status: str = None,
        order_amount: int = None,
        order_closed_reason: str = None,
        order_id: str = None,
        order_line_list: List[main_models.OrderLineResult] = None,
        order_status: str = None,
        request_id: str = None,
    ):
        self.create_date = create_date
        self.distributor_id = distributor_id
        self.logistics_status = logistics_status
        self.order_amount = order_amount
        self.order_closed_reason = order_closed_reason
        self.order_id = order_id
        self.order_line_list = order_line_list
        self.order_status = order_status
        self.request_id = request_id

    def validate(self):
        if self.order_line_list:
            for v1 in self.order_line_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['createDate'] = self.create_date

        if self.distributor_id is not None:
            result['distributorId'] = self.distributor_id

        if self.logistics_status is not None:
            result['logisticsStatus'] = self.logistics_status

        if self.order_amount is not None:
            result['orderAmount'] = self.order_amount

        if self.order_closed_reason is not None:
            result['orderClosedReason'] = self.order_closed_reason

        if self.order_id is not None:
            result['orderId'] = self.order_id

        result['orderLineList'] = []
        if self.order_line_list is not None:
            for k1 in self.order_line_list:
                result['orderLineList'].append(k1.to_map() if k1 else None)

        if self.order_status is not None:
            result['orderStatus'] = self.order_status

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')

        if m.get('distributorId') is not None:
            self.distributor_id = m.get('distributorId')

        if m.get('logisticsStatus') is not None:
            self.logistics_status = m.get('logisticsStatus')

        if m.get('orderAmount') is not None:
            self.order_amount = m.get('orderAmount')

        if m.get('orderClosedReason') is not None:
            self.order_closed_reason = m.get('orderClosedReason')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        self.order_line_list = []
        if m.get('orderLineList') is not None:
            for k1 in m.get('orderLineList'):
                temp_model = main_models.OrderLineResult()
                self.order_line_list.append(temp_model.from_map(k1))

        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

