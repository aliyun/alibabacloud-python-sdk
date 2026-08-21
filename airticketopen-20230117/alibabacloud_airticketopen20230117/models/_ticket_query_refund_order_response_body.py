# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketQueryRefundOrderResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TicketQueryRefundOrderResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TicketQueryRefundOrderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TicketQueryRefundOrderResponseBodyData(DaraModel):
    def __init__(
        self,
        refund_orders: List[main_models.TicketQueryRefundOrderResponseBodyDataRefundOrders] = None,
    ):
        self.refund_orders = refund_orders

    def validate(self):
        if self.refund_orders:
            for v1 in self.refund_orders:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RefundOrders'] = []
        if self.refund_orders is not None:
            for k1 in self.refund_orders:
                result['RefundOrders'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refund_orders = []
        if m.get('RefundOrders') is not None:
            for k1 in m.get('RefundOrders'):
                temp_model = main_models.TicketQueryRefundOrderResponseBodyDataRefundOrders()
                self.refund_orders.append(temp_model.from_map(k1))

        return self

class TicketQueryRefundOrderResponseBodyDataRefundOrders(DaraModel):
    def __init__(
        self,
        fund_status: int = None,
        order_status: int = None,
    ):
        self.fund_status = fund_status
        self.order_status = order_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fund_status is not None:
            result['FundStatus'] = self.fund_status

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundStatus') is not None:
            self.fund_status = m.get('FundStatus')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        return self

